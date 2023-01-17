import yaml
import re
import os
from collections import namedtuple

f = open('config.yml')
config = yaml.safe_load(f)

# ==============================================================================
# GENERAL HELPERS
# ==============================================================================

def regex_match_single(pattern, lines, goal = None):
    """Does re.search function on 'lines' with 'pattern', if not found, throw exception with 'goal' if goal is specified. It returns the FIRST matched group
    """
    p = re.compile(pattern)
    result = p.search(lines)
    if not result and goal is not None:
        except_msg = "Regex could not match {}\n".format(goal)
        raise Exception(except_msg)

    if not result and goal is None:
        return None

    return result.group(1)

def regex_match_all(pattern, lines, goal = None):
    """Does re.findall function on 'lines' with 'pattern', if not found, throw exception with 'goal' if goal is specified. It returns all matched groups
    """
    p = re.compile(pattern)
    result = p.findall(lines)
    if not result and goal is not None:
        except_msg = "Regex could not match {}\n".format(goal)
        raise Exception(except_msg)

    if not result and goal is None:
        return None

    return result

def index_of(val, in_list):
    try:
        return in_list.index(val)
    except ValueError:
        return None 

def convert_to_attack_link(id):
    """ Converts an ID like T1059.004 into the attack Url https://attack.mitre.org/techniques/T1059/004/
    """
    id = id.replace('.', '/')
    return config['attackLink'] + id


# ==============================================================================
# MBC DIRECTORY TRAVERSAL
# ==============================================================================
def traverse_dir():
    """Traverses MBC directory (path defined in config file), ignoring files/folders in ignore list (defined in config file)
    """
    file_list = []

    for root, dirs, files in os.walk(config["MBCdir"]["MBCPath"]):
        if not any(block in root for block in config["MBCdir"]["ignorelist"]):
            for name in files:
                file_list.append(os.path.join(root, name))

    return file_list


def match_name_with_path(name, rel_path_base = None):
    """Given a string such as "Data::Decompress Data::aPLib", return path to corresponding file. Handles micro-objectives. If rel_path_base is specified, it will return the relative path with respect to rel_path_base
    """

    file_list = traverse_dir()

    # Splits name by '::', and then tries to match either the last or second to last section 
    split_name = name.lower().replace('/ ', '').replace('-', '').replace(' ', '-').split('::')

    for file in file_list:
        file_suffix = file.split('/')[-1].replace('.md', '')
        if split_name[-1] == file_suffix or split_name[-2] == file_suffix:
            if rel_path_base:
                return os.path.relpath(file, rel_path_base)

            return file

    raise Exception("No file path matched for '{}'".format(name))


# ==============================================================================
# BEHAVIOR HELPERS
# ==============================================================================
MalwareLink = namedtuple('MalwareLink', ['Name', 'Link', 'Year', 'ID', 'Description']) # Example: ['Rombertik', '../xample-malware/rombertik.md', '2015', [T1056.001],  ['desc', '<url>']]


def analyze_behavior_file_section_line_nums(file_list):
    """Parses read behavior file and returns the line numbers of each section in a dict
    
    Args:
        Behavior file in the form of a LIST (using .readlines() or .read() w/ .split())
    Returns:
        {
            Title: {}
            Method: {}
            Malware: {}
            Snippet: {}
            Detection: {}
            References: {}
        }
    """
    # Title needs special regex matching syntax bc it is not constant
    for line in file_list:
        title_match = regex_match_single(config['Behavior']['TitleRegex'], line)
        if title_match is not None:
            title = title_match
            title_line = file_list.index(line)
    if title is None:
        raise Exception('Title not found')

    method_line = index_of(config['Behavior']['MethodRegex'], file_list)
    malware_line = index_of(config['Behavior']['MalwareRegex'], file_list)
    snippet_line = index_of(config['Behavior']['SnippetRegex'], file_list)
    detection_line = index_of(config['Behavior']['DetectionRegex'], file_list)
    ref_line = index_of(config['Behavior']['ReferencesRegex'], file_list)

    if malware_line is None:
        malware_line = len(file_list) - 1
    if ref_line is None:
        ref_line = len(file_list) - 1

    return {
        title: title_line,
        'Method': method_line,
        'Malware': malware_line,
        'Snippet': snippet_line,
        'Detection': detection_line,
        'References': ref_line
    }

