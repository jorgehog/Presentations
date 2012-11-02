import sys, re

usage = "'count_words.py [options] filename word'.\
\nOptions: -i (case sensetive). -b (respect word boundaries)"

#Default values
caseSense = True
bounded = False


#Check if no CML args given:
if len(sys.argv) < 3:
    print "CML args missing."
    print "usage: %s" % usage
    sys.exit(1)


#If second last CML arg is an openable file (and that the word is present)
try:
    inFile = open(sys.argv[-2], 'r')

    #readlines is a list (split at \n). "".join merges it to a string.
    rawFile = "".join(inFile.readlines())
    inFile.close()
    
    word = sys.argv[-1]
    rawWord = word;
    
except:
    print """Error: %s could not be opened.
Second last CML arg must be a text file name.""" % sys.argv[-2]
    print "usage: %s" % usage


#Checking options
if "-i" in sys.argv[1:-2]:
    caseSense = False
    sys.argv.remove("-i")
if "-b" in sys.argv[1:-2]:
    bounded = True
    sys.argv.remove("-b")


#If anything is left between the first and the last (file) CML arg, it is not
#Recognized. (cannot be -b or -i)
if len(sys.argv[1:-2]) != 0:
    for unrecognizedArgument in sys.argv[1:-2]:
        print "Unrecognized CML arg: %s" % unrecognizedArgument
    sys.exit(1);


#Adding bounds to the word (pattern=any spacing, word, any ending)
stringOrWord = "string"
if bounded:
    stringOrWord = "word"
    word = "[\^\s]" + word + "[\s\b]"
    
#Flaging case insensitivity
if not caseSense:
    regExtObj = re.compile(word, re.IGNORECASE)
    printCase = " (case insensitive)"
else:
    regExtObj = re.compile(word)
    printCase = ""


#*.findall(#) lists all matches in # of pattern compiled in *
Nmatches = len(regExtObj.findall(rawFile))

printfArgs = (stringOrWord, rawWord, printCase, Nmatches)
print "Number of occurances of %s '%s'%s: %d" %  printfArgs
