"use strict";

/*
Configure how embedded relationships (ref properties) are mapped to graph
edges.  This map maps a STIX type to a list of triples, where each triple
describes an embedded relationship.  Each triple consists of (1) a
property path, (2) an edge label, and (3) a boolean which determines the
directionality of the edge: true to point to the referent, or false to point
to the referring object.

The null key maps to embedded relationships which should be checked on all
object types.  This is appropriate for common properties many objects can have.

A property path is a string formatted as a sequence of property names
separated by dots.  See getValuesAtPath().
*/
let embeddedRelationships = new Map([
    [null, [
        ["created_by_ref", "created-by", true],
        ["object_marking_refs", "applies-to", false]
    ]],
    ["directory", [
        ["contains_refs", "contains", true]
    ]],
    ["domain-name", [
        ["resolves_to_refs", "resolves-to", true]
    ]],
    ["email-addr", [
        ["belongs_to_ref", "belongs-to", true]
    ]],
    ["email-message", [
        ["from_ref", "from", true],
        ["sender_ref", "sent-by", true],
        ["to_refs", "to", true],
        ["cc_refs", "cc", true],
        ["bcc_refs", "bcc", true],
        ["raw_email_ref", "raw-binary-of", false]
    ]],
    ["file", [
        ["contains_refs", "contains", true],
        ["content_ref", "contents-of", false],
        ["parent_directory_ref", "parent-of", false]
    ]],
    ["grouping", [
        ["object_refs", "refers-to", true]
    ]],
    ["ipv4-addr", [
        ["resolves_to_refs", "resolves-to", true]
    ]],
    ["ipv6-addr", [
        ["resolves_to_refs", "resolves-to", true]
    ]],
    ["language-content", [
        ["object_ref", "applies-to", true]
    ]],
    ["malware", [
        ["sample_refs", "sample-of", false]
    ]],
    ["malware-behavior", [
	["extensions.extension-definition--8e9e338f-c9ee-4d4f-8cac-85b4dcfdf3c1.related_object_refs", "related-to", false]
	// ["contributor_refs", "contributed-by", false]
    ]],	
    ["malware-method", [
	["extensions.extension-definition--8e9e338f-c9ee-4d4f-8cac-85b4dcfdf3c1.behavior_ref", "demonstrates", false]
    ]],
    ["malware-objective", [
        ["extensions.extension-definition--8e9e338f-c9ee-4d4f-8cac-85b4dcfdf3c1.created_by_ref", "created-by", false],
	["extensions.extension-definition--8e9e338f-c9ee-4d4f-8cac-85b4dcfdf3c1.object_marking_refs", "applies-to", false]
    ]],
    ["malware-analysis", [
        ["analysis_sco_refs", "captured-by", false]
    ]],
    ["network-traffic", [
        ["src_ref", "source-of", false],
        ["dst_ref", "destination-of", false],
        ["src_payload_ref", "source-payload-of", false],
        ["dst_payload_ref", "destination-payload-of", false],
        ["encapsulates_refs", "encapsulated-by", false],
        ["encapsulated_by_ref", "encapsulated-by", true]
    ]],
    ["note", [
        ["object_refs", "refers-to", true]
    ]],
    ["observed-data", [
        ["object_refs", "refers-to", true]
    ]],
    ["opinion", [
        ["object_refs", "refers-to", true]
    ]],
    ["process", [
        ["opened_connection_refs", "opened-by", false],
        ["creator_user_ref", "created-by", true],
        ["image_ref", "image-of", false],
        ["parent_ref", "parent-of", false]
    ]],
    ["report", [
        ["object_refs", "refers-to", true]
    ]],
    ["sighting", [
        ["sighting_of_ref", "sighting-of", true],
        ["observed_data_refs", "observed", true],
        ["where_sighted_refs", "saw", false]
    ]],
    ["windows-registry-key", [
        ["creator_user_ref", "created-by", true]
    ]],
	["attack-pattern", [
        ["created_by_ref", "created-by", false]
    ]]
]);


// Defines operator support for the mongo-ish match algorithm.
let valueOps = new Map([
    ["$eq", (a, b) => a === b],
    ["$gt", (a, b) => a > b],
    ["$gte", (a, b) => a >= b],
    ["$in", (val, arr) => arr.includes(val)],
    ["$lt", (a, b) => a < b],
    ["$lte", (a, b) => a <= b],
    ["$ne", (a, b) => a !== b],
    ["$nin", (val, arr) => !arr.includes(val)]
]);


/**
 * Instances represent general invalid STIX content passed into the visualizer.
 */
class STIXContentError extends Error
{
    constructor(message=null, opts=null)
    {
        // Use a default generic message.
        if (!message)
            message = "Invalid STIX content: expected a non-empty mapping"
            + " (object or Map) which is a single STIX object or bundle with"
            + " at least one object, or a non-empty array of objects.";

        super(message, opts);
    }
}


/**
 * Instances represent a particular invalid STIX object.
 */
class InvalidSTIXObjectError extends STIXContentError
{
    constructor(stixObject, opts=null)
    {
        let message = "Invalid STIX object: requires at least type and id"
        + " properties";

        // May as well give some extra info if we know it.  It may seem
        // silly to say we require an id property... and them give the value
        // of the id property!  I think users will get the idea.
        let stixId = stixObject.get("id");
        if (stixId)
            message += ": " + stixId;

        super(message, opts);

        this.stixObject = stixObject;
    }
}


/**
 * Instances represent an invalid configuration value.
 */
class InvalidConfigError extends Error
{
    constructor(message=null, opts=null)
    {
        if (!message)
            message = "Invalid configuration value: must be a JSON or"
                      + " Javascript object.";

        super(message, opts);
    }
}


/**
 * Instances represent an invalid operator in match criteria for STIX objects.
 */
class InvalidMatchOperator extends Error
{
    constructor(op=null, opts=null)
    {
        let message = "In match criteria, invalid operator: " + op;

        super(message, opts);
    }
}


/**
 * Determine whether the given value is a plain javascript object.  E.g. one
 * which was given as an object literal.
 */
function isPlainObject(value)
{
    let result = false;

    // null/undefined would cause errors in Object.getPrototypeOf(), and
    // {} and [] are actually truthy in javascript!  I don't think anything
    // falsey could be a plain object.
    if (value)
        // https://stackoverflow.com/questions/52001739/what-is-considered-a-plain-object
        result = Object.getPrototypeOf(value) === Object.prototype;

    return result;
}


