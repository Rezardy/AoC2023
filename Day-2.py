#Uh oh! Python will read my inputs weird!

question = input()
start = question.split("\r\n")
print(start)
#inputs readable now

def Part1(ses, gameid):
    for ses in session:
        color = ses.split(", ") #Individual colors
        possible = True
        for c in color:
            #If impossible, its not possible
            if "red" in c and int(c.strip(" red")) > 12:
                possible = False
            elif "blue" in c and int(c.strip(" blue")) > 14:
                possible = False
            elif "green" in c and int(c.strip(" green")) > 13:
                possible = False
        if not possible:
            return 0
    return int(gameid)

def Part2(ses):
    red, blue, green = 0, 0, 0
    for ses in session:
        color = ses.split(", ") #Individual colors
        for c in color:
            #If there's more, update most.
            if "red" in c:
                if int(c.strip(" red")) > red:
                    red = int(c.strip(" red"))
            elif "blue" in c:
                if int(c.strip(" blue")) > blue:
                    blue = int(c.strip(" blue"))
            elif "green" in c:
                if int(c.strip(" green")) > green:
                    green = int(c.strip(" green"))
    return red * blue * green
    
p1res, p2res = 0, 0
for game in start:
    game = game.split(": ")
    gameid = game[0].split(" ")[1] #GameID
    session = game[1].split("; ") #Sessions
    p1res += Part1(session, gameid) #Less clutter
    p2res += Part2(session) #Less clutter
print(p1res, p2res)