def analyze_behavior_file_malware_section(file_list, line_num_dict = None, reference_list = None):
    """Parses read behavior file and returns the mappings to the corpus in the 'Use in Malware' section

    Args:
        - Behavior file in the form of a LIST (using .readlines() or .read() w/ .split())
        - Optional: Dict of sectional line numbers (created by analyze_behavior_file_section_line_nums())
        - Optional: List of reference links (created by analyze_behavior_file_references())
    Returns:
        [(MalwareLink 1), (MalwareLink 2)]
    """
    malware_list = []

    if line_num_dict is None:
        line_num_dict = analyze_behavior_file_section_line_nums(file_list)
    if reference_list is None:
        reference_list = analyze_behavior_file_references(file_list, line_num_dict)

    if line_num_dict['Malware'] == len(file_list) - 1: # Checking if malware section does not exist
        return []
    
    if line_num_dict['Detection']:
        malware_section = file_list[line_num_dict['Malware']:line_num_dict['Detection']-1]
    elif line_num_dict['Snippet']:
        malware_section = file_list[line_num_dict['Malware']:line_num_dict['Snippet']-1]
    else:
        malware_section = file_list[line_num_dict['Malware']:line_num_dict['References']-1]

    if index_of(config['Behavior']['UseinMalwareTableStr2'],malware_section) is None:
        print(file_list)
        raise Exception

    malware_section = malware_section[index_of(config['Behavior']['UseinMalwareTableStr2'],malware_section)+1:] # Getting rid of lines up to and including '|---|---|---|---|'

    for malware in malware_section:
        if malware != '':
            result = regex_match_all(config['Behavior']['UseinMalwareRegex'], malware)
            if result is None: # There are some instances where there is malware that aren't in the corpus (see smokeloader in dynamic analysis evasion)
                result = regex_match_all(config['Behavior']['UseinMalwareRegex2'], malware, "the following malware mapping: {}".format(malware))
                result = list(result[0])
                result.insert(1, None)
            else:
                result = result[0]
            descript_match = regex_match_all(config['Malware']['DescRegex'], result[4], "description section of {}".format(result[4]))

            # Convert ref numbers to links
            for i, x in enumerate(descript_match):
                x = list(x)
                x[1] = reference_list[int(x[1])-1]
                descript_match[i] = x

            malware_list.append(MalwareLink(result[0], result[1], result[2], result[3], descript_match))

    return malware_list

def analyze_behavior_file_references(file_list, line_num_dict = None):
    """Parses read behavior file and returns the References links of the behavior in a list

    This function assumes that the references section is the last section of a behavior file and that the ref IDs start at 1 and increment in order
    
    Args:
        - Behavior file in the form of a LIST (using .readlines() or .read() w/ .split())
        - Optional: Dict of sectional line numbers (created by analyze_behavior_file_section_line_nums())
    Returns:
        [<link>, <link>, ]
    """
    return_list = []

    if line_num_dict is None:
        line_num_dict = analyze_behavior_file_section_line_nums(file_list)

    # Splits malware file into just Reference section
    ref_lines = file_list[int(line_num_dict['References'])+1:]
    
    for line in ref_lines:
        if line != '':
            link = regex_match_single(config['Malware']['ReferenceRegex'], line, "Reference Link {}".format(line))
            return_list.append(link)


    return return_list

