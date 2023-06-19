score = 0
with open('2.txt', 'r') as input:
    for line in input:
        if (line[2] == 'X'):
            score += 1
            if (line[0] == 'A'):
                score += 3
            elif (line[0] == 'C'):
                score += 6
        if (line[2] == 'Y'):
            score += 2
            if (line[0] == 'B'):
                score += 3
            elif (line[0] == 'A'):
                score += 6
        if (line[2] == 'Z'):
            score += 3
            if (line[0] == 'C'):
                score += 3
            elif (line[0] == 'B'):
                score += 6
#print(score)
# part 2
score = 0
with open('2.txt', 'r') as input:
    for line in input:
        if (line[2] == 'X'):
            match line[0]:
                case 'A':
                    score += 3
                case 'B':
                    score += 1
                case 'C':
                    score += 2
        if (line[2] == 'Y'):
            score += 3
            match line[0]:
                case 'A':
                    score += 1
                case 'B':
                    score += 2
                case 'C':
                    score += 3
        if (line[2] == 'Z'):
            score += 6
            match line[0]:
                case 'A':
                    score += 2
                case 'B':
                    score += 3
                case 'C':
                    score += 1
print(score)