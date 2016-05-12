import string
#Read in a string
s = str(open("input/input00.txt").read())
l = len(s)

#Calculate total possible substrings and subtrings that start with a vowel
Total = sum([l- i for i in range(l)])
Kscore = sum([l-i if s[i] in ['A','E','I','O','U'] else 0 for i in range(l)])

#If it's not a draw, print the winners score (fraction of total)
if Kscore != Total / 2:
    print('Kevin ' + str(Kscore) if Kscore > Total - Kscore else 'Stuart ' + str(Total - Kscore) )
else:
    print('Draw')