def analyze_behavior_file_all(file):
    """Parses an entire behavior file, and returns all metadata in the form of a dict:

    Args: 
        Behavior file in the form of ONE string (using .read())
    Returns: 
        {
            "Title": 
            "Line Nums": {}
            "MalLinks": []
            "References": []
        }
    """

    return_dict = {
        "Line Nums": {},
        "MalLinks": [],
        "References": []
    }

    file_list = file.split('\n')

    return_dict["Line Nums"] = analyze_behavior_file_section_line_nums(file_list)
    return_dict["Title"]  = list(return_dict["Line Nums"].keys())[0]
    return_dict["References"] = analyze_behavior_file_references(file_list, return_dict["Line Nums"])
    return_dict["MalLinks"] = analyze_behavior_file_malware_section(file_list, return_dict["Line Nums"], return_dict["References"])

    return return_dict

def create_behavior_page(new_dict, path):
    """Writes file specified by path
    
    Args: 
        - Dict of behavior file with changes
        - Path to behavior file
    Returns: 
        - None
    """

    ##########
    # WIP: Only handles changes to 'Use in Malware' and 'References' section right now
    ##########
    f = open(path, 'r')
    behavior_file_lines = f.read()
    f.close()
    behavior_file_lines = behavior_file_lines.split('\n')

    line_num_dict = analyze_behavior_file_section_line_nums(behavior_file_lines)
    
    # Build new 'Use in Malware' Section
    malware_lines = []

    if line_num_dict['Malware'] == len(behavior_file_lines) - 1:
        malware_lines.append('')

    malware_lines.append(config['Behavior']['MalwareRegex'])
    malware_lines.append('')
    malware_lines.append(config['Behavior']['UseinMalwareTableStr1'])
    malware_lines.append(config['Behavior']['UseinMalwareTableStr2']) 
    
    for mal in new_dict['MalLinks']:
        desc = ""
        for d in mal.Description:
            refnum = new_dict['References'].index(d[1]) + 1
            desc = desc + config['Behavior']['UseinMalwareDescStr'].format(d[0], refnum, refnum)
            desc = desc[0].upper() + desc[1:-1]
        
        if mal.Link is None:
            malware_lines.append(config['Behavior']['UseinMalwareStr2'].format(mal.Name, mal.Year, mal.ID, desc))
        else:
            malware_lines.append(config['Behavior']['UseinMalwareStr'].format(mal.Name, mal.Link, mal.Year, mal.ID, desc))
    
    malware_lines.append('')

    if line_num_dict['Snippet']:
        behavior_file_lines[line_num_dict['Malware']:line_num_dict['Snippet']] = malware_lines
    else:
        behavior_file_lines[line_num_dict['Malware']:line_num_dict['References']] = malware_lines

    line_num_dict = analyze_behavior_file_section_line_nums([item.strip() for item in behavior_file_lines])

    # Build new 'References' Section
    reference_lines = []

    if line_num_dict['References'] == len(behavior_file_lines) - 1:
        malware_lines.append('')

    reference_lines.append(config['Behavior']['ReferencesRegex'])
    reference_lines.append('')
    counter = 1
    for link in new_dict['References']:
        reference_lines.append(config['Malware']['ReferenceStr'].format(counter, counter, link) + "\n")
        counter += 1

    behavior_file_lines[line_num_dict['References']:] = reference_lines


    # write to file
    with open(path, 'w') as f:
        f.writelines(s + '\n' for s in behavior_file_lines)

    f.close()

    return


