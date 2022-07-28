#!/usr/bin/python

import sys
import re
import glob

from fuzzywuzzy import fuzz  # pip install fuzzywuzzy python-Levenshtein


MALWARE_EXAMPLES_HEADER = "\nMalware Examples\n----------------\n|Name|Date|Description|\n|---|---|---|\n"
REFERENCES_HEADER = "\nReferences\n----------"
ATTACK_TECHNIQUE_HEADER = "\nATT&CK Techniques\n-----------------\n|Name|Use|\n|---|---|\n"
BEHAVIORS_HEADER = "\nBehaviors\n---------\n|Name|Use|\n|---|---|\n"

def file_search(file_lines, string): # Searches file f for a string, returns the line number. If not found, return -1
    count = 0

    for x in file_lines:
        if string in x:
            return count
        
        count += 1

    return -1


def fuzzy_file_directory_search(files, string): # Searches file directories for a file using fuzzy matching
    count = 0
    f = ''
    for file in files:
        x = fuzz.partial_ratio(file, string)
        # print(file + " " + str(x))
        if x > count:  # Returns highest fuzzy match score
            count = x
            f = file
    
    if count == 0 or f is None:
        raise Exception("Fuzzy file search did not find anything: ".format(string))

    return f


def populate_behavior(name, date, reference, path, description, orig_file):
    # if len(sys.argv) != 4:
    #     print("This script needs three command-line parameters: the malware name, date, and reference link. Additionally, paste the markdown into the input file")
    #     return 
    

    # malware_name = sys.argv[1]
    # malware_date = sys.argv[2]
    # reference_link = sys.argv[3]
    # input_regex = "\[[^]]*\]\(([^\)]*)\)\|(.*?) \["
    # input_regex2 = "\[[^]]*\]\(([^\)]*)\)\|"
    reference_regex = "<a name="

    # lines = []
    # with open("input") as f:  # Reading input file
    #     lines = f.readlines()

    # for line in lines:  # Pulling path+description from input file
    #     x = re.search(input_regex, line)
    #     try:
    #         path = x.group(1)
    #         description = x.group(2)
    #     except AttributeError:
    #         x = re.search(input_regex2, line)
    #         path = x.group(1)
    #         description = ""
       
    with open(path, "r+") as f:  # Navigating to 'path', determining if behavior already has a 'Malware Example' section
        mbcBehaviorLines = f.readlines()
        f.seek(0)
        mbcFile = f.read()

    if file_search(mbcBehaviorLines, name) != -1: # If malware is already listed, skip this file
        print("[+] Detecting that {} is already in {}\n".format(name, path))
        return

    malware_examples_line = file_search(mbcBehaviorLines, 'Malware Examples')  # Determining if Malware Examples and Reference sections are present
    references_line = file_search (mbcBehaviorLines, 'References')

    if malware_examples_line == -1: # If there is no malware_examples line, build one
        if references_line == -1: # If there is no reference section, we can write malware_examples to the end
            mbcBehaviorLines.append(MALWARE_EXAMPLES_HEADER)
            malware_examples_line = len(mbcBehaviorLines) - 1
        else:
            mbcBehaviorLines.insert(references_line - 1, MALWARE_EXAMPLES_HEADER)
            malware_examples_line = references_line - 1

    if references_line == -1: # If there is no reference section, write a reference header at the end of the file
        mbcBehaviorLines.append(REFERENCES_HEADER)
        references_line = len(mbcBehaviorLines)

    # Count number of references present, then add one for the new entry
    reference_num = len(re.findall(reference_regex, mbcFile)) + 1

    # Building the text
    malware_example_text = "|[**{}**]({})|{}|{} [[{}]](#{})|\n".format(name, orig_file, date, description, reference_num, reference_num)
    reference_text = '\n<a name="{}">[{}]</a> {}\n'.format(reference_num, reference_num, reference)
    
    # Insert malware notation in the line above the Reference line (which should be the bottom of malware examples)
    # Insert new reference at the end
    mbcBehaviorLines.insert(references_line - 1, malware_example_text)
    mbcBehaviorLines.append(reference_text)

    # Fix some spacing issues between sections if present
    malware_examples_line = file_search(mbcBehaviorLines, 'Malware Examples')
    if mbcBehaviorLines[malware_examples_line - 1] != '\n':
        mbcBehaviorLines.insert(malware_examples_line, '\n')

    references_line = file_search(mbcBehaviorLines, 'References')
    if mbcBehaviorLines[references_line - 1] != '\n':
        mbcBehaviorLines.insert(references_line, '\n')

    with open(path, "w") as f:
        f.writelines(mbcBehaviorLines)

    print("[+] Inserting Malware Reference into {}\n".format(path))
    return


