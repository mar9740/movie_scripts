import matplotlib.pyplot as plt
import csv
import numpy as np

# Start teh first figure, the one that will be used for the missclassification
plt.figure(1)
plt.ylabel("# of Occurences")
plt.xlabel("Type of word")
plt.title("Amount of occurence per word type")

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ,21 ,22,23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])
my_xticks = ['.,();:', 'CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS',
             'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM',
             'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']
plt.xticks(x, my_xticks, rotation=90)

with open('output.csv') as csvfile:
    reader = csv.reader(csvfile)
    c = 0
    for row in reader:
        if len(row) <= 2 or len(row) >= 6:
            word = ''
            type = ''
            count = 0
        elif len(row) == 4:
            word = str(row[0])+str(row[1])
            type = str(row[2])
            count = int(row[3])
        elif len(row) == 5:
            word = ','
            type = ','
            count = int(row[4])
        else:
            word = str(row[0]).replace("\'", "")
            type = str(row[1]).replace("\'", "")
            count = int(row[2])

        #print(word, type, count)

        if not count == 0:
            place = 0
            for item in my_xticks:
                if str(item).strip() == str(type).strip():
                    place = my_xticks.index(item)
            plt.plot(place, count, marker='.', color='#800080')

plt.show()
