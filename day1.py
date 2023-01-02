puzzle = open("puzzle.txt", "r")

lines = puzzle.read().split('\n')
x = 0
summed = []

for line in lines:
    if line == '':
        line = 0
    x += int(line)
    if line == 0:
        summed.append(x)
        x = 0

summed.sort(reverse=True)

print(summed)

top3 = (summed[0] + summed[1] + summed[2])

print(top3)