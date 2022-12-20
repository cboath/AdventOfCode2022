sekrits = open('sekrit.txt', "r")
blarg = sekrits.read()

def doesItMatch(string):
    print(string)
    first = list(string); first.sort()
    second = list(set(string)); second.sort()
    return first == second

def runTheNumbers(string, offset):
    for x in range(len(string)):
        if doesItMatch(blarg[x:x + offset]):
            return x + offset

ans1 = runTheNumbers(blarg, 4)
ans2 = runTheNumbers(blarg, 14)

print('Answer 1:', ans1)
print('Answer 2:', ans2) 