import os
import csv
from collections import Counter


dirname=os.path.dirname
budgetDataPath = os.path.join(dirname(__file__), "Resources", "election_data.csv")

polls = dict()

with open(budgetDataPath, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
   
    for row in reader:
        key = row['Voter ID']
        polls[key] = (row['Candidate'])

voteCount = len(polls)

khanCount = sum( k == 'Khan' for k in polls.values())
khanPercent = (khanCount / voteCount) * 100

corrCount = sum( c == 'Correy' for c in polls.values())
corrPercent = (corrCount / voteCount) * 100

liCount = sum( l == 'Li' for l in polls.values())
liPercent = (liCount / voteCount) * 100

toolCount = sum( o == 'O\'Tooley' for o in polls.values())
toolPercent = (toolCount / voteCount) * 100

voterDict = {'Khan' : khanCount, 'Correy' : corrCount, 'Li' : liCount, 'O\'Tooley' : toolCount }
winnerKey = max(voterDict, key=voterDict.get)


print('Election Results\n-------------------------\nTotal Votes: ' + str(voteCount) + '\n-------------------------\nKhan: ' + str(round(khanPercent,3)) + '% (' + str(khanCount) + ')\nCorrey: ' + str(round(corrPercent,3)) + '% (' + str(corrCount) + ')\nLi: ' + str(round(liPercent,3)) + '% (' + str(liCount) + ')\nO\'Tooley: ' + str(round(toolPercent,3)) + '% (' + str(toolCount) + ')\n-------------------------\nWinner: ' + winnerKey + '\n-------------------------')

with open('Election Results.csv','w') as f:
    print('Election Results\n-------------------------\nTotal Votes: ' + str(voteCount) + '\n-------------------------\nKhan: ' + str(round(khanPercent,3)) + '% (' + str(khanCount) + ')\nCorrey: ' + str(round(corrPercent,3)) + '% (' + str(corrCount) + ')\nLi: ' + str(round(liPercent,3)) + '% (' + str(liCount) + ')\nO\'Tooley: ' + str(round(toolPercent,3)) + '% (' + str(toolCount) + ')\n-------------------------\nWinner: ' + winnerKey + '\n-------------------------')