def insert_malware_in_behavior(newMalware, behavior_file_link):
    """ Parses behavior file's 'Use in Malware' section, and then inserts the newMalware into the list. If the malware is already present, add the behavior ID to the methods column, and change the description to 'Please see [MalwareNameLink] for details. Overwrites file with new content'
    
    Args:
        - MalwareLink Object
        - link to BEHAVIOR file
    """
    f = open(behavior_file_link, 'r')
    behavior_file_lines = f.read()
    f.close()

    # Analyze behavior file
    behavior_dict = analyze_behavior_file_all(behavior_file_lines)

    # identify if the incoming description link is present in references. If not, insert into references list
    for i, d in enumerate(newMalware.Description):
        if d[1] not in behavior_dict['References']:
            behavior_dict['References'].append(d[1])
        
        newMalware.Description[i] = d

    found = False

    # if behavior_dict['Title'] == 'C2 Communication':
    #     print(behavior_dict["MalLinks"])

    for i, malware in enumerate(behavior_dict['MalLinks']):
        # Determine if behavior already in behavior_dict by comparing the name
        # If the method column contains '--', update with correct ID
        # If the new ID is not in the method field (which means that the malware contains mappings to multiple methods of the same behavior), replace the description with 'Please see <link> for details.' When doing this, new reference links will be removed from the references list
        if malware.Name == newMalware.Name:
            if '--' in malware.ID:
                malware = malware._replace(ID = newMalware.ID)
                behavior_dict["MalLinks"][i] = malware
            elif newMalware.ID not in malware.ID:
                malware = malware._replace(ID = malware.ID + ', ' + newMalware.ID, Description = [[config['Behavior']['UseinMalwarePluralDesc'].format(malware.Name), malware.Description[0][1]]])
                for _, d in enumerate(newMalware.Description):
                    if d[1] != malware.Description[0][1] and not any(d[1] in sl.Description[0][1] for sl in behavior_dict['MalLinks']): # Check if other malwareLinks use the reference link. If so, don't delete the link
                        behavior_dict['References'].remove(d[1])

                behavior_dict["MalLinks"][i] = malware
            elif newMalware.ID in malware.ID:
                for i, d in enumerate(newMalware.Description):
                    if d[1] != malware.Description[0][1] and not any(d[1] in sl.Description[0][1] for sl in behavior_dict['MalLinks']):
                        behavior_dict['References'].remove(d[1])
            
            found = True
            break
            
    
    if not found:
        behavior_dict["MalLinks"].append(newMalware)

    # Write to file
    create_behavior_page(behavior_dict, behavior_file_link)

    return


# ==============================================================================
# MALWARE CORPUS HELPERS
# ==============================================================================
Behavior = namedtuple('Behavior', ['Name', 'ID', 'Link', 'Description']) # Example: ['Execution::User Execution', 'E1204', '../execution/user-execution.md', [('Description....', <url>), ]]

def analyze_malware_file_header(file):
    """Parses read malware file and returns the header values in a dict:

    Args: 
        Malware file in the form of ONE string (using .read())
    Returns: 
        {
            "ID": ,
            "Aliases": ,
            "Platforms": ,
            "Year": ,
            "Associated ATT&CK Software": 
        }
    """
    return_dict = {}

    pattern = config['Malware']['HeaderRegex']

    id = regex_match_single(pattern.format('ID'), file, "ID field of header")
    return_dict["ID"] = id

    aliases = regex_match_single(pattern.format('Aliases'), file, "Aliases field of header")
    # Malware can sometimes have multiple aliases, so handle that here
    if ',' in aliases:
        aliases = aliases.split(', ')
    return_dict["Aliases"] = aliases

    platforms = regex_match_single(pattern.format('Platforms'), file, "Platforms field of header")
    return_dict["Platforms"] = platforms
    
    year = regex_match_single(pattern.format('Year'), file, "Year field of header")
    return_dict["Year"] = year

    attack_soft = regex_match_single(config['Malware']['AssociatedSoftwareRegex1'], file, "Associated ATT&CK Software field of header")
    # if attack_soft != 'None':
    #     # Do a bit more processing, converting "<a href="https://attack.mitre.org/software/S0370/">SamSam</a>" to just "SamSam"
    #     attack_soft = regex_match_single(config['Malware']['AssociatedSoftwareRegex2'], attack_soft, "Associated ATT&CK Software link and name")
    return_dict["Associated ATT&CK Software"] = attack_soft

    return return_dict

