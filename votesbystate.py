'''
Sort votes by state from votes.txt
Data scraped from http://www.politico.com/2016-election/results/map/president
'''

candidates = [4,6,4,8,5,22,4,4,4,6,3,5,8,4,3,10,4,6,13,4,4,4,6,9,7,5,5,4,6,5,9,8,4,3,6,5,3,4,5,5,7,4,7,4,10,6,5,7,5,7,6]

#votesFiles = open("votes.txt", "r")


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print ('Number of votes ' + str(file_len("votes.txt")))

total = 0
for num in candidates:
    total += num

print ('number of votes '+ str(total))
