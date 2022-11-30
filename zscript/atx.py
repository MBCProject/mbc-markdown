import os
import re


# Converts all header format to atx (# ...)
def dir_walk(directory):
    ignorelist = ["nursery", '.github', '.git', 'LICENSE.txt', 'README.md', '.gitattributes', 'ynewsletters', 'yfaq', 'zscript']

    # Iterate recursively over all files in the repo
    for root, dirs, files in os.walk(directory):
        if not any(block in root for block in ignorelist):
            for name in files:
                f = open(os.path.join(root, name), "r")
                lines = f.readlines()  # Read contents of each capa rule
                f.close()

                for line in lines:
                    equals = re.search("={3,}\n", line)  # Search capa rule for attack mapping, if found, add to attack counter
                    
                    if equals:
                        print(os.path.join(root, name))
                        index = lines.index(equals.group(0))
                        lines.remove(equals.group(0))
                        lines[index-1] = "# {0}\n".format(lines[index-1])

                
                        with open(os.path.join(root, name), 'w') as f:
                            for line in lines:
                                f.write(line)
                            f.close()



dir_walk('..')