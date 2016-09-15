import sys

sentenceToAnalyze = str(sys.argv[1]).lower()

articles = ["the", "a", "an", "some", "this", "those", "that"]

prepositions = ["abeam", "aboard", "about", "bout", "abroad", "across", "after", "against", "along", "alongside", "amid", "amidst", "among", "around", "as", "at", "before", "behind", "below", "beneath", "beside", "besides", "between", "beyond", "but", "by", "circa", "despite", "down", "during", "except", "for", "from", "in", "inside", "into", "like", "minus", "near", "notwithstanding", "of", "off", "on", "onto", "opposite", "out", "outside", "over", "past", "post", "since", "than", "through", "throughout", "to", "toward", "towards", "under", "underneath", "unlike", "until", "til", "till", "up", "upon", "upside", "versus", "with", "without"]

pronouns = ["i", "me", "you", "she", "her", "he", "him", "it", "we", "us", "they", "them"]

possessivePronouns = ["my", "mine", "your", "yours", "her", "hers", "his", "our", "ours", "their", "theirs"]

copula = ["am", "are", "is", "was", "were", "been", "look like", "will be", "will look"]

transitiveVerb = ["have", "has", "had", "will", "have had", "had had", "has had"]

compositedPrepositions = ["according to", "adjacent to", "ahead of", "apart from", "as for", "as of", "as per", "as regards", "aside from", "astern of", "back to", "because of", "close to", "due to", "except for", "far from", "inside of", "instead of", "left of", "near to", "next to", "opposite of", "opposite to", "out from", "out of", "outside of", "owing to", "prior to", "pursuant to", "pursuant to", "rather than", "regardless of", "right of", "subsequent to", "such as", "thanks to", "up to"]

prepositionalPhrases = ["as far as", "as opposed to", "as soon as", "as well as", "at the behest of", "by means of", "by virtue of", "for the sake of", "in accordance with", "in addition to", "in case of", "in front of", "in lieu of", "in order to", "in place of", "in point of", "in spite of", "on account of", "on behalf of", "on top of", "with regard to", "with respect to", "with a view to"]

curseWords = ["arse", "ass", "asshole", "bastard", "bitch", "bloody", "bollocks", "child-fucker", "motherfucker", "mother-fucker", "crap", "cunt", "damn", "fuck", "goddamn", "holy shit", "holy fuck", "shit", "shit ass", "shitass", "son of a bitch", "son of a whore", "whore", "douche", "douchebag", "fag", "faggot", "dick", "bang", "tits", "titties", "blowjob", "blow", "fuckboy"]

filters = articles + pronouns + possessivePronouns + copula + transitiveVerb + prepositions + compositedPrepositions + prepositionalPhrases

print "analyzing " + sentenceToAnalyze

def checkForCurseWords(a):
    i = 0
    presenceOfCurseWord = 0
    while i < len(curseWords):
        #print "checked " + str(i) + "/" + str(len(curseWords))
        try: 
            a.index(curseWords[i])
            #print curseWords[i] + " present"
            i = len(curseWords)
            presenceOfCurseWord = 1
        except:
            #print curseWords[i] + " not here"
            i += 1
    return presenceOfCurseWord

def extractKeyWords(a):
    splitList = a.split(" ")
    for word in filters:
        try: 
            splitList.index(word)
            splitList.pop(splitList.index(word))
        except:
            continue
    return splitList

if checkForCurseWords(sentenceToAnalyze) == 0:
    print "------------------"
    print "moving forward"
    print extractKeyWords(sentenceToAnalyze)
else:
    print "done"