def analyze_malware_file_section_line_nums(file_list):
    """Parses read malware file and returns the line numbers of each section in a dict
    
    Args:
        Malware file in the form of a LIST (using .readlines() or .read() w/ .split())
    Returns:
        {
            Title: {}
            ATT&CK Techniques: {}
            Enhanced ATT&CK Techniques: {}
            MBC Behaviors: {}
            Indicators of Compromise: {}
            References: {}
        }
    """

    # Title needs special regex matching syntax bc it is not constant
    for line in file_list:
        title_match = regex_match_single(config['Malware']['TitleRegex'], line)
        if title_match is not None:
            title = title_match
            title_line = file_list.index(line)
    if title is None:
        raise Exception('Title not found')

    attack_line = index_of(config['Malware']['AttackRegex'], file_list)
    enhanced_line = index_of(config['Malware']['EnAttackRegex'], file_list)
    mbc_line = index_of(config['Malware']['BehaviorRegex'], file_list)
    ioc_line = index_of(config['Malware']['IoCRegex'], file_list)
    ref_line = index_of(config['Malware']['ReferencesRegex'], file_list)

    return {
        title: title_line,
        'ATT&CK Techniques': attack_line,
        'Enhanced ATT&CK Techniques': enhanced_line,
        'MBC Behaviors': mbc_line,
        'Indicators of Compromise': ioc_line,
        'References': ref_line
    }

def analyze_malware_file_title(file_list, line_num_dict = None):
    """Parses read malware file and returns the Malware Title name and description
    

    Args:
        - Malware file in the form of a LIST (using .readlines() or .read() w/ .split())
        - Optional: Dict of sectional line numbers (created by analyze_malware_section_line_nums())
    Returns:
        {
            "Name": ,
            "Description": 
        }
    """

    return_dict = {}

    if line_num_dict is None:
        line_num_dict = analyze_malware_file_section_line_nums(file_list)

    title = list(line_num_dict.keys())[0]
    return_dict["Name"] = title

    index = line_num_dict[title] + 2
    description = []
    line = ""

    while "##" not in line:
        line = file_list[index]
        description.append(line)
        index += 1

    description = description[:-2]

    return_dict["Description"] = description

    return return_dict

