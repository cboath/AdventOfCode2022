stacks = open("stacks.txt", "r")
lines = stacks.read().split('\n')

sequence = open("sequence.txt", "r")
lines2 = sequence.read().split('\n')

allStacks = [[],[],[],[],[],[],[],[],[]]

def getline(line):
    n = 4
    who = [line[i:i+n] for i in range(0, len(line), n)]
    for r in range(9):
        stripper = str(who[r]).replace('[','').replace(']','')
        stripped = stripper.strip()

        if stripped == '':
            j = 1 + 1
        else:
            allStacks[r].append(stripped)

for x in range(8):
    getline(lines[x])


def moveStacks(amount, fromStack, toStack):
    part2 = []
    for iter in range(int(amount)):
        crate = allStacks[int(fromStack)-1][0]
        del allStacks[int(fromStack)-1][0]
        part2.append(crate)
    allStacks[int(toStack)-1] = part2 + allStacks[int(toStack)-1]





for moveLine in lines2:
    amt = int(moveLine.split('-')[0])
    brkr = moveLine.split('-')[1]
    frm = int(brkr.split('>')[0])
    tostk = int(moveLine.split('>')[1])
    moveStacks(amt, frm, tostk)





for h in range(9):
    print(allStacks[h])