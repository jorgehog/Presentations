# -*- coding: utf-8 -*-

    
import sys, re

#load entire file into a string. Convert to lower case letters.
f1 = open(sys.argv[1]); allwords = f1.read().lower(); f1.close()

max_length = 15; min_length = 5

#Recognize all words
rePattern = r"[a-zA-Z]{%d,%d}" % (min_length, max_length)
allwords = re.findall(rePattern, allwords)

texWords = ['hat', 'end', 'begin', 'equation', 'rangle', 'langle', 'right',
            'left', 'caption', 'frac', 'dagger', 'phantom', 'hline', 'sum', 
            'label', 'eq', 's', 'h', 'center', 'plain', 'split', 'textrm', 
            'tabular', 'table']

#count words
wordCount = {}
for word in allwords:
    if word not in texWords and not re.findall('.*(fmf).*', word):
        if word not in wordCount.keys():
            wordCount[word] = 1
        elif word in wordCount.keys():
            wordCount[word] += 1

#Sort scores from largest to lowest
sort = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)

#Output:
s = max_length
print sys.argv[1].ljust(len(sys.argv[1]))
print "%s: %s" % ("word".ljust(s), "n".ljust(s))     
print
for key, value in sort:
    print "%s: %s" % (key.ljust(s), str(value).ljust(s))