def analyze_malware_file_behaviors(file_list, line_num_dict = None, reference_list = None):
    """Parses read malware file and returns the behaviors and techniques exhibited by the malware in a dict of Behavior tuples
    
    This function will consider if the 'ATT&CK Techniques', 'Enhanced ATT&CK Techniques', and 'Indicators of Compromise' sections are missing
    This function assumes that 'MBC Behaviors' and 'References' sections are present

    Args:
        - Malware file in the form of a LIST (using .readlines() or .read() w/ .split())
        - Optional: Dict of sectional line numbers (created by analyze_malware_section_line_nums())
        - Optional: List of references (created by analyze_malware_file_references())
    Returns:
        {
            ATT&CK Techniques: [BehaviorTuple, BehaviorTuple]
            Enhanced ATT&CK Techniques: [BehaviorTuple, BehaviorTuple]
            MBC Behaviors: [BehaviorTuple, BehaviorTuple]
            Extra ATT&CK Technique Text: <If there is a 'See ATT&CK..' line (such as blackenergy)>
        }
    """
    return_dict = {
        'ATT&CK Techniques': [],
        'Enhanced ATT&CK Techniques': [],
        'MBC Behaviors': [],
        'Extra ATT&CK Technique Text': None
    }

    if line_num_dict is None:
        line_num_dict = analyze_malware_file_section_line_nums(file_list)
    if reference_list is None:
        reference_list = analyze_malware_file_references(file_list, line_num_dict)

    # Attack
    # Splits the malware file either from sections ATT&CK Techniques to Enhanced ATT&CK Techniques or ATT&CK Techniques to MBC Behaviors if enhanced not present
    # Does regex matching (twice) to create groupings
    if line_num_dict['ATT&CK Techniques']:
        if line_num_dict['Enhanced ATT&CK Techniques']:
            attack_list = file_list[line_num_dict['ATT&CK Techniques']:line_num_dict['Enhanced ATT&CK Techniques']]
        else:
            attack_list = file_list[line_num_dict['ATT&CK Techniques']:line_num_dict['MBC Behaviors']]
        
        try:
            attack_list = attack_list[index_of(config['Malware']['TableStr'],attack_list)+1:] # Getting rid of lines up to and including '|---|---|'
        except TypeError:
            attack_list = attack_list[1:]

        for attack in attack_list:
            if attack != '':
                if "See ATT&CK" in attack:
                    return_dict['Extra ATT&CK Technique Text'] = attack
                    continue

                result = regex_match_all(config['Malware']['BehavRegex'], attack, "the following ATT&CK technique: {}".format(attack))[0]
                if result[3] != '':
                    descript_match = regex_match_all(config['Malware']['DescRegex'], result[3], "description section of {}".format(attack))

                    # Convert ref numbers to links
                    for i, x in enumerate(descript_match):
                        x = list(x)
                        x[1] = reference_list[int(x[1])-1]
                        descript_match[i] = x
                else:
                    descript_match = None
                return_dict['ATT&CK Techniques'].append(Behavior(result[0], result[1], result[2], descript_match))

    # Enhanced ATT&CK
    if line_num_dict['Enhanced ATT&CK Techniques']:
        if line_num_dict['MBC Behaviors']:
            en_attack_list = file_list[line_num_dict['Enhanced ATT&CK Techniques']:line_num_dict['MBC Behaviors']]
        elif line_num_dict['Indicators of Compromise']:
            en_attack_list = file_list[line_num_dict['Enhanced ATT&CK Techniques']:line_num_dict['Indicators of Compromise']]
        en_attack_list = en_attack_list[index_of(config['Malware']['TableStr'],en_attack_list)+1:] # Getting rid of lines up to and including '|---|---|'

        for attack in en_attack_list:
            if attack != '':
                result = regex_match_all(config['Malware']['BehavRegex'], attack, "the following Enhanced ATT&CK technique: {}".format(attack))[0]
                if result[3] != '':
                    descript_match = regex_match_all(config['Malware']['DescRegex'], result[3], "description section of {}".format(attack))

                    # Convert ref numbers to links
                    for i, x in enumerate(descript_match):
                        x = list(x)
                        x[1] = reference_list[int(x[1])-1]
                        descript_match[i] = x
                else:
                    descript_match = None
                return_dict['Enhanced ATT&CK Techniques'].append(Behavior(result[0], result[1], result[2], descript_match))

    # MBC Behaviors
    if line_num_dict['Indicators of Compromise']:
        mbc_behavior_list = file_list[line_num_dict['MBC Behaviors']:line_num_dict['Indicators of Compromise']]
    else:
        mbc_behavior_list = file_list[line_num_dict['MBC Behaviors']:line_num_dict['References']]
   
    mbc_behavior_list = mbc_behavior_list[index_of(config['Malware']['TableStr'],mbc_behavior_list)+1:] # Getting rid of lines up to and including '|---|---|'

    for behavior in mbc_behavior_list:
        if behavior != '':
            result = regex_match_all(config['Malware']['BehavRegex'], behavior, "the following MBC Behavior: {}".format(behavior))[0]
            if result[3] != '':
                descript_match = regex_match_all(config['Malware']['DescRegex'], result[3], "description section of {}".format(behavior))
                
                # Convert ref numbers to links
                for i, x in enumerate(descript_match):
                    x = list(x)
                    x[1] = reference_list[int(x[1])-1]
                    descript_match[i] = x
            else:
                descript_match = None
            return_dict['MBC Behaviors'].append(Behavior(result[0], result[1], result[2], descript_match))

    return return_dict

