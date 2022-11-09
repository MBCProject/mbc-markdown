#!/usr/bin/python

import sys
import re
import glob
import argparse

from fuzzywuzzy import fuzz  # pip install fuzzywuzzy python-Levenshtein

objective_list = ['anti-behavioral-analysis', 'anti-static-analysis', 'collection', 'command-and-control', 'credential-access', 'defense-evasion', 'discovery', 'execution', 'exfiltration', 'impact', 'lateral-movement', 'micro-behaviors', 'persistence', 'privilege-escalation']
anti_analysis_types = ['Evasion', 'Detection']
impact_types = ['Integrity', 'Breach', 'Availability']

# Checks if 'string' in 'l' at index 'line_num'. If missing, insert 'string' into 'l' at index 'line_num'
# Return possibly modified 'l'
def insert_if_missing(l, line_num, string):
    if l[line_num] != string:
        l.insert(line_num, string)

    return l

# Matches string to an entry in objective_list
def objective_search(string):
    string = string.lower().replace('_', '-')
   
    if string not in objective_list:
        raise Exception("Objective {} did not match anything: ".format(string))

    return "../" + string

def main():
    # Initialize parser
    parser = argparse.ArgumentParser(description="Inserts a formatted header for MBC. Only add parameters that are missing. In case of bugs, only run on a second copy")
    
    # Adding arguments
    parser.add_argument("-f", "--file", help = "File to modify", required=True)
    parser.add_argument("-i", "--id", help = "ID (B0001)")
    parser.add_argument("-o", "--objective", nargs='+', help = "Objectives separated by spaces, replace spaces within the name with underscore (Anti-Behavioral_Analysis Anti-Static_Analysis)")
    parser.add_argument("-a", "--attack", nargs='+', help = "Related ATT&CK Techniques grouped by name and ID (Debugger_Evasion,T1622 Virtualization/Standbox_Evasion_Checks,T1497.001,T1633.001)")
    parser.add_argument("-t", "--type", help = "Anti-Analysis or Impact Types (Evasion, Detection, Integrity, Breach, Availability)")
    parser.add_argument("-v", "--version", help="Version")
    parser.add_argument("-c", "--created", help="Method Creation Date (1_August_2019)")
    parser.add_argument("-m", "--last_modified", help="Last modified date (1_August_2019)")

    # Read arguments from command line
    args = parser.parse_args()
    
    # Read file
    file = args.file
    with open(file) as f:
        lines = f.readlines()
        f.close()

    offset = 0  # Handles unique fields such as anti-analysis/impact type

    # Some files have an empty line 1, delete that
    if lines[0] == '\n':
        lines.pop(0)

    # Checking if first line is <table>, if not, that means this file does not have any appropriate header formatting
    lines = insert_if_missing(lines, 0, "<table>\n")
    lines = insert_if_missing(lines, 1, "<tr>\n")
    
    # Adding ID field
    if args.id:
        lines = insert_if_missing(lines, 2, "<td><b>ID</b></td>\n")
        lines.insert(3, "<td><b>{}</b></td>\n".format(args.id))
        lines.insert(4, "</tr>\n")

    # Adding Objective field
    if args.objective:
        lines = insert_if_missing(lines, 5, "<tr>\n")
        lines = insert_if_missing(lines, 6, "<td><b>Objective(s)</b></td>\n")
        
        # Build objectives if multiple
        obj_str = "<td><b>"
        for objective in args.objective:
            obj_path = objective_search(objective)
            objective = objective.replace('_', ' ')

            obj_str = obj_str + "<a href=\"{}\">{}</a>, ".format(obj_path, objective)
        
        # Chop off last ', '
        obj_str = obj_str[:len(obj_str) - 2]
        obj_str = obj_str + "</b></td>\n"

        lines.insert(7, obj_str)
        lines.insert(8, "</tr>\n")

    # Adding Related ATT&CK Techniques Field
    if args.attack:
        lines = insert_if_missing(lines, 9, "<tr>\n")
        lines = insert_if_missing(lines, 10, "<td><b>Related ATT&CK Techniques</b></td>\n")

        # Build attack links if multiple
        attack_str = "<td><b>"
        for attack in args.attack:
            attack = attack.split(",")
            attack_name = attack[0].replace('_', ' ')
            
            attack_str = attack_str + attack_name + " ("

            # Looking at technique IDs now
            for i in range(1, len(attack)):
                attack_id = attack[i]
                attack_id_dash = attack_id.replace('.', '/')

                attack_str = attack_str + "<a href=\"https://attack.mitre.org/techniques/{}/\">{}</a>, ".format(attack_id_dash, attack_id)

            # Chop off last ', '
            attack_str = attack_str[:len(attack_str) - 2]
            attack_str = attack_str + "), "

        # Chop off last ', '
        attack_str = attack_str[:len(attack_str) - 2]
        attack_str = attack_str + "</b></td>\n"

        lines.insert(11, attack_str)
        lines.insert(12, "</tr>\n")
        print(attack_str)

    # Adding Anti-Analysis/Impact Type
    if args.type:
        if args.type in impact_types:
            lines.insert(13, "<tr>\n")
            lines = insert_if_missing(lines, 14, "<td><b>Impact Type</b></td>\n")

        elif args.type in anti_analysis_types:
            lines.insert(13, "<tr>\n")
            lines = insert_if_missing(lines, 14, "<td><b>Anti-Analysis Type</b></td>\n")

        else:
            raise Exception("Anti-Analysis/Impact Type is not valid")
        
        lines.insert(15, "<td><b>{}</b></td>\n".format(args.type))
        lines.insert(16, "</tr>\n")

        offset += 4

    # Adding version field
    if args.version:
        lines = insert_if_missing(lines, 13+offset, "<tr>\n")
        lines = insert_if_missing(lines, 14+offset, "<td><b>Version</b></td>\n")

        lines.insert(15+offset, "<td><b>{}</b></td>\n".format(args.version))
        lines.insert(16+offset, "</tr>\n")

    # Adding Created field
    if args.created:
        lines = insert_if_missing(lines, 17+offset, "<tr>\n")
        lines = insert_if_missing(lines, 18+offset, "<td><b>Created</b></td>\n")

        created = args.created.replace('_', ' ')
        lines.insert(19+offset, "<td><b>{}</b></td>\n".format(created))
        lines.insert(20+offset, "</tr>\n")
    
    # Adding Last Modified Field
    if args.last_modified:
        lines = insert_if_missing(lines, 21+offset, "<tr>\n")
        lines = insert_if_missing(lines, 22+offset, "<td><b>Last Modified</b></td>\n")

        last_modified = args.last_modified.replace('_', ' ')
        lines.insert(23+offset, "<td><b>{}</b></td>\n".format(last_modified))
        lines.insert(24+offset, "</tr>\n")

    lines = insert_if_missing(lines, 25+offset, "</table>\n")
    lines = insert_if_missing(lines, 26+offset, "\n")

    # Now that modifications are complete, write to file
    with open(file, "w") as f:
        for line in lines:
            f.write(line)

    f.close()
           
    return

if __name__=="__main__":
    main()