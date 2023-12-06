import numpy
finalinput = open("input/Day-6.txt").read()
start = finalinput.split("\n")
print(start)

#I'm... totally ignoring day 5 now :AmeliaPain:
#There's only like, one formula to think about here, his feels weirdly easy.

def toList(notList, ignoreSpace):
    mem, theList, writing = "", [], False
    notList += " " #Adds a definitely not digit in case the last character is a digit
    for char in notList:
        if char.isdigit(): #Character is digit
            mem += char #Add it to memory
            writing = True #Currenly Writing
        elif writing is True: #The last digit was written
            if not ignoreSpace: #Separate the numbers
                theList.append(int(mem)) #Add number to the list
                mem, writing = "", False #Reset memory and no longer writing.
        #Its neither digit nor did we wrote one            
    if ignoreSpace: #We didn't separate the numbers
        theList.append(int(mem))
    return theList

def race(time, record):
    wins = 0
    for ms in range(1, time): #for every milisecond, minus pushing always/never
        if ms*(time-ms) > record: #Distance covered is higher than record
            wins += 1 #You win
    return wins

def Solution(start, mode):
    time = start[0].lstrip("Time:").lstrip(" ")
    dis = start[1].lstrip("Distance:").lstrip(" ")
    time = toList(time, mode)
    dis = toList(dis, mode)
    errMargin = list(map(race, time, dis))
    prodError = numpy.prod(errMargin)
    #prodError = time
    return prodError

print(Solution(start, False))
print(Solution(start, True))
