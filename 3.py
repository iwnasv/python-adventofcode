chars = [ ]
with open('3.txt', 'r') as input:
    for line in input:
        mid = len(line) // 2
        a = line[:mid]
        b = line[mid:]
        for char in a:
            if char in b:
                chars.append(char)
                break
lowercase_values = {chr(ord('a') + i): i + 1 for i in range(26)}
uppercase_values = {chr(ord('A') + i): i + 27 for i in range(26)}
values_mapping = {**lowercase_values, **uppercase_values}
#totalsum = sum(values_mapping[char] for char in chars)
#print(len(chars))
# must be 300
#print(sum)
badges = []
with open('3.txt', 'r') as input:
    lines = input.readlines()
for i in range(0, len(lines), 3):
    group = [line.strip() for line in lines[i:i+3]] # swsto einai apla exei anagkh to strip
    chars = set(group[0])
    for line in group[1:]: # 2nd and 3rd line
        chars.intersection_update(set(line)) # remove characters not in those lines
    a = chars.pop()
    if a != '\n':
        badges.append(a)
totalsum = sum(values_mapping[badge] for badge in badges)
print(totalsum)