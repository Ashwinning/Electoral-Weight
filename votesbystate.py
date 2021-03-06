'''
Sort votes by state from votes.txt
Data scraped from http://www.politico.com/2016-election/results/map/president
'''

candidates = [4,6,4,8,5,22,4,4,4,6,3,5,8,4,3,10,4,6,13,4,4,4,6,9,7,5,5,4,6,5,9,8,4,3,6,5,3,4,5,5,7,4,7,4,10,6,5,7,5,7,6]

votes = open("votes.txt", "r")
votesByState = open("votesbystate.txt", "w")

def ClearCommasAndReturnInt(text):
    return int(text.replace(',', ''))

votes.readline() #skip first line

for num in candidates:
    totalVotesInState = 0
    for i in range(1,num):
        totalVotesInState += ClearCommasAndReturnInt(votes.readline())
    votesByState.write(str(totalVotesInState)+'\n')
