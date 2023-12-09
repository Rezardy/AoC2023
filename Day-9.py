finalinput = open("input/Day-9.txt").read()
start = finalinput.split("\n")
#print(start)

def extrapolate(seq, mode):
    resSeq = [int(seq[x+1]) - int(seq[x]) for x in range(len(seq)-1)]
    isZero = [0 for x in range(len(seq))]
    exDigit = 0
    if seq != isZero:
        if mode == "Part1":
            exDigit = int(seq[-1]) + extrapolate(resSeq, mode)
        elif mode == "Part2":
            exDigit = int(seq[0]) - extrapolate(resSeq, mode)
        else: print("somethings horribly wrong")
    return exDigit

def exMap(fstr, mode):
    return extrapolate(fstr.split(" "), mode)

def Solution(start, mode):
    exDigits = list(map(exMap, start, (mode for x in range(len(start)))))
    return sum(exDigits)

print(Solution(start, "Part1"))
print(Solution(start, "Part2"))
