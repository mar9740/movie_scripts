# Parse the text files into 1 file
import csv, os
import textmining
import nltk
from nltk.corpus import treebank
from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
import collections
import string

def ily(tokens):
    ilyCount = 0
    for i in range(len(tokens)):
        if tokens[i].lower().strip() == 'i':
            if tokens[i+1].lower().strip() == 'love':
                if tokens[i+2].lower().strip() == 'you' or tokens[i+2].lower().strip() == 'you.':
                    ilyCount += 1
    return ilyCount

def omg(tokens):
    omgCount = 0
    for i in range(len(tokens)):
        if tokens[i].lower().strip() == 'oh':
            if tokens[i+1].lower().strip() == 'my':
                if tokens[i+2].lower().strip() == 'god' or tokens[i+2].lower().strip() == 'god.' or tokens[i+2].lower().strip() == 'god!' or tokens[i+2].lower().strip() == 'god,':
                    omgCount += 1
    return omgCount

def ybr(tokens):
    ybrCount = 0
    for i in range(len(tokens)):
        if tokens[i].lower().strip() == 'you':
            if tokens[i+1].lower().strip() == 'better':
                if tokens[i+2].lower().strip() == 'run' or tokens[i+2].lower().strip() == 'run.' or tokens[i+2].lower().strip() == 'run!' or tokens[i+2].lower().strip() == 'run,':
                    ybrCount += 1
    return ybrCount

def on(tokens):
    onCount = 0
    for i in range(len(tokens)):
        if tokens[i].lower().strip() == 'oh' or tokens[i].lower().strip() == 'oh,' or tokens[i].lower().strip() == 'oh.':
            if tokens[i+1].lower().strip() == 'no' or tokens[i+1].lower().strip() == 'no.' or tokens[i+1].lower().strip() == 'no!' or tokens[i+1].lower().strip() == 'no,':
                onCount += 1
    return onCount

def getLengths(tokens):
    notletter = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    over7 = 0
    for i in range(len(tokens)):
        if len(tokens[i]) == 1 and str.isalpha(tokens[i]):
            one += 1
        elif len(tokens[i]) == 1 and not str.isalpha(tokens[i]):
            notletter += 1
        elif len(tokens[i]) == 2:
            two += 1
        elif len(tokens[i]) == 3:
            three += 1
        elif len(tokens[i]) == 4:
            four += 1
        elif len(tokens[i]) == 5:
            five += 1
        elif len(tokens[i]) == 6:
            six += 1
        elif len(tokens[i]) >= 7:
            over7 += 1

    characterData.write("Punctuation characters: "+str(notletter)+"\n")
    characterData.write(("1 character words: "+str(one))+"\n")
    characterData.write(("2 character words: "+str(two))+"\n")
    characterData.write(("3 character words: "+str(three))+"\n")
    characterData.write(("4 character words: "+str(four))+"\n")
    characterData.write(("5 character words: "+str(five))+"\n")
    characterData.write(("6 character words: "+str(six))+"\n")
    characterData.write(("7+ character words: "+str(over7))+"\n\n")

scriptsLocation = os.getcwd()+"\scripts\\"
outputFile = open('output.csv', 'w')

characterData = open('cd.txt', 'w')

scripts = []

for filename in os.listdir(scriptsLocation):
    scripts.append(scriptsLocation+filename)

for s in scripts:
    print("Parsing file: "+s)
    tokens = []
    outputFile.write(s+"\n")
    file = open(s)
    for line in file.readlines():
        if line.strip():            # Strips away empty lines
            temptokens = nltk.word_tokenize(line)
            tokens.append(temptokens)

    tokens = [val for sublist in tokens for val in sublist]

    # Search for key phrases

    print('I love you count = '+str(ily(tokens)))
    print('Oh My God count = '+str(omg(tokens)))
    print('You better run count = '+str(ybr(tokens)))
    print('Oh no count = '+str(on(tokens)))

    characterData.write(s+"\n")
    getLengths(tokens)

    tagged_tokens = nltk.pos_tag(tokens)

    treetokens = tagged_tokens

    tagged_counter = dict(collections.Counter(tagged_tokens))

    sortedlist = sorted(tagged_counter.items(), key=lambda x: x[1], reverse=True)

    for value in sortedlist:
        outputFile.write("'"+value[0][0]+"' , '"+value[0][1]+"' , "+str(value[1])+"\n")

    outputFile.write("\n--------------------------------------------------------\n")

    print()
    # entities = nltk.chunk.ne_chunk(treetokens)

    # nltk.chunk.conlltags2tree(entities, chunk_types=['NP']).draw()



    file.close()

outputFile.close()

print('End Program')