def analyze_malware_file_ioc(file_list, line_num_dict = None):
    """Parses read malware file and returns the Indicators of Compromise of the malware in a dict
    
    This function assumes that the formatting is as follows:
    <category>
    - <value>

    Example:
    SHA256 Hashes
    - 0785bb93fdb219ea8cb1673de1166bea839da8ba6d7312284d2a08bd41e38cb9

    This function also assumes that the references section comes right after the IoC section
    
    Args:
        - Malware file in the form of a LIST (using .readlines() or .read() w/ .split())
        - Optional: Dict of sectional line numbers (created by analyze_malware_section_line_nums())
    Returns:
        {
            "SHA256 Hashes": [],
            <category>
        }
    """
    return_dict = {}
    category = "Default"

    if line_num_dict is None:
        line_num_dict = analyze_malware_file_section_line_nums(file_list)

    # Splits malware file into just IoC section
    ioc_lines = file_list[line_num_dict['Indicators of Compromise']+1:line_num_dict['References']]
    
    for line in ioc_lines:
        if line != '':
            if line[0] != '-':  # Discovering a new category
                return_dict[line] = []
                category = line
            else:
                if "Unavailable" in line:
                    return_dict[category] = None
                    continue
                if category == "Default" and "Default" not in return_dict.keys():
                    return_dict["Default"] = []
                return_dict[category].append(line[2:])

    return return_dict

def analyze_malware_file_references(file_list, line_num_dict = None):
    """Parses read malware file and returns the References of the malware in a list

    This function assumes that the references section is the last section of a malware file and that the ref IDs start at 1 and increment in order
    
    Args:
        - Malware file in the form of a LIST (using .readlines() or .read() w/ .split())
        - Optional: Dict of sectional line numbers (created by analyze_malware_section_line_nums())
    Returns:
        [<link>, <link>, ]
    """
    return_list = []
    
    if line_num_dict is None:
        line_num_dict = analyze_malware_file_section_line_nums(file_list)

    # Splits malware file into just Reference section
    ref_lines = file_list[line_num_dict['References']+1:]
    
    for line in ref_lines:
        if line != '':
            link = regex_match_single(config['Malware']['ReferenceRegex'], line, "Reference {}".format(line))
            return_list.append(link)


    return return_list

def analyze_malware_file_all(file):
    """Parses an entire malware file, and returns all metadata in the form of a dict:

    Args: 
        Malware file in the form of ONE string (using .read())
    Returns: 
        {
            "Headers": {},
            "Line Nums": {},
            "Behaviors": {},
            "IoC": {},
            "References": {}
        }
    """

    return_dict = {
        "Headers": {},
        "Line Nums": {},
        "Behaviors": {},
        "IoC": {},
        "References": {}
    }

    file_list = file.split('\n')

    return_dict['Headers'] = analyze_malware_file_header(file)
    return_dict['Line Nums'] = analyze_malware_file_section_line_nums(file_list)
    return_dict['Title'] = analyze_malware_file_title(file_list, return_dict["Line Nums"])
    return_dict['References'] = analyze_malware_file_references(file_list, return_dict["Line Nums"])
    return_dict['Behaviors'] = analyze_malware_file_behaviors(file_list, return_dict["Line Nums"], return_dict["References"])
    return_dict['IoC'] = analyze_malware_file_ioc(file_list, return_dict["Line Nums"])

    return return_dict


