import sys
import subprocess

message = sys.argv[1]
message = str(message)

filteredMessage = subprocess.check_output("python keywordExtractor.py '" + message + "'", shell=True)
#print filteredMessage

#print "---------------"

responses = {}

i = 0
while i < 50:
    #print str(i) + "/50"
    proverb = subprocess.check_output("python example.py", shell=True)
    proverb = proverb.split("\n")[0]

    wordCount = 0
    for word in filteredMessage:
        try: 
            proverb.split(" ").index(word)
            wordCount += 1
        except:
            continue

    relevance = wordCount / float(len(filteredMessage)) 
    #print relevance
    responses[relevance] = proverb
    #print proverb
    i += 1

#print responses
#print sorted(responses)
print responses[sorted(responses)[len(responses) - 1]]