/**
 * A JSON.parse() "reviver" function which may be used to cause JSON.parse()
 * to produce a Map instead of a plain javascript object (from a JSON object).
 */
function mapReviver(key, value)
{
    if (isPlainObject(value))
        return new Map(Object.entries(value));
    else
        return value;
}


/**
 * Recursively search through the given value and convert all plain objects
 * found into Map's.
 */
function recursiveObjectToMap(obj)
{
    let newValue;

    if (isPlainObject(obj))
    {
        let map = new Map();
        for (let [key, value] of Object.entries(obj))
            map.set(key, recursiveObjectToMap(value));

        newValue = map;
    }
    else if (Array.isArray(obj))
        newValue = obj.map(recursiveObjectToMap);
    else
        newValue = obj;

    return newValue;
}


/**
 * Convert the given content to a data structure which uses Maps.  E.g. for
 * strings, do the same thing as normal JSON.parse(), but translate JSON
 * objects into Javascript Maps instead of plain objects.  For plain objects,
 * convert them and their sub-objects to Maps.  That way we can use more sane
 * container types.
 *
 * @param jsonContent A JSON string, plain object, or array
 * @return The converted content
 */
function parseToMap(jsonContent)
{
    let newValue;

    if (typeof jsonContent === "string" || jsonContent instanceof String)
        newValue = JSON.parse(jsonContent, mapReviver);
    else
        newValue = recursiveObjectToMap(jsonContent);

    return newValue;
}

/**
 * Check value(s) for a match against some criteria.  This is inspired by
 * Mongo queries, but isn't the same.  It is Mongo-ish.  The value(s) to be
 * checked are inside the given object, identified by the given property path.
 *
 * This function differs from mongoishMatchObject() in that it operates on
 * potentially multiple values instead of just one (due to the propPath
 * selector), and it supports the "$exists" operator at the top level to check
 * existence.
 *
 * The "$exists" key must be mapped to a boolean value.  If the mapped
 * value is true, the check evaluates to true iff any values are selected by
 * propPath.  If the mapped value is false, the check evaluates to true iff no
 * value is selected by propPath.
 *
 * Otherwise, it behaves analogously to the aforementioned function.  See its
 * documentation for more details.
 *
 * @param object A Map instance
 * @param propPath A property path which selects some values within object
 * @param criteria Some match criteria
 * @return true if any of the selected values match; false otherwise
 */
function mongoishMatchProperty(object, propPath, criteria)
{
    // Separate various types of criteria.
    let logicalCriteria = new Map();
    let valueCriteria = new Map();
    let presenceCriteria = new Map();

    if (criteria instanceof Map)
    {
        for (let [critPropName, critPropValue] of criteria)
        {
            if (["$and", "$or", "$not"].includes(critPropName))
                logicalCriteria.set(critPropName, critPropValue);
            else if (valueOps.has(critPropName))
                valueCriteria.set(critPropName, critPropValue);
            else if (critPropName === "$exists")
                presenceCriteria.set(critPropName, critPropValue);
            else if (critPropName.startsWith("$"))
                throw new InvalidMatchOperator(critPropName);
            else
                // Another property path style check
                valueCriteria.set(critPropName, critPropValue);
        }
    }
    else
        // Non-map: treat the same as a plain equality check.
        valueCriteria.set("$eq", criteria);

    let result = true;

    // Check logical criteria
    for (let [logicalOp, subCriteria] of logicalCriteria)
    {
        if (logicalOp === "$or")
        {
            let orResult = false;
            for (let subCriterion of subCriteria)
                if (mongoishMatchProperty(object, propPath, subCriterion))
                {
                    orResult = true;
                    break;
                }

            result &&= orResult;
        }
        else if (logicalOp === "$and")
        {
            let andResult = true;
            for (let subCriterion of subCriteria)
                if (!mongoishMatchProperty(object, propPath, subCriterion))
                {
                    andResult = false;
                    break;
                }

            result &&= andResult;
        }
        else  // logicalOp === "$not"
            result &&= !mongoishMatchProperty(
                object, propPath, subCriteria
            );

        if (!result)
            break;
    }

    let anyValuesFound = false;
    if (result)
    {
        // Check value criteria.  If there aren't any, this check trivially
        // passes.  But we still need to go as far as ascertaining whether any
        // values exist which match the propPath selector.  That is necessary
        // for any subsequent presence checking.
        //
        // If there are any value criteria, the implied per-value checks here
        // are implicitly OR'd.
        if (valueCriteria.size > 0)
            result = false;

        for (let propValue of getValuesAtPath(object, propPath))
        {
            anyValuesFound = true;

            // If already trivially passed (see above), this loop really just
            // acts to tell whether the property path refers to any values.
            // There is no need to test any values against criteria.  If we are
            // in this loop body, we found a referent value.
            if (result)
                break;

            result = mongoishMatchObject(propValue, valueCriteria);

            if (result)
                break;
        }
    }

    // Check presence criteria.
    if (result)
    {
        // Hard-code handling of the only presence criterion we support.
        if (presenceCriteria.has("$exists"))
        {
            let exists = presenceCriteria.get("$exists");  // true or false
            result &&= (exists === anyValuesFound);
        }
    }

    return result;
}


