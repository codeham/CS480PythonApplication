import re
import json
import appbackend

categorylist = ['date', 'time', 'sourceIP', 'destinationIP', 'sourcePort', 'destinationPort']
# Pattern Order:
# Date, Time, Source IP, Destination IP, Source Port, Destination Port
patterns = [r'^[A-Z][a-z]*\s\d*', r'[0-9][0-9]\b:\b[0-9][0-9]\b:\b[0-9][0-9]',
            r'\bSRC=\b[0-9]+(?:\.[0-9]+){3}', r'\bDST=\b[0-9]+(?:\.[0-9]+){3}',
            r'\bSPT=\b[0-9]*\s', r'\bDPT=\b[0-9]*\s']

# Joining(concatenating) full pattern with OR operator for better efficieny
pattern = "|".join(patterns)
counter = 0

def printList(temp):
    print ("--------------------------------------------------------------------------------------------")
    print ("Amount of parsed lines " + str(counter))
    print ("--------------------------------------------------------------------------------------------")
    for element in temp:
        print element
    print ("--------------------------------------------------------------------------------------------")

def listtojson(temp):
    dict_items = {}
    index = 0

    for item in categorylist:
        dict_items[item] = temp[index]
        index += 1

    json_string = json.dumps(dict_items, indent=2)
    appbackend.jsontodb(json_string)
    # dictionary -> json string
    # index json string to elastic database
def trimlist(mylist):
    index = 0
    while index < len(mylist):
        mylist[index] = re.sub(r'[A-Z]*=', "", mylist[index])
        index += 1
    return mylist

with open("log.txt") as fn:
    # temp = []
    for line in fn.readlines():
        temp = []
        temp.extend(re.findall(pattern, line))
        listtojson(trimlist(temp))
        counter += 1

# total lines parsed in file
print "Total Count:" + str(counter)
print appbackend.printtest()
print appbackend.r.content
# DDOS Give Aways
# same IP -> Multiple Ports