# Receives an input file such as 'example_input', parses the file and inserts corresponding information into the markdown
# NOTE: Does require the example malware file to be created first
def populate_malware_example(input_file):
    references = []
    input_regex = "(.*?) (\(\S+)\s+\[(\d)\]\s(.*)"
    input_regex2 = "(.*?) (\(\S+)\s+\[(\d)\]\s"
    reference_regex = '<a name="\d+">\[\d+\]<\/a> (\S+)'
    date_regex = "\|\*\*Year\*\*\|(.*?)\|"

    mbc_file_map = glob.glob('../**/*.md', recursive=True)  # Get list of all files in MBC

    with open(input_file) as f:  # Reading input file
        # Read first line, which should be a name
        line = f.readline()
        if not re.search('X\d{4}', line): # Asserts that name line (Kraken X0010) is correctly formatted
            raise Exception("Name syntax not correct")
        name_line = line.split()

        # Start iteratively reading the next lines
        input_lines = f.readlines()
    
    print("[+] Input File parsed, searching for {}".format(name_line[0]))

    # Try to match malware name to the corresponding xample-malware using fuzzy string matching
    malware_files = glob.glob("../xample-malware/*")
    name = "../xample-malware/" + name_line[0].lower() + ".md"
    modified_xample_file = fuzzy_file_directory_search(malware_files, name)

    print("[+] Malware file found: {}\n".format(modified_xample_file))


    # Reading the xample-malware file
    with open(modified_xample_file) as f:
        xample_file_lines = f.readlines()
        f.seek(0)
        xample_file_whole = f.read()

    
    # Verify file id with xample_file
    if name_line[1] not in xample_file_whole:
        raise("Exception malware ID did not match file")

    # Get date
    date = re.findall(date_regex, xample_file_whole)[0]

    # Searching xample-malware file to see what sections are present
    attack_techniques_line = file_search(xample_file_lines, 'ATT&CK Techniques')
    behaviors_line = file_search(xample_file_lines, 'Behaviors')
    references_line = file_search(xample_file_lines, 'References')

    # Fill in missing sections
    if references_line == -1:
        xample_file_lines.append(REFERENCES_HEADER)
    # print(xample_file_lines)

    if behaviors_line == -1:
        references_line = file_search(xample_file_lines, 'References')
        xample_file_lines.insert(references_line, BEHAVIORS_HEADER)

    if attack_techniques_line == -1:
        behaviors_line = file_search(xample_file_lines, 'Behaviors')
        xample_file_lines.insert(behaviors_line, ATTACK_TECHNIQUE_HEADER)
    

    # Count number of references present
    existing_references = re.findall(reference_regex, xample_file_whole)
    for ref in existing_references:
        references.append(ref)
    reference_diff = len(existing_references)

    # Iterate through input file and populate xample-malware file
    for line in input_lines:
        if line.isspace():
            continue

        if "Reference" in line:  # Determines if reference is already present, if not, add it
            reference_link = line.split()[-1]
            if reference_link not in xample_file_whole:
                references.append(reference_link)
                reference_num = len(references)
                reference_text = '\n<a name="{}">[{}]</a> {}\n'.format(reference_num, reference_num, reference_link)
                xample_file_lines.append(reference_text)
            
        else:  # Parse behavior/technique lines
            print("[+] Parsing " + line.replace("\n", ''))
            x = re.search(input_regex, line) 
            try:
                technique_behavior = x.group(1)
                id = x.group(2)
                reference = x.group(3)
                description = x.group(4)
            except AttributeError:  # In case description is absent
                x = re.search(input_regex2, line)
                technique_behavior = x.group(1)
                id = x.group(2)
                reference = x.group(3)

            if reference_diff > 0:
                reference_diff -= 1
            reference = str(int(reference) + reference_diff)
            reference_link = references[int(reference) - 1]

            if id in xample_file_whole:
                print("[+] Skipping {} because already present".format(id))
                continue

        
            if 'T' in id: # Determine if ATT&CK technique
                attack_link = "https://attack.mitre.org/techniques/{}/".format(id.replace('(', '').replace(')', '').replace('.', '/'))
                technique_text = "|[{} {}]({})|{} [[{}]](#{})|\n".format(technique_behavior, id, attack_link, description, reference, reference)
                
                behaviors_line = file_search(xample_file_lines, 'Behaviors')
                xample_file_lines.insert(behaviors_line, technique_text)

                print("[+] Inserting ATT&CK technique: {}\n".format(technique_behavior))

            else:  # If it is an MBC behavior
                # Try to fuzzy match the input behavior to a file 
                print("[+] Searching for {}".format(technique_behavior))
                mbc_file = fuzzy_file_directory_search(mbc_file_map, technique_behavior)
                print("[+] Behavior found: {}".format(mbc_file))

                behavior_text = "|[{} {}]({})|{} [[{}]](#{})|\n".format(technique_behavior, id, mbc_file, description, reference, reference)
                
                references_line = file_search(xample_file_lines, 'References')
                xample_file_lines.insert(references_line, behavior_text)

                # Add malware entry into the behavior file itself
                populate_behavior(name_line[0], date, reference_link, mbc_file, description, modified_xample_file)

    # Fix some spacing issues between sections if present
    behaviors_line = file_search(xample_file_lines, 'Behaviors')
    if xample_file_lines[behaviors_line - 1] != '\n':
        xample_file_lines.insert(behaviors_line, '\n')

    references_line = file_search(xample_file_lines, 'References')
    if xample_file_lines[references_line - 1] != '\n':
        xample_file_lines.insert(references_line, '\n')


    with open(modified_xample_file, "w") as f:
        f.writelines(xample_file_lines)

def main():
    if len(sys.argv) != 2:
        print("This script needs one command-line parameters: the path to the input file")
        return 
    

    input_file = sys.argv[1]
    populate_malware_example(input_file)
    return


if __name__=="__main__":
    main()