/**
 * Check a value for a match against some criteria.  This is inspired by
 * Mongo queries, but isn't the same.  It is Mongo-ish.
 *
 * The value and criteria can be anything.  It is most interesting though, if
 * both are Map instances.  If neither is a Map, this acts as an equality check
 * (using "===", with the weirdness that entails).  If the value is a Map and
 * criteria is not, it's an automatic non-match.  If value is not a Map but
 * criteria is, one can obtain simple comparisons using some Mongo-style
 * operators, e.g. "$lt".
 *
 * Criteria as a Map is a conjunction of a few types of checks (i.e. all checks
 * are implicitly AND'd): logical, value, and property.  The last is applicable
 * only to Map values since others don't have any properties.  Each key/value
 * pair constitutes one of these types of checks, as follows:
 *
 * If the key is "$and", "$or", or "$not", then it is a logical check.  The
 * key must map to an array of checks in the first two cases, and any check in
 * the latter case.  For "$not", the mapped check is performed and the result
 * is simply inverted.  It does *not* invert nested operators.
 *
 * If the key is "$eq", "$gt", "$gte" "$in", "$lt", "$lte" "$ne", "$nin",
 * then it is a "value" check, i.e. a check of the value as a whole, not any
 * of its properties (if applicable).  The "$in" and "$nin" operators must be
 * mapped to arrays (they mean "in" and "not in" the given array).
 *
 * A string property name which does not begin with a "$" is treated as a
 * property path, i.e. a type of "selector" of values within a Map.  The
 * property path maps to some check.  The result is a disjunction over checks
 * of all selected values, i.e. it is implicitly OR'd.  See getValuesAtPath()
 * for property path syntax and semantics.  Property path checks support an
 * additional "$exists" operator to check whether any values are selected (the
 * values themselves are irrelevant).  This amounts to a type of existence
 * check.  See mongoishMatchProperty() for for details on "$exists".
 *
 * For example, given:
 *
 * {
 *     "foo": [
 *         {"bar": 1}
 *         {"bar": 2}
 *     ]
 * }
 *
 * Criteria:
 *
 * {"foo.bar": 1} results in a match
 * {"foo.bar": {"$or": [2, 3]}} results in a match
 * {"foo.bar": {"$in": [2, 3]}} results in a match
 * {"foo.bar": {"$nin": [2, 3]}} results in a match
 * {"foo.bar": {"$not": {"$in": [2, 3]}}} results in no match
 *
 * Firstly, the "foo.bar" path selects both 1 and 2 from the mapping.
 *
 * 1 results in a match because the check (as with all of the criteria) is
 * implicitly OR'd across all selected values.  Also, non-Map value/criteria is
 * treated as a simple equality check.  So this is equivalent to
 * (1 === 1 || 2 === 1).
 *
 * $or and $in wound up being the same, but $or's mapped value is treated as an
 * array of arbitrary sub-criteria, whereas $in uses the array literally
 * (Array.includes() is used), so it is only suited to simple values.  $in may
 * also be more efficient, where applicable.
 *
 * $in and $nin both result in a match because the first looks for a value in
 * [2, 3] and the second looks for a value not in [2, 3], and a satisfying
 * value exists in both cases.  The $not $in case results in no match because
 * $not inverts result of the $in check.  As noted, the $in check results in
 * true, so the inverse is false.  This shows that using $not and inverting an
 * operator don't necessarily result in the same behavior.
 *
 * @param value Some value to check
 * @param criteria Some criteria to check for
 * @return true if value matches the criteria; false if not
 */
function mongoishMatchObject(value, criteria)
{
    let result = true;

    // Separate various types of criteria.
    let logicalCriteria = new Map();
    let valueCriteria = new Map();
    let propValueCriteria = new Map();

    if (criteria instanceof Map)
    {
        // Map criteria can check properties of a map value, and can also check
        // non-map values (in the latter case, the criteria keys must be
        // operators, e.g. "$lt").
        for (let [critKey, critValue] of criteria)
        {
            if (["$and", "$or", "$not"].includes(critKey))
                logicalCriteria.set(critKey, critValue);
            else if (valueOps.has(critKey))
                valueCriteria.set(critKey, critValue);
            else if (critKey.startsWith("$"))
                throw new InvalidMatchOperator(critKey);
            else
                // Key is a property path.
                propValueCriteria.set(critKey, critValue);
        }
    }
    else if (value instanceof Map)
        // Non-map criteria is not applicable to a map value.  Not sure what
        // the semantics would be... e.g. comparing a Map to 4.  What would
        // that mean?  Just treat as a non-match.
        result = false;
    else
        // A non-map criteria can be a check on a non-map value.  Just treat as
        // an equality check.
        valueCriteria.set("$eq", criteria);

    // Check logical criteria
    if (result)
    {
        for (let [logicalOp, subCriteria] of logicalCriteria)
        {
            if (logicalOp === "$or")
            {
                let orResult = false;
                for (let subCriterion of subCriteria)
                    if (mongoishMatchObject(value, subCriterion))
                    {
                        orResult = true;
                        break;
                    }

                result &&= orResult;
            }
            else if (logicalOp === "$and")
            {
                let andResult = true;
                for (let subCriterion of subCriteria)
                    if (!mongoishMatchObject(value, subCriterion))
                    {
                        andResult = false;
                        break;
                    }

                result &&= andResult;
            }
            else  // logicalOp === "$not"
                result &&= !mongoishMatchObject(value, subCriteria);

            if (!result)
                break;
        }
    }

    // Check value criteria
    if (result)
    {
        for (let [op, operand] of valueCriteria)
        {
            let opFunc = valueOps.get(op);
            result &&= opFunc(value, operand);

            if (!result)
                break;
        }
    }

    // Check property value criteria
    if (result)
    {
        for (let [propPath, criteria] of propValueCriteria)
        {
            if (value instanceof Map)
                result &&= mongoishMatchProperty(value, propPath, criteria);
            else
                // Kind of an n/a situation.  Criteria is given as if it was to
                // be used with a map (including property paths), but this
                // value is not a map!  Well it can't match, so just eval to
                // false.
                result = false;

            if (!result)
                break;
        }
    }

    return result;
}


/**
 * Perform a simple sanity check on a STIX object to determine whether it's
 * valid.
 *
 * @param stixObject The STIX object
 * @return true if the object is valid; false if not
 */
function isValidStixObject(stixObject)
{
    // assume we've gone through the normalization process such that we
    // can assume we have a Map object.  This is more about whether an object
    // has what we need, than whether we have an object in the first place.
    return stixObject.has("id") && stixObject.has("type");
}


/**
 * Sometimes we want to restrict attention to STIX types which are usable as
 * nodes in our graph.  (relationships are notably invalid for this.)
 *
 * @param stixType A STIX type
 * @return true if the type is usable as a node, false if not
 */
function isStixTypeValidForNode(stixType)
{
    return stixType !== "relationship";
}


/**
 * Sometimes we want to restrict attention to STIX types which are usable as
 * nodes in our graph.  (relationships are notably invalid for this.)
 * This function is useful for object references, which are STIX IDs.
 *
 * @param stixId A STIX ID
 * @return true if the type embedded within the ID is usable as a node, false
 *      if not
 */
function isStixIdValidForNode(stixId)
{
    // length of UUIDs is 36 chars, plus 2 for the "--"
    let typeLength = stixId.length - 38;
    let stixType = stixId.substring(0, typeLength);

    return isStixTypeValidForNode(stixType);
}


/**
 * Given a name, modify it to make it unique: add a "(n)" suffix depending
 * on the content of nameCounts.  nameCounts contains the number of times the
 * name was previously seen.  nameCounts is updated as necessary.
 *
 * @param baseName A computed name, which may not be unique
 * @param nameCounts Bookkeeping to support uniquefication, mapping previously
 *      seen base names to counts
 * @return A uniquefied name
 */
