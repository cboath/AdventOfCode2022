strategy = open("rucksack.txt", "r")
lines = strategy.read().split('\n')
score = 0

matches = []

first = 0
second = 1
third = 2

def compareTwoBags(a, b):
    staging = []
    for x in a:
        for y in b:
            if x == y:
                staging.append(x)
                break
    return staging
    




# for x in range(1):
#     for char1 in lines[first]:
#         firstMatch = False
#         for char2 in lines[second]:
#             mightitmatch = ''
#             secondMatch = False
#             for char3 in lines[third]:
#                 print('1' + char1)
#                 print('2' + char2)
#                 print('3' + char3)
#                 if char2 == char3:
#                     mightitmatch = char2
#                     secondMatch = True
#                     break
#             print('WHY!!: ' + char2)
#             # if secondMatch == True:
#             #     break
#         print('Hi: ' + mightitmatch)
#         if char1 == mightitmatch:
#             matches.append(char1)
#         print('Char1func: ' + char1)
#     first += 3
#     second += 3
#     third += 3

# print(matches)

for q in range(100):

        
    playin = compareTwoBags(lines[second], lines[third])

    perhaps = compareTwoBags(playin, lines[first])
    
    matches.append(perhaps[0])

    print(perhaps)
    first += 3
    second += 3
    third += 3


def calcscore(letter):
    setrec = ord(letter)%32
    if letter.isupper():
        setrec += 26
    return setrec

for match in matches:
    newdscore = calcscore(match)
    score += newdscore

print(score)