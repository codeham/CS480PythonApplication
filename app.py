import re
from texttable import Texttable

date, time, srcIp, destIp, sourcePort, destPort = list(), list(), list(), list(), list(), list()
tempList = []
patterns = [r'^[A-Z][a-z]*\s\d*', r'\bDPT=\b[0-9]*\s', r'[0-9][0-9]\b:\b[0-9][0-9]\b:\b[0-9][0-9]',
            r'\bSRC=\b[0-9]+(?:\.[0-9]+){3}', r'\bSRC=\b[0-9]+(?:\.[0-9]+){3}', r'\bDST=\b[0-9]+(?:\.[0-9]+){3}',
            r'\bSPT=\b[0-9]*\s', r'\bDPT=\b[0-9]*\s']
pattern = "|".join(patterns)

counter = 0
with open("log.txt") as fn:
    for line in fn.readlines():
        tempList.append(re.findall(pattern, line))
        counter += 1

print ("Amount of parsed lines " + str(counter))
print ("--------------------------------------------------------------------------------------------")
for element in tempList:
    print element

# t = Texttable()
# t.add_row([['All Content'], [tempList]])
# print ("Amount of lines " + str(counter))
# print t.draw()




# date.append(re.findall(r'^[A-Z][a-z]*\s\d*', line))
# time.append(re.findall(r'[0-9][0-9]\b:\b[0-9][0-9]\b:\b[0-9][0-9]', line))
# srcIp.append(re.findall(r'\bSRC=\b[0-9]+(?:\.[0-9]+){3}', line))
# destIp.append(re.findall(r'\bDST=\b[0-9]+(?:\.[0-9]+){3}', line))
# sourcePort.append(re.findall(r'\bSPT=\b[0-9]*\s', line))
# destPort.append(re.findall(r'\bDPT=\b[0-9]*\s', line))
# json_string = '{"date": , "time": , "sourceIP": , "destinationIP": , "sourcePort":, "destinationPort": }'

# t = Texttable()
# t.add_rows([['Date', 'Time', 'Source IP', 'Destination IP', 'Source Port', 'Destination Port'],
#             [date, time, srcIp, destIp, sourcePort, destPort]])
# t.add_rows([['ALL'], [tempList]])
# print t.draw()

# DDOS Give Aways
# same IP -> Multiple Ports