function uniquefyName(baseName, nameCounts)
{
    let uniqueName;
    let nameCount = nameCounts.get(baseName) || 0;

    ++nameCount;
    nameCounts.set(baseName, nameCount);

    if (nameCount === 1)
        uniqueName = baseName;
    else
        uniqueName = baseName + "(" + nameCount.toString() + ")";

    return uniqueName;
}


/**
 * Find a name for the given STIX object.  This will be the label users see
 * in the graph.  If a name has already been computed for the object, it is
 * returned.  Otherwise, a new name is computed and data structures updated
 * (stixIdToName and nameCounts).
 *
 * @param stixObject a STIX object
 * @param stixIdToName A mapping from IDs of STIX objects to previously
 *      computed names.
 * @param nameCounts A mapping from names to counts, used to uniquefy new names.
 * @param config A config object containing preferences for naming objects;
 *      null to use defaults
 * @return A name
 */
function nameForStixObject(stixObject, stixIdToName, nameCounts, config=null)
{
    let stixId = stixObject.get("id");
    let stixType = stixObject.get("type");

    let name = stixIdToName.get(stixId);
    if (!name)
    {
        let baseName;
        let userLabels;

        // Look for an ID-specific label; if that fails, look for a
        // type-specific label; if that fails, use some hard-coded fallbacks,
        // which eventually just default to using the STIX type.
        if (config)
        {
            userLabels = config.get("userLabels");
            if (userLabels)
                baseName = userLabels.get(stixId);

            if (!baseName)
            {
                let typeConfig = config.get(stixType);
                if (typeConfig)
                {
                    let labelPropName = typeConfig.get("displayProperty");
                    if (labelPropName)
                        baseName = stixObject.get(labelPropName);
                }
            }
        }

        // Copied from old visualizer, fall back to some hard-coded properties
        if (!baseName)
            baseName = stixObject.get("name");
        if (!baseName)
            baseName = stixObject.get("value");
        if (!baseName)
            baseName = stixObject.get("path");
        if (!baseName)
            baseName = stixType;

        // Copied from old visualizer: ensure the name isn't too long.
        if (baseName.length > 40)
          baseName = baseName.substr(0,40) + '...';

        name = uniquefyName(baseName, nameCounts);
        stixIdToName.set(stixId, name);
    }

    return name;
}


/**
 * Create a URL to an icon file for the given STIX type.  This does not check
 * whether the icon file actually exists.
 *
 * @param stixType the STIX type to get a URL for
 * @param iconPath A path to prepend to an icon filename.  The path is
 *      prepended as <path>/<filename>, i.e. it is separated from the filename
 *      with a forward slash.  If null/undefined, don't prepend a path.
 * @param iconFileName An icon file name.  If falsey, a default is constructed
 *      from the given STIX type.
 * @return A URL of an icon for the given STIX type
 */
function stixTypeToIconURL(stixType, iconPath, iconFileName)
{
    let iconUrl;

    if (!iconFileName)
        iconFileName = "stix2_"
            + stixType.replaceAll("-", "_")
            + "_icon_tiny_round_v1.png";

    if (iconPath === null || iconPath === undefined)
        iconUrl = iconFileName;
    else
        iconUrl = iconPath + "/" + iconFileName;

    return iconUrl;
}


/**
 * Create an object representing a visjs network edge.  Any changes to edge
 * config settings can be made here.
 *
 * @param sourceRef STIX ID of the source object
 * @param targetRef STIX ID of the dest object
 * @param label A label to be associated with the edge
 * @param stixId If this edge represents a relationship SRO, the STIX ID of
 *      the SRO.  If it represents another type of relationship (e.g. an
 *      embedded relationship), this can be null.
 * @return An edge object
 */
function makeEdgeObject(sourceRef, targetRef, label, stixId=null)
{
    let edge = {
        from: sourceRef,
        to: targetRef,
        label: label
    };

    if (stixId)
        edge.id = stixId;

    return edge;
}


/**
 * Create an object representing an visjs network node.  Any changes to node
 * config settings can be made here.
 *
 * @param name A node name; will be used to label the node in the graph
 * @param stixObject The STIX object.  Provided in case any info from it is
 *      needed for configuring the node
 * @return A node object
 */
function makeNodeObject(name, stixObject)
{
    let node = {
        id: stixObject.get("id"),
        label: name
    };

    return node;
}


/**
 * Create a fallback icon URL to use any time the usual STIX type based
 * icon file is not found.  (Implied: this default is the same, regardless of
 * STIX type.)  Of course, this fallback *should* be known to always exist!
 *
 * @param iconPath The user-configured setting for the icon directory, in case
 *      it is relevant for the fallback; null if one was not configured.
 * @return A URL to an icon
 */
function getDefaultIconURL(iconPath=null)
{
    let defaultURL = stixTypeToIconURL('custom_object', iconPath, null);
    defaultURL = defaultURL.replace('.png', '.svg');

    return defaultURL;
}


/**
 * Make a data structure which is suitable for an external entity to create a
 * legend.
 *
 * @param stixIdToObject A mapping from STIX IDs to Map instances containing
 *      all STIX objects
 * @param config Config data used for finding icons for legend entries; null
 *      to use default settings (a Map instance)
 * @return A [iconURLs, defaultIconURL] 2-tuple, where iconURLs is a Map
 *      instance which maps STIX type to a URL, and defaultIconURL is a
 *      fallback URL in case the URL in the mapping does not resolve.
 */
function makeLegendData(stixIdToObject, config=null)
{
    let iconPath = null;
    if (config)
        iconPath = config.get("iconDir");

    let defaultIconURL = getDefaultIconURL(iconPath);

    let stixTypes = new Set();

    // collect our types
    for (let object of stixIdToObject.values())
    {
        let stixType = object.get("type");
        if (isStixTypeValidForNode(stixType))
            stixTypes.add(stixType);
    }

    let iconURLs = new Map();
    for (let type of stixTypes)
    {
        // Choose an icon file according to config settings
        let iconFileName;

        if (config)
        {
            let typeConfig = config.get(type);
            if (typeConfig)
                iconFileName = typeConfig.get("displayIcon");
        }

        let iconURL = stixTypeToIconURL(type, iconPath, iconFileName);

        iconURLs.set(type, iconURL);
    }

    return [iconURLs, defaultIconURL];
}


/**
 * Config can be given as JSON or an object.  Normalize whatever we are given
 * to a Map.
 *
 * @param config configuration as given to this module
 * @return A configuration Map
 * @throw InvalidConfigError if the given config value is invalid
 */
