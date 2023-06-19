import re
with open('4.txt', 'r') as input:
    lines = input.readlines()

pattern = r'(\d+)-(\d+),(\d+)-(\d+)'
score = 0

for line in lines:
    matches = re.findall(pattern, line)
    if matches:
        a1, a2, b1, b2 = map(int, matches[0])
        #if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
        if (a1 <= b1 and a2 >= b1) or (b1 <= a1 and b2 >= a1):
            score += 1
print(score)