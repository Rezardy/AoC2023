from numpy import prod

finalinput = open("input/Day-6.txt").read()
start = finalinput.split("\n")
print(start)

#This code is technically longer than the original
#But, it didn't lag, so I count it as an upgrade

def toList(notList, ignoreSpace):
    mem, theList, writing = "", [], False
    for char in notList:
        if char.isdigit(): #Character is digit
            mem += char #Add it to memory
            writing = True #Currenly Writing
        elif writing is True and not ignoreSpace: #The last char was digit
            theList.append(int(mem)) #Add number to the list
            mem, writing = "", False #Reset memory and no longer writing.
    theList.append(int(mem)) #The last digit is added
    return theList

def race(time, record):
    wins = int("".join(["9" for i in range(len(str(time)))]))
    for nth in range(len(str(time))-1, -1, -1): #from leftmost number of time
        for i in range(9): #this is just the original with extra steps..
            if wins * (time-wins) > record: #it beats the record
                if nth is not 0: #unless it's the 1s digits.
                    wins += pow(10, nth) #add a '1' to borrow from
                break #go to the next digits place
            wins -= pow(10, nth) #try lower
    wins = wins-(time-wins)+1 #all numbers between highest and lowest
    return wins

def Solution(start, mode):
    time = toList(start[0].lstrip("Time:").lstrip(" "), mode)
    dis = toList(start[1].lstrip("Distance:").lstrip(" "), mode)
    prodError = prod(list(map(race, time, dis))) #I know how to map!!
    return prodError

print(Solution(start, False), Solution(start, True))