function normalizeConfig(config)
{
    try
    {
        config = parseToMap(config)
    }
    catch(err)
    {
        throw new InvalidConfigError(null, {cause: err});
    }

    if (!(config instanceof Map))
        throw new InvalidConfigError();

    return config;
}


/**
 * STIX content input can take different forms.  This function normalizes it to
 * an array of objects, so subsequent code only deals with a single form.  Each
 * object is itself normalized to a Map instance (as are all sub-objects).
 *
 * This function also does some simple sanity checks on the input to try to
 * ensure it is valid.
 *
 * @param stixContent STIX content consisting of a single STIX object, array of
 *      objects, or bundle of objects, as a plain javascript object, array,
 *      Map instance, or JSON string.
 * @return An array of objects
 * @throw STIXContentError if any errors are found in the input
 */
function normalizeContent(stixContent)
{
    let stixObjects;

    try
    {
        stixContent = parseToMap(stixContent);
    }
    catch (err)
    {
        throw new STIXContentError(null, {cause: err});
    }

    if (stixContent instanceof Map && stixContent.size > 0)
    {
        if (stixContent.get("type") === "bundle")
            stixObjects = stixContent.get("objects") || [];
        else
            // Assume we were given a single object
            stixObjects = [stixContent];
    }
    else if (Array.isArray(stixContent))
        stixObjects = stixContent;
    else
        throw new STIXContentError();

    if (!Array.isArray(stixObjects) || stixObjects.length <= 0)
        throw new STIXContentError();

    // Do a simple validity check on our individual STIX objects.
    for (let stixObject of stixObjects)
        if (!isValidStixObject(stixObject))
            throw new InvalidSTIXObjectError(stixObject);

    return stixObjects;
}


/**
 * Abstract base class for views of STIX-derived graph data.
 */
class STIXContentView
{
    #legendData;

    constructor(stixIdToObject, config=null)
    {
        this.#legendData = makeLegendData(stixIdToObject, config);
    }

    /**
     * Get a data structure which is suitable for an external entity to create
     * a legend.
     *
     * @return A [iconURLs, defaultIconURL] 2-tuple, where iconURLs is a Map
     *      instance which maps STIX type to a URL, and defaultIconURL is a
     *      fallback URL in case the URL in the mapping does not resolve.
     */
    get legendData()
    {
        return this.#legendData;
    }

    /**
     * Add an event listener to the view.  Events/semantics depends on the
     * view.
     */
    on(...args)
    {
    }

    /**
     * Dispose of the view to free up resources.
     */
    destroy()
    {
    }

    /**
     * Toggle display of view elements of a particular STIX type.
     *
     * @param stixType the STIX type whose nodes should be toggled
     */
    toggleStixType(stixType)
    {
    }

    /**
     * Set the selection to the view element corresponding to the given STIX
     * ID.
     *
     * @param stixId the STIX ID of the node to select
     */
    selectNode(stixId)
    {
    }
}


/**
 * A view of STIX-derived graph data which is a simple textual list.
 */
class ListView extends STIXContentView
{
    #containerRoot;
    #contentRoot;
    #stixIdToObject;
    #selectedId;

    /**
     * Initialize a list view.
     *
     * @param domElement the parent element where the graph is to be located in
     *      a web page
     * @param nodeDataSet A visjs DataSet instance with graph node data derived
     *      from STIX content
     * @param edgeDataSet A visjs DataSet instance with graph edge data derived
     *      from STIX content
     * @param stixIdToObject A Map instance mapping STIX IDs to STIX objects as
     *      Maps, containing STIX content.
     * @param config A config object
     */
    constructor(
        domElement, nodeDataSet, edgeDataSet, stixIdToObject, config=null
    )
    {
        if (config !== null)
            config = normalizeConfig(config);

        super(stixIdToObject, config);

        this.#containerRoot = domElement;
        this.#stixIdToObject = stixIdToObject;

        let doc = domElement.ownerDocument;
        let ol = doc.createElement("ol");

        nodeDataSet.forEach((item, id) => {
            let stixObject = stixIdToObject.get(id);
            let itemText = stixObject.get("type") + ": " + item.label;

            let li = doc.createElement("li");
            li.id = id;
            li.className = "list-view-item";
            ol.append(li);
            li.append(itemText);
        });

        edgeDataSet.forEach((item, id) => {
            let fromItem = nodeDataSet.get(item.from);
            let toItem = nodeDataSet.get(item.to);

            let itemText = fromItem.label
                + " " + item.label
                + " " + toItem.label;

            if (!stixIdToObject.has(id))
                itemText += " (embedded)";

            let li = doc.createElement("li");
            li.id = id;
            li.className = "list-view-item";
            ol.append(li);
            li.append(itemText);
        });

        this.#contentRoot = ol;
        this.#containerRoot.append(ol);

        this.#selectedId = null;
    }

    /**
     * Adds a plain HTML event listener to the content root element of this
     * view.
     */
    on(...args)
    {
        this.#contentRoot.addEventListener(...args);
    }

    /**
     * Remove all the DOM nodes associated with this view.
     */
    destroy()
    {
        this.#containerRoot.replaceChildren();
    }

    /**
     * Toggle visibility of list items corresponding to STIX objects of the
     * given type.
     *
     * @param stixType the STIX type whose items should be toggled
     */
    toggleStixType(stixType)
    {
        let listItems = this.#contentRoot.getElementsByTagName("li");

        for (let idx=0; idx < listItems.length; ++idx)
        {
            let li = listItems[idx];
            let stixObject = this.#stixIdToObject.get(li.id);

            if (stixObject && stixObject.get("type") === stixType)
                li.classList.toggle("hidden");
        }
    }

