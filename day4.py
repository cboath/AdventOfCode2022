strategy = open("clean.txt", "r")
lines = strategy.read().split('\n')
score = 0

for line in lines:
    cleaner = line.split(',')
    cleanerA = cleaner[0].split('-')
    cleanerB = cleaner[1].split('-')

    cleaner1 = int(cleanerA[0])
    cleaner2 = int(cleanerA[1])
    cleaner3 = int(cleanerB[0])
    cleaner4 = int(cleanerB[1])

    if (((cleaner1 < cleaner3) and (cleaner2 < cleaner3)) or ((cleaner1 > cleaner4) and (cleaner2 > cleaner3))) or (((cleaner3 < cleaner1) and (cleaner4 < cleaner1)) or ((cleaner3 > cleaner2) and (cleaner4 > cleaner2))):
        print('a', line)
        score += 1

    # if ((cleaner1 >= cleaner3) and (cleaner2 <= cleaner4)):
    #     print('Really? ', cleaner1, cleaner3)
    #     print('b', line)
    #     score += 1

print(score)

print(1000 - 185)