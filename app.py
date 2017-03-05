import re
import json

tempList = []
categorylist = ['date', 'time', 'sourceIP', 'destinationIP', 'sourcePort', 'destinationPort']
# Pattern Order:
# Date, Time, Source IP, Destination IP, Source Port, Destination Port
patterns = [r'^[A-Z][a-z]*\s\d*', r'[0-9][0-9]\b:\b[0-9][0-9]\b:\b[0-9][0-9]',
            r'\bSRC=\b[0-9]+(?:\.[0-9]+){3}', r'\bDST=\b[0-9]+(?:\.[0-9]+){3}',
            r'\bSPT=\b[0-9]*\s', r'\bDPT=\b[0-9]*\s']

# Joining(concatenating) full pattern with OR operator for better efficieny
pattern = "|".join(patterns)
counter = 0

def printList(tempList):
    print ("--------------------------------------------------------------------------------------------")
    print ("Amount of parsed lines " + str(counter))
    print ("--------------------------------------------------------------------------------------------")
    for element in tempList:
        print element
    print ("--------------------------------------------------------------------------------------------")

def listtojson(templist):
    dict_items = {}
    index = 0
    
    for item in categorylist:
        dict_items[item] = tempList[index]
        index += 1

    s = json.dumps(dict_items, indent = 2)
    print s

    dict_items.clear()

def trimList(mylist):
    index = 0
    while index < len(mylist):
        mylist[index] = re.sub(r'[A-Z]*=', "", mylist[index])
        index += 1
    return mylist

with open("shortlog.txt") as fn:
    for line in fn.readlines():
        tempList.extend(re.findall(pattern, line))
        tempList = trimList(tempList)
        listtojson(tempList)
        del tempList[:]
        counter += 1
print "Total Count:" + str(counter)

# DDOS Give Aways
# same IP -> Multiple Ports
