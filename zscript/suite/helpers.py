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
    split_name = name.lower().replace('-', '').replace(' ', '-').split('::')

    for file in file_list:
        file_suffix = file.split('/')[-1].replace('.md', '')
        if split_name[-1] == file_suffix or split_name[-2] == file_suffix:
            if rel_path_base:
                return os.path.relpath(file, rel_path_base)

            return file

    raise Exception("No file path matched for '{}'".format(name))


# ==============================================================================
# MALWARE CORPUS HELPERS
# ==============================================================================
Behavior = namedtuple('Behavior', ['Name', 'ID', 'Link', 'Description']) # Example: ['Execution::User Execution', 'E1204', '../execution/user-execution.md', [('Description....', 1), ]]

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

def analyze_malware_file_behaviors(file_list, line_num_dict = None):
    """Parses read malware file and returns the behaviors and techniques exhibited by the malware in a dict of Behavior tuples
    
    This function will consider if the 'ATT&CK Techniques', 'Enhanced ATT&CK Techniques', and 'Indicators of Compromise' sections are missing
    This function assumes that 'MBC Behaviors' and 'References' sections are present

    Args:
        - Malware file in the form of a LIST (using .readlines() or .read() w/ .split())
        - Optional: Dict of sectional line numbers (created by analyze_malware_section_line_nums())
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
                else:
                    descript_match = None
                return_dict['ATT&CK Techniques'].append(Behavior(result[0], result[1], result[2], descript_match))

    # Enhanced ATT&CK
    if line_num_dict['Enhanced ATT&CK Techniques']:
        en_attack_list = file_list[line_num_dict['Enhanced ATT&CK Techniques']:line_num_dict['MBC Behaviors']]
        en_attack_list = en_attack_list[index_of(config['Malware']['TableStr'],en_attack_list)+1:] # Getting rid of lines up to and including '|---|---|'

        for attack in en_attack_list:
            if attack != '':
                result = regex_match_all(config['Malware']['BehavRegex'], attack, "the following Enhanced ATT&CK technique: {}".format(attack))[0]
                if result[3] != '':
                    descript_match = regex_match_all(config['Malware']['DescRegex'], result[3], "description section of {}".format(attack))
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
    """Parses read malware file and returns the References of the malware in a dict

    This function assumes that the references section is the last section of a malware file and that the ref IDs start at 1 and increment in order
    
    Args:
        - Malware file in the form of a LIST (using .readlines() or .read() w/ .split())
        - Optional: Dict of sectional line numbers (created by analyze_malware_section_line_nums())
    Returns:
        {
            1: <link>,
            2: <link>
        }
    """
    return_dict = {}
    counter = 1

    if line_num_dict is None:
        line_num_dict = analyze_malware_file_section_line_nums(file_list)

    # Splits malware file into just Reference section
    ref_lines = file_list[line_num_dict['References']+1:]
    
    for line in ref_lines:
        if line != '':
            link = regex_match_single(config['Malware']['ReferenceRegex'], line, "Reference ID {}".format(counter))
            return_dict[counter] = link
            counter += 1


    return return_dict

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

    return_dict["Headers"] = analyze_malware_file_header(file)
    return_dict["Line Nums"] = analyze_malware_file_section_line_nums(file_list)
    return_dict["Title"] = analyze_malware_file_title(file_list, return_dict["Line Nums"])
    return_dict["Behaviors"] = analyze_malware_file_behaviors(file_list, return_dict["Line Nums"])
    return_dict["IoC"] = analyze_malware_file_ioc(file_list, return_dict["Line Nums"])
    return_dict["References"] = analyze_malware_file_references(file_list, return_dict["Line Nums"])

    return return_dict


def create_malware_corpus_page(new_dict, path):
    """Compares malware file dict (structure is what is returned from analyze_malware_file_all) with old version, and overwrites malware_lines. When finished, writes malware_lines to path
    
    Args: 
        - dict of malware file before changes (returned from analyze_malware_file_all)
        - dict of malware file with changes
        - Malware file in the form of a LIST (using .readlines() or .read() w/ .split())
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
                desc = desc + config['Malware']['BehavDescStr'].format(d[0], d[1], d[1])
                desc = desc[0].upper() + desc[1:]
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
                desc = desc + config['Malware']['BehavDescStr'].format(d[0], d[1], d[1])
                desc = desc[0].upper() + desc[1:]
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
                desc = desc + config['Malware']['BehavDescStr'].format(d[0], d[1], d[1])
                desc = desc[0].upper() + desc[1:]
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
    for num, link in new_dict['References'].items():
            malware_lines.append(config['Malware']['ReferenceStr'].format(num, num, link) + "\n")

    # write to file

    with open(path, 'w') as f:
        f.writelines(s + '\n' for s in malware_lines)

    f.close()
    
    return