    /**
     * Set the graph selection to the node corresponding to the given STIX ID.
     *
     * @param stixId the STIX ID of the node to select
     */
    selectNode(stixId)
    {
        let doc = this.#contentRoot.ownerDocument;

        // de-select the previous item, if any
        if (this.#selectedId)
        {
            let oldLi = doc.getElementById(this.#selectedId);
            if (oldLi)
                oldLi.classList.remove("list-view-selected");
        }

        let li = doc.getElementById(stixId);
        if (li)
        {
            li.classList.add("list-view-selected");
            this.#selectedId = stixId;
            li.scrollIntoView({block: "nearest"});
        }
    }
}


/**
 * A view of STIX-derived graph data which is a visjs graph.
 */
class GraphView extends STIXContentView
{
    #nodeDataSet;
    #edgeDataSet;
    #network;

    /**
     * Initialize a graph view.
     *
     * @param visjs The visjs-network module
     * @param domElement the parent element where the graph is to be located in
     *      a web page
     * @param nodeDataSet A visjs DataSet instance with graph node data derived
     *      from STIX content
     * @param edgeDataSet A visjs DataSet instance with graph edge data derived
     *      from STIX content
     * @param stixIdToObject A Map instance mapping STIX IDs to STIX objects as
     *      Maps, containing STIX content.
     * @param config A config object
     */
     constructor(
        visjs, domElement, nodeDataSet, edgeDataSet, stixIdToObject,
        config=null
    )
    {
        if (config !== null)
            config = normalizeConfig(config);

        super(stixIdToObject, config);

        this.#edgeDataSet = edgeDataSet;

        // Add some node data specific to this view, which enables the icons.
        // This constructs a new dataset from the old one, to avoid modifying
        // the original.
        this.#nodeDataSet = new visjs.DataSet();

        nodeDataSet.forEach((item, id) => {
            this.#nodeDataSet.add({
                ...item,
                group: stixIdToObject.get(id).get("type")
            });
        });

        let groups = this.#makeGroups();

        let graphData = {
            nodes: this.#nodeDataSet,
            edges: this.#edgeDataSet
        };

        let graphOpts = {
            groups: groups,
            nodes: {
                color: {
                    border: "black"
                },
                font: {
                    size: 20
                },
                borderWidth: 2,
                chosen: {
                    // Enable a drop shadow when a node is selected
                    node: (values, id, selected, hovering) => {
                        if (selected)
                        {
                            values.shadow = true;
                            values.shadowX = values.shadowY = 8;
                            values.borderWidth = 4;
                        }
                    }
                }
            },
            edges: {
                arrows: "to",
                width: 3,
                color: "gray",
                font: {
                    size: 20
                }
            },
            physics: {
                solver: "barnesHut",
                barnesHut: {
                    theta: 0.9,
                    gravitationalConstant: -3000,
                    centralGravity: 0,
                    springConstant: 0.01,
                    springLength: 400
                },
                minVelocity: 1,
                // Set to false if you want to watch the graph stabilize when
                // it first loads.
                stabilization: true
            }
        };

        this.#network = new visjs.Network(domElement, graphData, graphOpts);
    }

    /**
     * Get the underlying visjs Network object.  Might be useful in case one
     * wants to perform operations specific to the library.
     */
    get graph()
    {
        return this.#network;
    }

    /**
     * Get the visjs DataSet object containing graph node data.  Useful to
     * affect changes in the graph.
     */
    get nodeDataSet()
    {
        return this.#nodeDataSet;
    }

    /**
     * Get the visjs DataSet object containing graph edge data.  Useful to
     * affect changes in the graph.
     */
    get edgeDataSet()
    {
        return this.#edgeDataSet;
    }

    /**
     * Convenience event handling method which passes through to the underlying
     * graph method.
     */
    on(...args)
    {
        this.graph.on(...args);
    }

    /**
     * Dispose of the graph to free up resources.
     */
    destroy()
    {
        this.graph.destroy();
    }

    /**
     * Create a visjs network groups structure.  There will be one group per
     * STIX type present in the data (except "relationship").
     */
    #makeGroups()
    {
        let [iconURLs, defaultIconURL] = this.legendData;

        let groups = {};
        for (let [stixType, iconURL] of iconURLs)
        {
            groups[stixType] = {
                shape: "circularImage",
                image: iconURL,
                brokenImage: defaultIconURL
            };
        }

        return groups;
    }

    /**
     * Toggle the display of graph nodes of a particular STIX type.
     *
     * @param stixType the STIX type whose nodes should be toggled
     */
    toggleStixType(stixType)
    {
        let nodes = this.nodeDataSet.get({
            filter: item => item.group === stixType,
            fields: ["id", "hidden"]
        });

        if (nodes.length === 0)
            return;

        this.enablePhysics();

        // Whether we are hiding or showing nodes of the selected type.
        // If first node is currently hidden, we must be showing, and vice
        // versa.
        let hiding = !nodes[0].hidden;

        let toggledNodes = [];
        let toggledEdges = [];

        // An edge could connect two nodes of the same type.  Ensure we don't
        // toggle an edge more than once!
        let toggledEdgeIds = new Set();

        for (let node of nodes)
        {
            // Toggling the node is simple
            toggledNodes.push({
                id: node.id, hidden: hiding, physics: !hiding
            });

            // Toggling the edges is more complex...
            let edgesForNode = this.edgeDataSet.get({
                // find (a) edges connecting to 'node'; (b) edges with the
                // right visibility; (c) edges we have not already seen.
                filter: item => (item.from === node.id || item.to === node.id)
                    && !item.hidden === hiding && !toggledEdgeIds.has(item.id),
                fields: ["id", "from", "to"]
            });

            if (hiding)
            {
                // simple case: unconditionally hide everything
                for (let edge of edgesForNode)
                {
                    toggledEdges.push({
                        id: edge.id, hidden: true, physics: false
                    });
                    toggledEdgeIds.add(edge.id);
                }
            }
            else
            {
                // showing is a more complex case: gotta check the other ends
                // of the edges.  Only show if the other end is also visible
                // or of the selected type (meaning it will become visible).
                for (let edge of edgesForNode)
                {
                    let otherEndId;
                    if (edge.from === node.id)
                        otherEndId = edge.to;
                    else
                        otherEndId = edge.from;

                    let otherEndNode = this.nodeDataSet.get(
                        otherEndId,
                        {fields: ["group", "hidden"]}
                    );

                    if (!otherEndNode.hidden
                        || otherEndNode.group === stixType)
                    {
                        toggledEdges.push({
                            id: edge.id, hidden: false, physics: true
                        });
                        toggledEdgeIds.add(edge.id);
                    }
                }
            }
        }

        this.nodeDataSet.updateOnly(toggledNodes);
        this.edgeDataSet.updateOnly(toggledEdges);
    }

    /**
     * Set the graph selection to the node corresponding to the given STIX ID.
     */
    selectNode(stixId)
    {
        this.graph.selectNodes([stixId]);
    }

    /**
     * Enable physics in this graph view
     */
    enablePhysics()
    {
        this.#network.setOptions( { physics: true } );
    }

    /**
     * Disable physics in this graph view
     */
    disablePhysics()
    {
        this.#network.setOptions( { physics: false } );
    }
}


