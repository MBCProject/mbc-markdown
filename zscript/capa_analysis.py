#!/usr/bin/python3

import os
import re
import sys
from collections import Counter

import termplotlib as tpl
import yaml


# Walk through capa directory, ignoring files within the ignorelist folders
# Read each file and use regex to match mbc or attack mappings
# If found, insert them into the corresponding Counter
def dir_walk(directory):
    attack_regex = "att&ck:\s*- ([^\n]*)"
    mbc_regex = "mbc:\s*- ([^\n]*)"
    ignorelist = ["nursery", '.github', 'LICENSE.txt', 'README.md', '.gitattributes', '.git']

    attack_mappings = Counter()
    mbc_mappings = Counter()

    # Iterate recursively over all files in the repo
    for root, dirs, files in os.walk(directory):
        if not any(block in root for block in ignorelist):
            for name in files:
                f = open(os.path.join(root, name), "r")
                capa_rule = f.read()  # Read contents of each capa rule

                attack = re.search(attack_regex, capa_rule)  # Search capa rule for attack mapping, if found, add to attack counter
                if attack:
                    attack_mappings.update(Counter([attack.group(1)]))

                mbc = re.search(mbc_regex, capa_rule)
                if mbc:
                    mbc_mappings.update(Counter([mbc.group(1)]))

    return attack_mappings, mbc_mappings

def plot(dict):
    keys = list(dict.keys())
    nums = [dict[x]['num'] for x in keys]
    fig = tpl.figure()
    fig.barh(nums, keys, force_ascii=True)
    fig.show()

# Takes a list of tactics/behaviors and converts them as keys in a dict
# Iterates over list of mappings and split the strings to separate tactics/techniques, behaviors/methods
# Insert into dictionary
# Print out results and create a histogram
def analysis(map, keys, mbc_micro_behaviors=None):
    tactic_behavior_dict = {k: {'num':0, 'rule':[]} for k in keys}
    if mbc_micro_behaviors:
        micro_behavior_dict = {k: {'num':0, 'rule':[]} for k in mbc_micro_behaviors}

    for mapping in map:
        try:
            split_map = mapping.split("::", 1)
            tactic_behavior = split_map[0]
            tactic_behavior_dict[tactic_behavior]['rule'].append(split_map[1])
            tactic_behavior_dict[tactic_behavior]['num'] += 1
        except KeyError:
            if mbc_micro_behaviors:
                try:
                    micro_behavior_dict[tactic_behavior]['rule'].append(split_map[1])
                    micro_behavior_dict[tactic_behavior]['num'] += 1
                except KeyError:
                    print("The following MBC mapping could not be identified: " + str(mapping))
            else:
                print("The following ATT&CK mapping could not be identified: " + str(mapping))


        

    if mbc_micro_behaviors is None:
        print("---------ATT&CK MAPPINGS---------")
        print(yaml.dump(tactic_behavior_dict, default_flow_style=False))
        plot(tactic_behavior_dict)
    else:
        print("\n---------MBC MAPPINGS---------")
        print(yaml.dump(tactic_behavior_dict, default_flow_style=False))
        plot(tactic_behavior_dict)
        print("\n---------MBC MICRO-BEHAVIOR MAPPINGS---------")
        print(yaml.dump(micro_behavior_dict, default_flow_style=False))
        plot(micro_behavior_dict)

def return_mbc_mapping(capa_dir):
    attack_mapping, mbc_mapping = dir_walk(capa_dir)
    return dict(mbc_mapping)
    

if __name__ == "__main__":    
    if sys.argv[1] == "-h":
        print("This script analyzes the capa repo to determine the coverage wrt ATT&CK + MBC. \n Usage: python3 capa_analysis.py <directory>")
    directory = sys.argv[1]

    attack_tactics = ["Reconnaissance", "Resource Development", "Initial Access", "Execution", "Persistence", "Privilege Escalation", "Defense Evasion", "Credential Access", "Discovery", "Lateral Movement", "Collection", "Command and Control", "Exfiltration", "Impact"]
    mbc_behaviors = ["Anti-Behavioral Analysis", "Anti-Static Analysis", "Collection", "Command and Control", "Credential Access", "Defense Evasion", "Discovery", "Execution", "Exfiltration", "Impact", "Lateral Movement","Persistence", "Privilege Escalation"]
    mbc_micro_behaviors = ["Communication", "Cryptography", "Data", "File System", "Hardware", "Memory", "Operating System", "Process"]


    attack_mapping, mbc_mapping = dir_walk(directory)
    analysis(attack_mapping, attack_tactics)

    analysis(mbc_mapping, mbc_behaviors, mbc_micro_behaviors=mbc_micro_behaviors)

    print(dict(mbc_mapping))