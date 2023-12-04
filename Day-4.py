#Uncomment debuginput when debugging

finalinput = open("input/Day-4.txt").read()
debuginput = input()
start = finalinput.split("\n")
#start = debuginput.split("\r\n")
print(start)

#So.. Umm.. figured out open().read() is a thing.
#I'll begin uploading my own inputs from now.
#Since apparently, inputs are different between users?
#I won't be providing inputs on 1-3 because I'm too lazy.

#This'll look a lot like Day 2 huh?

numofcards = []

def ofcoursetheresdoublespaces(thing):
    #single digits messed me up, whyyyy do you need to space them out 'to look neat'?
    result = []
    counter = 1
    itemnums = ""
    for nums in thing:
        counter += 1
        if nums is not " ":
            itemnums += nums
        if counter == 3:
            result.append(itemnums)
            counter = 0
            itemnums = ""
    return result

def gamble(winnum, yournum):
    winnings = 0
    rewards = 1
    for nums in yournum:
        if nums in winnum:
            winnings = rewards
            rewards += rewards
    #print(winnings)
    return winnings
    
def gambleEX(winnum, yournum, lastcard, cardindex, currcopy):
    global numofcards
    winnings = gamble(winnum, yournum) #Gambles
    copynum = 0
    while winnings >= 1: #I refuse the math module for logs
        winnings /= 2
        copynum += 1
    for copies in range(0, copynum):
        if cardindex is lastcard:
            break
        numofcards[cardindex] += 1*currcopy
        cardindex += 1
    return currcopy
        


def Solution(start, mode):
    global numofcards
    result = 0
    lastcard = len(start) #last index + 1
    numofcards = [1 for i in range (0, lastcard)] #start with 1 og card
    for card in start:
        cardindex = int(card.split(": ")[0].lstrip("Card").lstrip(" ")) #this looks so weird o.o
        lotterynums = card.split(": ")[1] #The actual numbers
        towinningnums = lotterynums.split(" | ")[0] #left side
        toyournums = lotterynums.split(" | ")[1] #right side
        winningnums = ofcoursetheresdoublespaces(towinningnums)
        yournums = ofcoursetheresdoublespaces(toyournums)
        #print(towinningnums, toyournums)
        #print(winningnums, yournums)
        if mode == "Part1":
            result += gamble(winningnums, yournums)
        elif mode == "Part2":
            #print(numofcards[cardindex-1])
            result += gambleEX(winningnums, yournums, lastcard, cardindex, numofcards[cardindex-1])
    return result


print(Solution(start, "Part1"))
print(Solution(start, "Part2"))
