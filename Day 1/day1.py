import re

input = [line.strip() for line in open(r"day1input.txt").readlines()]
digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
nums = []
input_numbered = []

def make_numbers(string):
    nums = []
    return_numbers = []
    for num, digit in enumerate(digits):
        indices = [s.start() for s in re.finditer(digit, string)]
        for i in indices:
            nums.append((i, num))
    for i, char in enumerate(string):
        if char.isdigit():
            nums.append((i, int(char)))
    for pair in sorted(nums):
        return_numbers.append(pair[1])
    return return_numbers
        

for line in input:
    line_numbered = make_numbers(line)
    nums.append(line_numbered[0]*10 + line_numbered[-1])
    
    
print(sum(nums))