/**
 * Create a network edge object from the given STIX relationship object, if
 * possible.  If source or target_ref refers to an unknown object, the edge
 * can't be created and null is returned.
 *
 * @param stixRel a STIX relationship object
 * @param stixIdToObject A Map instance mapping STIX IDs to STIX objects as
 *      Maps, containing STIX content.
 * @return An visjs network edge object, or null if one could not be created
 */
function edgeForRelationship(stixRel, stixIdToObject)
{
    let sourceRef = stixRel.get("source_ref");
    let targetRef = stixRel.get("target_ref");
    let relType = stixRel.get("relationship_type");

    let edge = null;
    if (stixIdToObject.has(sourceRef) && stixIdToObject.has(targetRef))
    {
        // check STIX types just in case
        if (isStixIdValidForNode(sourceRef) && isStixIdValidForNode(targetRef))
            edge = makeEdgeObject(
                sourceRef, targetRef, relType, stixRel.get("id")
            );
    }
    else
        console.warn(
            "Skipped relationship %s %s %s: missing endpoint object(s)",
            sourceRef, relType, targetRef
        );

    return edge;
}


/**
 * Generate values from stixValue according to the given path.
 *
 * A property path is a string in a dot-delimited syntax: property names
 * concatenated with dots in between.  This syntax is used to locate values
 * within a JSON-like structure which is a composition of Maps and arrays.
 * In this syntax, array properties are not indexed.  All array elements are
 * automatically searched.  If the last path element is array-valued, its
 * elements are individually generated, you don't get the whole array at once.
 * Because arrays are transparently searched, a property path does not
 * necessarily identify a unique location in a structure.
 *
 * Property paths shouldn't begin or end with a dot, there should be no
 * adjacent dots, and the path should not be empty.  Property names can't
 * contain dots; there is no escaping.  But this should be okay since STIX
 * property names should not contain dots.
 *
 * For example, given structure:
 *     {
 *         "a": [
 *             {"b": 1},
 *             {
 *                 "b": {
 *                     "c": [2, 3]
 *                 }
 *             }
 *         ]
 *     }
 *
 * Paths and results include:
 *     "a" -> {"b": 1}, {"b": {"c": [2, 3]}}  (two results)
 *     "a.b" -> 1, {"c": [2, 3]} (two results)
 *     "a.b.c" -> 2, 3 (two results)
 *     "a.b.c.d" -> (no results)
 *
 * @param stixValue The value to search, as a Map or an array
 * @param propPath The path to follow
 * @param index The index of one of the dots in propPath, or -1.  This keeps
 *      track of which path component we're on through recursive calls.  The
 *      path component extends from the character after "index" to the next
 *      occurrence of ".", or to the end of the string.  If -1, the current
 *      path component is the first one.  The initial call should let this
 *      parameter default to -1.
 */
function* getValuesAtPath(stixValue, propPath, index=-1)
{
    if (Array.isArray(stixValue))
    {
        // pass-through array elements
        for (let elt of stixValue)
            yield* getValuesAtPath(elt, propPath, index);
    }

    else if (stixValue instanceof Map)
    {
        let nextDotIdx = propPath.indexOf(".", index+1);
        let pathStep;

        if (nextDotIdx === -1)
            pathStep = propPath.substring(index+1);
        else
            pathStep = propPath.substring(index+1, nextDotIdx);

        if (pathStep.length > 0)
        {
            if (stixValue.has(pathStep))
            {
                let propValue = stixValue.get(pathStep);

                if (nextDotIdx === -1)
                {
                    // End of path; just yield whatever we have
                    if (Array.isArray(propValue))
                        yield* propValue;
                    else
                        yield propValue;
                }
                else
                    yield* getValuesAtPath(propValue, propPath, nextDotIdx);
            }
        }
        else if (nextDotIdx !== -1)
            // Ignore empty path steps, e.g. two adjacent dots.
            yield* getValuesAtPath(stixValue, propPath, nextDotIdx);
    }
}


/**
 * Search a STIX object according to embedded relationship information
 * based on property paths, and create graph edge structures.
 *
 * @param stixObject The STIX object to search
 * @param stixIdToObject A Map instance mapping STIX IDs to STIX objects as
 *      Maps, containing STIX content.
 * @param relInfo An array of [<property path>, <edge label>, <direction>]
 *      triples which describes what to search for within the object and how
 *      to create the edges.
 * @return An array of edge objects
 */
function edgesFromPropertyPaths(stixObject, stixIdToObject, relInfo)
{
    let sourceId = stixObject.get("id");
    let edges = [];

    for (let [propPath, edgeLabel, forward] of relInfo)
    {
        for (let ref of getValuesAtPath(stixObject, propPath))
        {
            if (isStixIdValidForNode(ref))
            {
                if (stixIdToObject.has(ref))
                {
                    let edgeSrc, edgeDst;

                    // "forward" edge direction is referrer->referent
                    // "backward" is referent->referrer
                    if (forward)
                        [edgeSrc, edgeDst] = [sourceId, ref];
                    else
                        [edgeSrc, edgeDst] = [ref, sourceId];

                    let edge = makeEdgeObject(edgeSrc, edgeDst, edgeLabel);

                    edges.push(edge);
                }
                else
                    console.warn(
                        "Skipped embedded relationship %s %s %s: target object"
                        + " missing",
                        sourceId, propPath, ref
                    );
            }
        }
    }

    return edges;
}


/**
 * Create visjs network edges for embedded relationships within the given
 * object.
 *
 * @param stixObject a STIX object
 * @param stixIdToObject A Map instance mapping STIX IDs to STIX objects as
 *      Maps, containing STIX content.
 * @param config A config object containing user preferences regarding
 *      embedded relationships
 * @return An array of edge objects
 */
function edgesForEmbeddedRelationships(stixObject, stixIdToObject, config=null)
{
    let stixType = stixObject.get("type");

    let typeAgnosticRels = embeddedRelationships.get(null);
    let typeSpecificRels = embeddedRelationships.get(stixType);

    let userTypeAgnosticRels = null;
    let userTypeSpecificRels = null;

    if (config)
    {
        // Can't have null keys in JSON or javascript (plain objects), so use
        // an empty string.  Put type-agnostic config there.
        if (config.has(""))
        {
            let typeConfig = config.get("");
            if (typeConfig.has("embeddedRelationships"))
                userTypeAgnosticRels = typeConfig.get("embeddedRelationships");
        }

        if (config.has(stixType))
        {
            let typeConfig = config.get(stixType);
            if (typeConfig.has("embeddedRelationships"))
                userTypeSpecificRels = typeConfig.get("embeddedRelationships");
        }
    }

    let allRels = [];

    if (typeAgnosticRels)
        allRels.push(...typeAgnosticRels);

    if (typeSpecificRels)
        allRels.push(...typeSpecificRels);

    if (userTypeAgnosticRels)
        allRels.push(...userTypeAgnosticRels);

    if (userTypeSpecificRels)
        allRels.push(...userTypeSpecificRels);

    let edges = edgesFromPropertyPaths(stixObject, stixIdToObject, allRels);

    return edges;
}


