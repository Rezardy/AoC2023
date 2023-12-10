finalinput = open("input/Day-10.txt").read()
start = finalinput.split("\n")
print(start)

#Farthest distance is just half of loop length..
#As long as I can make a system reading the pipe, shouldn't be too hard to solve.\
#| - L J 7 F . S

#Checks what type of pipe it is.
#Checks the pipe connecting thats not the beginning
#Repeat above until it connects to S
#In the process add up how long it is

#Coord should be [x, y]
#Usage of coord should be for area[coord[1]][coord[0]]
#Shouldn't worry about oob, since it's one big loop without branches.
#My main worry should be S accidentally searching for a pipe that it's not connecting to

UP = ["L", "J", "|"]
DOWN = ["7", "F", "|"]
LEFT = ["7", "J", "-"]
RIGHT = ["L", "F", "-"]
dirs = ["Up", "Down", "Left", "Right"]

def checkFor(this, inhere):
    y, x = 0, 0
    for row in inhere:
        if this in row:
            for char in row:
                if char == this:
                    return x, y
                x += 1
        y += 1
    print("Something's up")
    return 0

def pipeScan(coord, area, begin):
    global UP
    global DOWN
    global LEFT
    global RIGHT
    global dirs
    pipeType = area[coord[1]][coord[0]]
    test = False
    if pipeType == "S" and begin not in dirs:
        if area[coord[1]+1][coord[0]] in UP:
            check = [coord[0], coord[1]+1]
            dirfrom = "Up"
        elif area[coord[1]-1][coord[0]] in DOWN:
            check = [coord[0], coord[1]-1]
            dirfrom = "Down"
        elif area[coord[1]][coord[0]-1] in LEFT:
            check = [coord[0]-1, coord[1]]
            dirfrom = "Left"
        elif area[coord[1]][coord[0]+1] in RIGHT:
            check = [coord[0]+1, coord[1]]
            dirfrom = "Right"
        else:
            print("Something's up")
            return 0
    elif pipeType in UP and begin != "Up":
        check = [coord[0], coord[1]-1]
        dirfrom = "Down"
    elif pipeType in DOWN and begin != "Down":
        check = [coord[0], coord[1]+1]
        dirfrom = "Up"
    elif pipeType in LEFT and begin != "Left":
        check = [coord[0]-1, coord[1]]
        dirfrom = "Right"
    elif pipeType in RIGHT and begin != "Right":
        check = [coord[0]+1, coord[1]]
        dirfrom = "Left"
    elif pipeType == "S":
        return [0, 0], "dirfrom", True
    else:
        check = [0, 0]
        dirfrom = "dirfrom"
        test = True
        print("Something's up")
    #print(pipeType)
    return check, dirfrom, test

def Solution(start):
    sCoord = checkFor("S", start)
    start = [list(start[x]) for x in range(len(start))]
    stop = False
    print(sCoord)
    mem = pipeScan(sCoord, start, "a",)
    lenPipe = -1
    while not stop:
        #print(mem)
        check = pipeScan(mem[0], start, mem[1])
        lenPipe += 1
        if lenPipe > 99999 or mem[2] == True:
            stop = True
        mem = check

    return lenPipe/2

print(Solution(start))