def create_malware_corpus_page(new_dict, path):
    """Writes file specified by path, with content of new_dict. The format of new_dict adheres to what's returned in analyze_malware_file_all
    
    Args: 
        - dict of malware file with changes
        - Path to malware file
    Returns: 
        - None
    """

    malware_lines = []
    
    # Generate headers
    if type(new_dict['Headers']['Aliases']) is list:
        new_header = config['Malware']['HeaderStr'].format(new_dict['Headers']['ID'], ', '.join(new_dict['Headers']['Aliases']), new_dict['Headers']['Platforms'], new_dict['Headers']['Year'], new_dict['Headers']['Associated ATT&CK Software'])
    else:
        new_header = config['Malware']['HeaderStr'].format(new_dict['Headers']['ID'], new_dict['Headers']['Aliases'], new_dict['Headers']['Platforms'], new_dict['Headers']['Year'], new_dict['Headers']['Associated ATT&CK Software'])
    malware_lines.append(new_header)
    malware_lines.append('')

    # Generate title + description
    malware_lines.append(config['Malware']['TitleStr'].format(new_dict['Title']['Name']))
    malware_lines.append('')
    malware_lines.extend(new_dict['Title']['Description'])
    malware_lines.append('')

    # Generate ATT&CK Techniques
    if new_dict['Behaviors']['ATT&CK Techniques']:
        malware_lines.append(config['Malware']['AttackRegex'])
        malware_lines.append('')
        malware_lines.append(config['Malware']['BehavTableStr'])
        malware_lines.append(config['Malware']['TableStr'])

        for attack in new_dict['Behaviors']['ATT&CK Techniques']:

            desc = ""
            for d in attack.Description: 
                refnum = new_dict['References'].index(d[1]) + 1
                desc = desc + config['Malware']['BehavDescStr'].format(d[0], refnum, refnum)
                desc = desc[0].upper() + desc[1:-1]
            malware_lines.append(config['Malware']['BehavStr'].format(attack.Name, attack.ID, attack.Link, desc))
        
        malware_lines.append('')

    if new_dict['Behaviors']['Extra ATT&CK Technique Text']:
        malware_lines.append(new_dict['Behaviors']['Extra ATT&CK Technique Text'])
        malware_lines.append('')

    # Generate Enhanced ATTACK
    if new_dict['Behaviors']['Enhanced ATT&CK Techniques']:
        malware_lines.append(config['Malware']['EnAttackRegex'])
        malware_lines.append('')
        malware_lines.append(config['Malware']['BehavTableStr'])
        malware_lines.append(config['Malware']['TableStr'])
        
        for attack in new_dict['Behaviors']['Enhanced ATT&CK Techniques']:
            desc = ""
            for d in attack.Description:
                refnum = new_dict['References'].index(d[1]) + 1
                desc = desc + config['Malware']['BehavDescStr'].format(d[0], refnum, refnum)
                desc = desc[0].upper() + desc[1:-1]
            malware_lines.append(config['Malware']['BehavStr'].format(attack.Name, attack.ID, attack.Link, desc))

        malware_lines.append('')

    # Generate MBC Behavior
    if new_dict['Behaviors']['Enhanced ATT&CK Techniques']:
        malware_lines.append(config['Malware']['BehaviorRegex'])
        malware_lines.append('')
        malware_lines.append(config['Malware']['BehavTableStr'])
        malware_lines.append(config['Malware']['TableStr'])

        for behav in new_dict['Behaviors']['MBC Behaviors']:
            desc = ""
            for d in behav.Description:
                refnum = new_dict['References'].index(d[1]) + 1
                desc = desc + config['Malware']['BehavDescStr'].format(d[0], refnum, refnum)
                desc = desc[0].upper() + desc[1:-1]
            malware_lines.append(config['Malware']['BehavStr'].format(behav.Name, behav.ID, behav.Link, desc))

        malware_lines.append('')

    # Generate IoC
    malware_lines.append(config['Malware']['IoCRegex'])
    malware_lines.append('')
    for key, value in new_dict['IoC'].items():
            if key == "Default":
                for ioc in value:
                    malware_lines.append(config['Malware']['IoCStr'].format(ioc))
            else:
                malware_lines.append(key)
                for ioc in value:
                    malware_lines.append(config['Malware']['IoCStr'].format(ioc))

    malware_lines.append('')

    # Generate References
    malware_lines.append(config['Malware']['ReferencesRegex'])
    malware_lines.append('')
    counter = 1
    for link in new_dict['References']:
        malware_lines.append(config['Malware']['ReferenceStr'].format(counter, counter, link) + "\n")
        counter += 1

    # write to file

    with open(path, 'w') as f:
        f.writelines(s + '\n' for s in malware_lines)

    f.close()
    
    return
