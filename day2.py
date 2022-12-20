strategy = open("rockpaperscis.txt", "r")

lines = strategy.read().split('\n')
score = 0

for line in lines:
    match line:
        case 'A X':
            score += 3
        case 'B X':
            score += 1
        case 'C X':
            score += 2
        case 'B Y':
            score += 5
        case 'A Y':
            score += 4
        case 'C Y':
            score += 6
        case 'C Z':
            score += 7
        case 'B Z':
            score += 9 
        case 'A Z':
            score += 8

print(score)
    