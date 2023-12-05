#Uncomment debuginput when debugging

finalinput = open("input/Day-5.txt").read()
#debuginput = input()
start = finalinput.split("\n")
#start = debuginput.split("\r\n")
print(start)

#oh dear, a puzzle that uses map as a word.
#maybe a good time to teach myself whatever a map is?
#nah, lets do some good ol array actions

#no way in hell I'm improving this one, no prime.
#PS, this has no part 2 solution. I am doing it, rest assured, problem: hella stuck.

def translate(source, guide):
    counter, mem, translation, frange = 0, [], [], []
    for num in guide:
        mem.append(int(num)) #save the number
        #is it the third number?
        if counter is 2:
            #minimum source, maximum source, shift.
            frange.append([mem[1], mem[1]+mem[2], mem[0]-mem[1]])
            counter, mem = -1, [] #reset everything
        counter += 1
    #print(rangesrc)
    #print(source)
    for john in source: #can't think of names
        #is thing inbetween the range of any maps?
        john = int(john)
        shift = 0
        for alex in frange:
            if john >= alex[0] and john < alex[1]:
                shift = alex[2]
        #print(john, alex)
        translation.append(john + shift)
    return translation

def Solution(start):
    #Reading the input
    maps = " ".join(start).split("  ")
    seeds = start[0].lstrip("seeds: ").split(" ") #Always in the 1st line
    #Map order : seed-soil-fertilizer-water-light-temperature-humidity-location
    soilmap = maps[1].lstrip("seeds-to-soil map: ").split(" ")
    fertmap = maps[2].lstrip("soil-to-fertilizer map: ").split(" ")
    watermap = maps[3].lstrip("fertilizer-to-water map: ").split(" ")
    lightmap = maps[4].lstrip("water-to-light map: ").split(" ")
    tempmap = maps[5].lstrip("light-to-temperature map: ").split(" ")
    humidmap = maps[6].lstrip("temperature-to-humidity map: ").split(" ")
    locmap = maps[7].lstrip("humidity-to-location map: ").split(" ")
    almanac = [soilmap, fertmap, watermap, lightmap, tempmap, humidmap, locmap]
    #print(seeds)
    #print(soilmap)
    #print(fertmap)
    #print(watermap)
    #print(lightmap)
    #print(tempmap)
    #print(humidmap)
    #print(locmap)
    for page in range(7):
        seeds = translate(seeds, almanac[page])
        #print(seeds)
    lowest = seeds[0]
    for loc in seeds:
        if loc < lowest:
            lowest = loc
    return lowest
print(Solution(start))
