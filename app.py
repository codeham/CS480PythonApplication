import re
import json

tempList = []
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
    dict_items['date'] = tempList[0]
    dict_items['time'] = tempList[1]
    dict_items['sourceIP'] = tempList[2]
    dict_items['destinationIP'] = tempList[3]
    dict_items['sourcePort'] = tempList[4]
    dict_items['destinationPort'] = tempList[5]
    print dict_items
    dict_items.clear()


with open("log.txt") as fn:
    for line in fn.readlines():
        tempList.extend(re.findall(pattern, line))
        listtojson(tempList)
        del tempList[:]
        counter += 1
    # print tempList
    # printList(tempList)





# DDOS Give Aways
# same IP -> Multiple Ports