/**
 * Make node and edge datasets derived from STIX content, representing a graph.
 *
 * @param stixIdToObject A Map instance mapping STIX IDs to STIX objects as
 *      Maps, containing STIX content.
 * @param config A config object containing preferences for naming graph
 *      elements and creating additional edges from embedded relationships;
 *      null to use defaults
 * @return 2-tuple consisting of an array of nodes and array of edges.
 */
function makeNodesAndEdges(stixIdToObject, config=null)
{
    // List of graph nodes, where each list element is whatever visjs needs
    // to represent the node.  This is a plain javascript object with an
    // "id" property at least, to identify the node.
    let nodes = [];

    // List of links/edges for the graph, where each list element is whatever
    // visjs needs to represent the edge.  This is a plain javascript object
    // with "from" and "to" properties at least, whose values are the IDs of
    // the linked nodes.
    let edges = [];

    // Used to uniquefy names.  E.g. first "foo" gets the name, then others
    // will be "foo(2)", "foo(3)", etc.  This map keeps track of those counts.
    // Maps the "base" name as computed for the STIX object, to a count.
    let nameCounts = new Map();

    // Map STIX IDs to the node names we use in the graph.
    let stixIdToName = new Map();

    for (let object of stixIdToObject.values())
    {
        let stixType = object.get("type");

        if (stixType === "relationship")
        {
            let edge = edgeForRelationship(object, stixIdToObject);

            if (edge)
                edges.push(edge);
        }
        // check STIX type for suitability just in case
        else if (isStixTypeValidForNode(stixType))
        {
            let name = nameForStixObject(
                object, stixIdToName, nameCounts, config
            );
            let node = makeNodeObject(name, object);
            nodes.push(node);

            let embeddedRelEdges = edgesForEmbeddedRelationships(
                object, stixIdToObject, config
            );

            // Seems like there ought to be a better way to extend one array
            // with the contents of another.
            edges.push(...embeddedRelEdges);
        }
    }

    return [nodes, edges];
}


/**
 * Handler for when graph stabilizes: disable physics so that dragging a node
 * only moves that node and all others stay where they are.
 *
 * @param event a visjs-network event object with the number of iterations it
 * took to stabilize the graph
 * @param view the visjs Graphview instance
 */
function stabilizedHandler(event, view)
{
    view.disablePhysics();
}


/**
 * Filter STIX objects according to criteria in the given config.  The config
 * must be a Map; if it contains "include" and/or "exclude" keys, the
 * corresponding value is criteria used to filter the objects.  "include"
 * causes matching objects to be included and the rest excluded; "exclude"
 * causes matching objects to be excluded and the rest included.  Both keys can
 * be present and both types of filtering will happen.
 *
 * See mongoishMatchObject() for information on criteria.
 *
 * @param stixObjects an array of STIX objects (as Maps)
 * @param config Configuration data, as a Map
 * @return An array containing STIX objects which passed the filters
 */
function filterStixObjects(stixObjects, config)
{
    if (config.has("include"))
    {
        let filterCriteria = config.get("include");
        stixObjects = stixObjects.filter(
            obj => mongoishMatchObject(obj, filterCriteria)
        );
    }

    if (config.has("exclude"))
    {
        let filterCriteria = config.get("exclude");
        stixObjects = stixObjects.filter(
            obj => !mongoishMatchObject(obj, filterCriteria)
        );
    }

    return stixObjects;
}


/**
 * Make graph data from the given STIX content.
 *
 * @param visjs the visjs module
 * @param stixContent STIX content as a STIX object, array of objects, or
 *      bundle of objects, or any of those as JSON
 * @param config Config settings as a Map or object, or as JSON
 * @return A 3-tuple include the node DataSet, edge DataSet, and normalized
 *      STIX content as a Map instance from STIX ID to a Map instance
 *      containing a STIX object.
 */
function makeGraphData(visjs, stixContent, config=null)
{
    if (config !== null)
        config = normalizeConfig(config);

    let stixObjects = normalizeContent(stixContent);
    stixObjects = filterStixObjects(stixObjects, config);

    let stixIdToObject = new Map();

    for (let object of stixObjects)
        stixIdToObject.set(object.get("id"), object);

    let [nodes, edges] = makeNodesAndEdges(stixIdToObject, config);

    let nodeDataSet = new visjs.DataSet(nodes);
    let edgeDataSet = new visjs.DataSet(edges);

    return [nodeDataSet, edgeDataSet, stixIdToObject];
}


/**
 * Create a graph view of the given data.  The content will be added to the
 * webpage DOM under the given element.
 *
 * @param visjs The visjs-network module
 * @param domElement the parent element where the graph is to be located in a
 *      web page
 * @param nodeDataSet A visjs DataSet instance with graph node data derived
 *      from STIX content
 * @param edgeDataSet A visjs DataSet instance with graph edge data derived
 *      from STIX content
 * @param stixIdToObject A Map instance mapping STIX IDs to STIX objects as
 *      Maps, containing STIX content.  Graph data can be looked up here, to
 *      obtain full details about the STIX objects.
 * @param config A config object.  Relevant preferences include those for
 *      customizing iconography.
 * @return The graph view object.  May be used perform certain actions on the
 *      view, e.g. dispose of it.
 */
function makeGraphView(
    visjs, domElement, nodeDataSet, edgeDataSet, stixIdToObject, config=null
)
{
    let view = new GraphView(
        visjs, domElement, nodeDataSet, edgeDataSet, stixIdToObject, config
    );

    // Add some handlers to enable some hard-coded behavior.
    view.on("stabilized", e => stabilizedHandler(e, view));

    return view;
}


/**
 * Create and return an object which is this file's module.
 */
function makeModule(visjs)
{
    let module = {
        makeGraphData: (stixContent, config=null) =>
            makeGraphData(visjs, stixContent, config),
        makeGraphView: (...args) => makeGraphView(visjs, ...args),
        makeListView: (...args) => new ListView(...args)
    };

    return module;
}


define(["nbextensions/stix2viz/vis-network"], makeModule);
