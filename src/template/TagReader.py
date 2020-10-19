import os
import html
import re
import glob
import json

def get_tags(directory):
    foundTags = []    
    files = glob.glob(directory + "/**/*.html", recursive=True)
    for filename in files:
        fname = filename # os.path.join(directory,filename)
        with open(fname, 'r') as f:
                html = f.read()
                tags = re.findall(r'<%[^\s]+%>', html)
                for tag in tags:
                    if tag not in foundTags:
                        foundTags.append(tag)
    return(foundTags)

def write_json(tags):
    jsonString = "[\n"
    for tag in tags:
        jsonString +="\t{\"tag\" : \""+tag+"\",\"value\":"+"\"putvaluehere\"},\n"

    jsonString = jsonString.rstrip(',') + "]"
    print(jsonString)

myTags = get_tags(".\\src\\template\\templates\\Family_Lawyer_Template")
write_json(myTags)

