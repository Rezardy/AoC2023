#fine.. I'll use the math module's log
import math

finalinput = open("input/Day-4.txt").read()
start = finalinput.split("\n")
print(start)

#I feel like I should start focusing on cleanliness instead of speed..
#I still want to speedrun, so I'll upload a separate clean code with 'Day-x Prime'

def gamble(winnum, yournum):
    numswon, winnings, rewards = 0, 0, 1
    for nums in yournum:
        if nums in winnum and nums is not "":
            winnings = rewards
            rewards += rewards
            numswon += 1
    return [winnings, numswon] #Experimented w returning arrays

#Duplicate gamble gone

def Solution(start):
    points, cardsscratched, cardindex = 0, 0, 0
    lastcard = len(start)
    numofcards = [1 for i in range (0, lastcard)]
    for card in start:
        lotterynums = card.split(": ")[1]
        winningnums = lotterynums.split(" | ")[0].split(" ")
        yournums = lotterynums.split(" | ")[1].split(" ")
        points += gamble(winningnums, yournums)[0]
        cardsscratched += numofcards[cardindex]
        numberswon = gamble(winningnums, yournums)[1]
        copyindex = cardindex+1
        for copies in range(0, numberswon):
            if copyindex is lastcard:
                break
            numofcards[copyindex] += numofcards[cardindex]
            copyindex += 1
        cardindex += 1
    return [str(points) + " Original Points", str(cardsscratched) + " Cards Scratched"]

print(Solution(start))
