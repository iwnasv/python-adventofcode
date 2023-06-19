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
sum = sum(values_mapping[char] for char in chars)
#print(len(chars))
# must be 300
#print(sum)
