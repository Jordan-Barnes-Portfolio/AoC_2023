from collections import defaultdict

lines = [line.strip() for line in open(r"day4input.txt").readlines()]

ans = 0
stuff = defaultdict(int)
for i, line in enumerate(lines):
    stuff[i] += 1
    beginning, end = line.split('|')
    num, card = beginning.split(':')
    
    nums = [int(x) for x in card.split()]
    winners = [int(x) for x in end.split()]
    
    y = len(set(nums) & set(winners))
    
    if y > 0:
        ans += 2**(y-1)
    for j in range(y):
        stuff[i+1+j] += stuff[i]
#part1         
print(ans)
#part2
print(sum(stuff.values()))

