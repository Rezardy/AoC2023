finalinput = open("input/Day-7.txt").read()
start = finalinput.split("\n")
#start = ["JJJJJ 20"]
print(start)

#Hand strength is based on Type, then the individual cards..

#Non-digits, 10-14
symbpk = ["T", "J", "Q", "K", "A"]

#I want to first know what type of hand it is
#It'll probably just be a simple integer, 0-6 (High-OP-TP-3K-FH-4K-5K)
#For the individual cards, it should be enough to join them as a single int.
#A translated hand should look like [type, strength, bid]
#Or, can I get away with type becoming multiples of 10 000 000 000?

def handStr(hand, Joker):
    global symbpk
    digitsplace = 100000000
    strength = 0
    mem1, mem2, mem3, mem4 = "", "", "", "" #What cards were already drawn?
    J, D, P = 0, 0, 0 #Jokers, Cards that doesn't have a unique label, One Pairs.
    stren = 0 #High Card default
    for char in hand:
        if char is "J" and Joker: #It's a joker!!
            char = "1" #Ace that would've been 1 is actually 14, so this is fine
            J += 1 #Count up the Jokers
        if char not in mem1 and char is not "1":
            mem1 += str(char)
        elif char not in mem2 and char is not "1":
            mem2 += str(char)
            D += 1 
            P += 1 #That's a pair
        elif char not in mem3 and char is not "1":
            mem3 += str(char)
            D += 1
            P -= 1 #No, wait, that's not a pair
        elif char not in mem4 and char is not "1":
            mem4 += str(char)
            D += 1
        elif char is not "1": #5 of a kind, Strength 6.
            D += 1
        
        if char in symbpk: #translate T, J, Q, K, A
            char = 10 + symbpk.index(char)
        strength += int(char)*int(digitsplace)
        digitsplace /= 100

        char = str(char)

    if Joker: #Count up Jokers
        while J > 0:
            if P == 1 and D == 1: #It's a one pair
                P -= 1
                D += 1 #Make it a Three of a Kind
            elif P == 2 and D == 2: #It's a Two Pair
                P -= 1
                D += 1 #Make it a Full House
            elif D > 0: #It's a Three/Four of a Kind
                D += 1 #Make it a Four/Five of a Kind
            else: #It's a High Card
                P += 1
                D += 1 #Make it a One Pair
            J -= 1

    if P == 1: #Check the typing strength
        if D == 1:
           stren = 10000000000
        else:
            stren = 40000000000
    elif P == 2:
        stren = 20000000000
    elif D > 0:
        stren = 30000000000
        if D == 3:
            stren = 50000000000
        elif D > 3:
            stren = 60000000000

    strength += stren #add up the typing strength
    return strength, stren/10000000000

def split(fstr, mode):
    result = fstr.split(" ")
    result[0] = handStr(result[0], mode)[0]
    return result

def sortKey(hand):
    return hand[0]

def Solution(start, mode):
    hands = list(map(split, start, [mode for x in range(len(start))]))
    hands.sort(key=sortKey) #Sort from weakest
    rank, winnings = 1, 0 #Rank start at 1
    for hand in hands:
        winnings += int(hand[1]) * rank #Bid multiplied by rank
        rank += 1
    return winnings

print(Solution(start, False))
print(Solution(start, True))
