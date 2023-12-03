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

partnumIDs = [] #Places where partnums are, (x, y) format

def checkPartNum(xpos, ypos, lastcol, mode):
    #Formatted with y first then x
    #Mode Sum is 0, Mode Gear is 1
    global start
    global partnumIDs
    global numbers
    global adjNums
    row = start[ypos]
    char = row[xpos]
    #print(char) Debugging
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
            partnumIDs.append(str(funx) + "," + str(ypos))
            #print(partnumIDs) debugging
            if funx+1 is lastcol:
                break
            funx += 1
        #print(int(funresult)) debugging
        return int(funresult)
    return 0 + mode #0 if sum, 1 if multiply.

def checkAdj(xpos, ypos, lastrow, lastcol, mode):
    global numbers
    global partnumIDs
    global adjNums
    adjNums = 0
    funsum = 0
    gear = 1
    for y in range(-1, 2):
        if ypos + y is not -1 and ypos + y is not lastrow:
            funy = ypos+y
            for x in range(-1, 2):
                funx = xpos+x
                if xpos + x is not 0 and xpos + x is not lastcol and str(xpos+x)+","+str(ypos+y) not in partnumIDs:
                    if mode == "sum":
                        funsum += checkPartNum(funx, funy, lastcol, 0)
                    if mode == "gear":
                        gear *= checkPartNum(funx, funy, lastcol, 1)
    if mode == "sum":
        return funsum
    elif mode == "gear" and adjNums == 2:
        return gear
    else:
        return 0


def Solution(start, mode):
    global numdot
    global partnumIDs
    partnumIDs = []
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
            if char not in numdot and mode is "sum":
                #It's a special character!
                result += checkAdj(xpos, ypos, lastrow, lastcol, "sum")
            elif char is "*" and mode is "gear":
                #It might be a gear?
                result += checkAdj(xpos, ypos, lastrow, lastcol, "gear")
            xpos += 1
    return result

print(Solution(start, "sum"))
print(Solution(start, "gear"))
#print(partnumIDs) Debugging
