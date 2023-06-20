import re
with open('4.txt', 'r') as input:
    lines = input.readlines()
input = """[D]        
[N]     [C]    
[Z] [M] [P]"""
lines = input.splitlines()
for line in lines: