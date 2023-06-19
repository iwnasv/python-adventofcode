with open('1.txt', 'r') as input:
    lines = input.readlines()

top = [ 0, 0, 0 ]
elf = 0
for line in lines:
    if line != "\n":
        elf += int(line.strip())
    else:
        if elf > top[2]:
            top.pop()
            top.append(elf)
            top.sort(reverse=True)
        elf = 0
    
print(sum(top))