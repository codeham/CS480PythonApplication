import re
import json
import appbackend

# tuple that holds items that will be mapped as keys in dictionary
list_categories = ('date', 'time', 'sourceIP', 'destinationIP', 'sourcePort', 'destinationPort')

# Pattern Order:
# Date, Time, Source IP, Destination IP, Source Port, Destination Port
# regex pattern that extracts data from log file
patterns = [r'^[A-Z][a-z]*\s\d*', r'[0-9][0-9]\b:\b[0-9][0-9]\b:\b[0-9][0-9]',
            r'\bSRC=\b[0-9]+(?:\.[0-9]+){3}', r'\bDST=\b[0-9]+(?:\.[0-9]+){3}',
            r'\bSPT=\b[0-9]*', r'\bDPT=\b[0-9]*']

# joining(concatenating) full pattern with OR operator for better efficieny
pattern = "|".join(patterns)
# global counter just to count entries (can be removed later)
counter = 0

# listtojson(temp)
# takes in a list containing one data entry
# example ['Dec 23', '17:04:40', '220.135.232.97', '192.168.133.189', '22934', '23']
# then properly maps each index to a python dictionary
# dictionary is then converted to json and then sent to backend to be appended into DB
def listtojson(temp):
    dict_items = {}
    index = 0

    for item in list_categories:
        print item
        dict_items[item] = temp[index]
        index += 1

    json_string = json.dumps(dict_items, indent=2)
    appbackend.jsontodb(json_string)

# trimlist(mylist)
# strips unwanted string from the parsed data list
# using a regular expression
# example 'SRC=192.12.32.2' -> '192.12.32.2'
def trimlist(mylist):
    index = 0
    while index < len(mylist):
        mylist[index] = re.sub(r'[A-Z]*=', "", mylist[index])
        mylist[index].rstrip
        index += 1
    return mylist

# opens the log file specified in field
# iterates line by line
# during each iteration each line is parsed with a regex to extract wanted data
# list is then passed in as an argument to trimlist(temp) to trim off any unwated string..
# this returns a list data type containing formatted entries
# trimlist(temp) is passed into listtojson(list data type), which communicates with the backend module..
# to append to database
with open("log.txt") as fn:
    for line in fn.readlines():
        temp = []
        temp.extend(re.findall(pattern, line))
        listtojson(trimlist(temp))
        counter += 1

# total lines parsed in file
print "Total Count:" + str(counter)
appbackend.defineMapping()
# appbackend.search("destinationPort","23")
# print appbackend.getData()
# DDOS Give Aways
# same IP -> Multiple Ports
