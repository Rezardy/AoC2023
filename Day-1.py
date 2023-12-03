#Uh oh! Python will read my inputs weird!

question = input()
start = question.split("\r\n")
#print(start)
#inputs readable now

Numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
Digits = ["zer0ero", "on1ne", "tw2wo", "thre3hree", "fou4our", "fiv5ive", "si6ix", "seve7even", "eigh8ight", "nin9ine"]
#replaces number words with the digit and part of the word to combat potential long 3-8-3-8 chains

def checkNum(fString):
    for findex in range(10):
        fString = fString.replace(Numbers[findex], Digits[findex])
    return fString

def readDigit(fString, Dir):
    #Input string, then 1 if forward, -1 if backwards
    findex = int(-0.5 + Dir/2)
    fString = checkNum(fString) #check the whole string for number-words
    fchar = fString[findex]
    while fchar.isdigit() == False:
        findex += Dir #Look at the next character
        fchar = fString[findex]
    return fchar

result = 0
for cal in start:
    first = readDigit(cal, 1)
    last = readDigit(cal, -1)
    result += int(first + last)
print(result)
