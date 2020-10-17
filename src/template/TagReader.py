import os
import html
import re
import glob

def get_tags(directory):
    foundTags = []
    files = glob.glob(directory + "/**/*.html", recursive=True)
    for filename in files:
        fname = os.path.join(directory,filename)
        with open(fname, 'r') as f:
                html = f.read()
                tags = re.findall(r'<%[^\s]+%>', html)
                for tag in tags:
                    if tag not in foundTags:
                        foundTags.append(tag)
    return(foundTags)


print(get_tags("./"))
