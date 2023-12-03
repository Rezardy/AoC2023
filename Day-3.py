#Uh oh! Python will read my inputs weird!

question = input()
start = question.split("\r\n")
print(start)
#inputs readable now

#Should I check all symbols instead of numbers?
#From a short skim.. Partnums are only ever touching 1 symbol.
#Maybe it'd be a good idea to keep track of numbers we got?

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numdot = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
adjNums = 0

#row would look like [(Row 1), (Row 2), (Row 3)]

partnumIDs = [] #Places where partnums are, (y x) format

def checkPartNum(ypos, xpos, lastcol):
    #Formatted with y first then x
    global start
    global partnumIDs
    global numbers
    row = start[ypos]
    char = row[xpos]
    #print(char) Debugging
    if char in numbers:
        #It's a new number and a unique one
        funx = xpos
        while row[funx] in numbers:
            #Look left until it's not a number or until first col
            if funx is 0:
                funx -= 1
                break
            funx -= 1
        funx += 1
        funresult = "0"
        while row[funx] in numbers:
            #Look right until it's not a number
            funresult += row[funx]
            partnumIDs.append(str(ypos) + "," + str(funx))
            #print(partnumIDs) debugging
            if funx+1 is lastcol:
                break
            funx += 1
        #print(int(funresult)) debugging
        return int(funresult)
    return 0

def checkPartNum2(ypos, xpos, lastcol):
    #Formatted with y first then x
    global start
    global partnumIDs
    global numbers
    global adjNums
    row = start[ypos]
    char = row[xpos]
    #print(char) #Debugging
    if char in numbers:
        #It's a new number and a unique one
        adjNums += 1
        funx = xpos
        while row[funx] in numbers:
            #Look left until it's not a number or until first col
            if funx is 0:
                funx -= 1
                break
            funx -= 1
        funx += 1
        funresult = "0"
        while row[funx] in numbers:
            #Look right until it's not a number
            funresult += row[funx]
            partnumIDs.append(str(ypos) + "," + str(funx))
            #print(partnumIDs) debugging
            if funx+1 is lastcol:
                break
            funx += 1
        #print(int(funresult)) #debugging
        return int(funresult)
    return 1 #this is the sole purpose of a second checknum 2, changing a 'not number' into 1 because we're dealing with multipliers, theres a smarter way, definitely, but im one hour in and pretty tired..

def checkAdj(xpos, ypos, lastrow, lastcol):
    global numbers
    global partnumIDs
    funresult = 0
    if ypos != 0:
        #Check the previous row
        
        if xpos != 0:
            #Check upper left
            if str(ypos-1) + "," + str(xpos-1) not in partnumIDs:
                funresult = checkPartNum(ypos-1, xpos-1, lastcol)

        #Check the upper middle
        if str(ypos-1) + "," + str(xpos) not in partnumIDs:
            funresult += checkPartNum(ypos-1, xpos, lastcol)

        if xpos+1 != lastcol:
            #Check upper right
            if str(ypos-1) + "," + str(xpos+1) not in partnumIDs:
                funresult += checkPartNum(ypos-1, xpos+1, lastcol)
    #---------------------------------------------------
    if xpos != 0:
        #Check middle left
        if str(ypos) + "," + str(xpos-1) not in partnumIDs:
            funresult += checkPartNum(ypos, xpos-1, lastcol)

    if xpos+1 != lastcol:
        #Check middle right
        if str(ypos) + "," + str(xpos+1) not in partnumIDs:
            funresult += checkPartNum(ypos, xpos+1, lastcol)
    #---------------------------------------------------
    if ypos+1 != lastrow:
        #Check the next row
        
        if xpos != 0:
            #Check lower left
            if str(ypos+1) + "," + str(xpos-1) not in partnumIDs:
                funresult += checkPartNum(ypos+1, xpos-1, lastcol)

        #Check the lower middle
        if str(ypos+1) + "," + str(xpos) not in partnumIDs:
            funresult += checkPartNum(ypos+1, xpos, lastcol)

        if xpos+1 != lastcol:
            #Check lower right
            if str(ypos+1) + "," + str(xpos+1) not in partnumIDs:
                funresult += checkPartNum(ypos+1, xpos+1, lastcol)
    return funresult


def checkAdj2(xpos, ypos, lastrow, lastcol):
    global numbers
    global partnumIDs
    global adjNums
    funresult = 1
    adjNums = 0
    if ypos != 0:
        #Check the previous row
        
        if xpos != 0:
            #Check upper left
            if str(ypos-1) + "," + str(xpos-1) not in partnumIDs:
                funresult *= checkPartNum2(ypos-1, xpos-1, lastcol)

        #Check the upper middle
        if str(ypos-1) + "," + str(xpos) not in partnumIDs:
            funresult *= checkPartNum2(ypos-1, xpos, lastcol)\

        if xpos+1 != lastcol:
            #Check upper right
            if str(ypos-1) + "," + str(xpos+1) not in partnumIDs:
                funresult *= checkPartNum2(ypos-1, xpos+1, lastcol)

    #---------------------------------------------------
    if xpos != 0:
        #Check middle left
        if str(ypos) + "," + str(xpos-1) not in partnumIDs:
            funresult *= checkPartNum2(ypos, xpos-1, lastcol)

    if xpos+1 != lastcol:
        #Check middle right
        if str(ypos) + "," + str(xpos+1) not in partnumIDs:
            funresult *= checkPartNum2(ypos, xpos+1, lastcol)
    #---------------------------------------------------
    if ypos+1 != lastrow:
        #Check the next row
        
        if xpos != 0:
            #Check lower left
            if str(ypos+1) + "," + str(xpos-1) not in partnumIDs:
                funresult *= checkPartNum2(ypos+1, xpos-1, lastcol)

        #Check the lower middle
        if str(ypos+1) + "," + str(xpos) not in partnumIDs:
            funresult *= checkPartNum2(ypos+1, xpos, lastcol)

        if xpos+1 != lastcol:
            #Check lower right
            if str(ypos+1) + "," + str(xpos+1) not in partnumIDs:
                funresult *= checkPartNum2(ypos+1, xpos+1, lastcol)
    if adjNums == 2:
        return funresult
    else:
        return 0

def Part1(start):
    global numdot
    isfirstrow = True #starts on the first row
    islastrow = False #doesn't start on last row
    lenCheck = 0 #Keep track of what row we're in
    result = 0
    lastrow = len(start)
    lastcol = len(start[0])
    for row in start:
        lenCheck += 1
        xpos = 0 #Set to leftmost character position
        ypos = lenCheck-1 #Indexing purposes
        if lenCheck == lastrow:
            #It's the last row
            islastrow = True
        for char in row:
            if char not in numdot:
                #It's a special character!
                result += checkAdj(xpos, ypos, lastrow, lastcol)
            xpos += 1
    return result

    
def Part2(start):
    global numdot
    isfirstrow = True #starts on the first row
    islastrow = False #doesn't start on last row
    lenCheck = 0 #Keep track of what row we're in
    result = 0
    lastrow = len(start)
    lastcol = len(start[0])
    for row in start:
        lenCheck += 1
        xpos = 0 #Set to leftmost character position
        ypos = lenCheck-1 #Indexing purposes
        if lenCheck == lastrow:
            #It's the last row
            islastrow = True
        for char in row:
            if char is "*":
                #It might be a gear?
                result += checkAdj2(xpos, ypos, lastrow, lastcol)
            xpos += 1
    return result

print(Part1(start))
partnumIDs = [] #Reset
print(Part2(start))
#print(partnumIDs) #Debugging
#Programmer's note: I am so tired................................. :LynxShivers:
