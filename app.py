import re

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

print ("--------------------------------------------------------------------------------------------")
print ("Amount of parsed lines " + str(counter))
print ("--------------------------------------------------------------------------------------------")
for element in tempList:
    print element

print ("--------------------------------------------------------------------------------------------")

    # DDOS Give Aways
# same IP -> Multiple Ports