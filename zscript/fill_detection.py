#!/usr/bin/python

import argparse
import re
import subprocess
import yaml

from capa_analysis import return_mbc_mapping

objective_list = ['anti-behavioral-analysis', 'anti-static-analysis', 'collection', 'command-and-control', 'credential-access', 'defense-evasion', 'discovery', 'execution', 'exfiltration', 'impact', 'lateral-movement', 'micro-behaviors', 'persistence', 'privilege-escalation']
capa_rule_blacklist = ['README', 'format']

def yaml_find(d, tag):
    if tag in d:
        yield d[tag]
    for k, v in d.items():
        if isinstance(v, dict):
            for i in yaml_find(v, tag):
                yield i



# Fills file with the detection capa + CAPE headers. Returns new lines and indexes of capa and cape indicating where new entries should be placed
def fill_detection(behavior_lines, index):
    behavior_lines.insert(index, "\n")
    behavior_lines.insert(index+1, "## Detection\n")
    behavior_lines.insert(index+2, "\n")
    behavior_lines.insert(index+3, "|Tool: capa|Mapping|APIs|\n")
    behavior_lines.insert(index+4, "|---|---|---|\n")
    behavior_lines.insert(index+5, "\n")
    behavior_lines.insert(index+6, "|Tool: CAPE|Mapping|APIs|\n")
    behavior_lines.insert(index+7, "|---|---|---|\n")
    behavior_lines.insert(index+8, "\n")

    return behavior_lines, index+5, index+8


# Starting at 'index', parse each line for text in between '[]', which is the rule name. Ends when a blank line is reached. Returns array of rules
def detect_existing_rules(behavior_lines, index):
    rules = []
    rule_line = behavior_lines[index]
    rule_re = "\[([^\]]+)]"
    
    while capa_line != "\n":
        rules.append(re.search(rule_re, rule_line).group(1))
        
        index += 1
        capa_line = behavior_lines[index]

    return rules

# Searches capa-rules repo for mentions of id using subprocess + grep, returns list of capa files that have MBC rule
def search_capa_rules(id, capa_repo):
    capa_rule_paths = []
    grep_output = subprocess.run(["grep", "-r", id, capa_repo], capture_output=True)
    grep_output = grep_output.stdout
    
    rules = grep_output.decode().split('\n')

    for rule in rules:
        if rule == '':
            continue

        rule_path = rule.split(' ', 1)[0][:-1]

        if not any(substring in rule_path for substring in capa_rule_blacklist):
            capa_rule_paths.append(rule_path)

    return capa_rule_paths


# Parses given capa rules and generates and inserts text into MBC file
def fill_capa_rules(capa_rules_path, behavior_lines):
    for rule in capa_rules_path:
        with open(rule) as f:
            capa_yaml = yaml.safe_load(f)
            f.close()

        # print(capa_yaml)
        rule_name = capa_yaml['rule']['meta']['name']
        api = list(yaml_find(capa_yaml, 'api'))
        
        if len(api) > 1:
            raise Exception(">1 API FOUND")
        
        api = api[0]
        


        print(capa_yaml.keys())
        print(rule_name)
        print(api)



    raise Exception


        


def test(file):
    try:
        with open(file) as f:
            behavior_lines = f.readlines()
            f.close()
    except FileNotFoundError:
        print("[X] FILE NOT FOUND: " + file)
        return -1

    # Determine if 'Detection' section already present
    if "## Detection\n" not in behavior_lines:
        if "## Code Snippets\n" in behavior_lines:
            index = behavior_lines.index("## Code Snippets\n") - 1
        elif "## References\n" in behavior_lines:
            index = behavior_lines.index("## References\n") - 1
        else:
            print("[X] Code Snippet or Reference Section not found")
            return -1

        behavior_lines, capa_index, cape_index = fill_detection(behavior_lines, index)


    else:
        capa_index = behavior_lines.index("|Tool: capa|Mapping|APIs|\n") + 2
        cape_index = behavior_lines.index("|Tool: CAPE|Mapping|APIs|\n") + 2

        # If 'Detection' section present, detect existing rules
        capa_rules = detect_existing_rules(behavior_lines, capa_index)
        cape_rules = detect_existing_rules(behavior_lines, cape_index)


    


    with open(file, 'w') as f:
        for line in behavior_lines:
            f.write(line)
        f.close()


def main():
    # Initialize parser
    parser = argparse.ArgumentParser(description="Inserts a 'detection' section into behaviors. The section will contain info on capa and cape rules related to that behavior")
    
    # Adding arguments
    parser.add_argument("-i", "--id", help = "ID (B0001)")
    parser.add_argument("-o", "--objective", nargs='+', help = "Objectives separated by spaces, replace spaces within the name with underscore (Anti-Behavioral_Analysis Anti-Static_Analysis)")
    parser.add_argument("-a", "--attack", nargs='+', help = "Related ATT&CK Techniques grouped by name and ID (Debugger_Evasion,T1622 Virtualization/Standbox_Evasion_Checks,T1497.001,T1633.001)")
    parser.add_argument("-t", "--type", help = "Anti-Analysis or Impact Types (Evasion, Detection, Integrity, Breach, Availability)")
    parser.add_argument("-v", "--version", help="Version")

    parser.add_argument("-m", "--last_modified", help="Last modified date (1_August_2019)")

    parser.add_argument("-c", "--capa", help="capa-rules directory", required=True)
    parser.add_argument("-f", "--file")

    # Read arguments from command line
    args = parser.parse_args()

    if args.file:
        test(args.file)
        return

    # Gets a dict of all behaviors that are mentioned in capa, along with count
    capa_behaviors = return_mbc_mapping(args.capa)

    for behavior, count in capa_behaviors.items():
        # Splitting dict entry into behavior and id
        # EX: communication/socket-communication/create-udp-socket, C0001.010
        str_split = behavior.split(" [", 1)
        behavior_path = str_split[0].lower().replace('::', '/').replace(' ', '-')
        id = str_split[1][:-1]

        # if method or sub-microbehavior, remove portion from path
        if '.' in id:
            str_split = behavior_path.split("/")[:-1]
            behavior_path = '/'.join(str_split)

        # If microbehavior, add 'micro-behaviors' to behavior path
        objective = behavior_path.split('/')[0]
        if objective not in objective_list:
            behavior_path = 'micro-behaviors/' + behavior_path

        behavior_path = '../' + behavior_path + '.md'
        try:
            with open(behavior_path) as f:
                behavior_lines = f.readlines()
                f.close()
        except FileNotFoundError:
            print("[X] FILE NOT FOUND: " + behavior_path)
            return -1

        if "## Code Snippets\n" in behavior_lines:
            index = behavior_lines.index("## Code Snippets\n") - 1
        elif "## References\n" in behavior_lines:
            index = behavior_lines.index("## References\n") - 1
        else: # If Code Snippet or Reference Section missing, return index of last line
            index = len(behavior_lines) - 1

        x = search_capa_rules(id, args.capa)

        fill_capa_rules(x, behavior_lines)
        



    # print(capa_behaviors.keys())
    # print(yaml.dump(capa_behaviors, default_flow_style=False))




if __name__=="__main__":
    main()