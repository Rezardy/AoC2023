#Uh oh! Python will read my inputs weird!

question = input()
start = question.split("\r\n")
#print(start)
#inputs readable now

Numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
Digits = ["zer0ero", "on1ne", "tw2wo", "thre3hree", "fou4our", "fiv5ive", "si6ix", "seve7even", "eigh8ight", "nin9ine"]
#each number possibility only shares at most 1 character
#zer[o]ne
#on[e]ight
#eigh[t]wo
#tw[o]ne
#eigh[t]hree
#thre[e]ight
#fiv[e]ight
#seve[n]ine
#nin[e]ight

def checkNum(fString):
    for findex in range(10):
        fString = fString.replace(Numbers[findex], Digits[findex])
    return fString

def readDigit(fString, Dir):
    #Input string, then 1 if forward, -1 if backwards
    findex = int(-0.5 + Dir/2)
    fString = checkNum(fString)
    fchar = fString[findex]
    #print(fString)
    while fchar.isdigit() == False:
        findex += Dir #Look at the next character
        fchar = fString[findex]
    return fchar

result = 0
for cal in start:
    first = readDigit(cal, 1)
    last = readDigit(cal, -1)
    #print(cal)
    #print(first, last)
    result += int(first + last)
print(result)
