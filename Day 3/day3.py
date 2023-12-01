

#if we see a symbol, we need to check around its [r, c] position for a number.

"""
Example:
    
    symbol at position [1,2]
    we must check [1,1], [1,3], [0,2], [0,3], [0,1], [2,2], [2,3], [2,1]
    so, again if position is [row 1, column 2], we check
    row 0, column 1 2 3
    row 1, column 1 3
    row 2, column 1 2 3
    [...123...
     ..%......
     .4.......]
    
    so algo would look like,
    
    symbol pos = [r, c]
    check pos = (r-1)[c-1 c c+1], (r)[c-1 c+1], (r+1)[c-1, c, c+1]
    
    edge cases:
        
            
            [..1..,
             ..%..,
             ..8..]
    
"""
inputStr = [line.strip() for line in open(r"day3input.txt").readlines()]

x = "x"*len(inputStr[0])
inputStr.insert(0, x)
inputStr.append(x)

for y in range(len(inputStr)):
    inputStr[y] = "x" + inputStr[y]
    inputStr[y] = inputStr[y] + "x"

numbers = []

def build_number(r, c):
    
    #if we see a number at r, c, we check c-1 and c+1 if its a number, if it is
    #add it to the string, and check found c +- 2 and so on
    
    number = inputStr[r][c]
    replace_l = list(inputStr[r])
    replace_l[c] = "x"
    inputStr[r] = ''.join(replace_l)
    
    
    
    counterleft, counterright = 1, 1
    
    while(True):
        
        if(inputStr[r][c-counterleft].isdigit()):
            number = inputStr[r][c-counterleft] + number
            
            replace_l = list(inputStr[r])
            replace_l[c-counterleft] = "x"
            inputStr[r] = ''.join(replace_l)
            
            counterleft+=1
            
        if(inputStr[r][c+counterright].isdigit()):
            number += inputStr[r][c+counterright]
            
            replace_l = list(inputStr[r])
            replace_l[c+counterright] = "x"
            inputStr[r] = ''.join(replace_l)
            
            counterright+=1
            
        elif(not inputStr[r][c+counterright].isdigit() and not inputStr[r][c-counterleft].isdigit()):
            numbers.append(int(number))
            break
        
 
            
def perform_check(r, c):
    
    top_middle = False
    bottom_middle = False
    #Start easy by checking sides and building from there.
    if(inputStr[r][c-1].isdigit()):
        build_number(r, c-1)
    if(inputStr[r][c+1].isdigit()):
        build_number(r, c+1)
        
    #Middles:
        #if either middle has a number, we build number out left and right
        #if neither middle has a number, we check corners to build out from their edge.
       
    if(inputStr[r-1][c].isdigit()):
        build_number(r-1, c)
        top_middle = True
    if(inputStr[r+1][c].isdigit()):
        build_number(r+1, c)
        bottom_middle = True
    
    #Corners:
        #if either middle is false, we will check that middles corners.
    
    if(not top_middle and str(inputStr[r-1][c-1]).isdigit()):
        build_number(r-1, c-1)
        perform_check(r, c)
    if(not top_middle and str(inputStr[r-1][c+1]).isdigit()):
        build_number(r-1, c+1)
        perform_check(r, c)
        
    if(not bottom_middle and str(inputStr[r+1][c-1]).isdigit()):
        build_number(r+1, c-1)
        perform_check(r, c)
    if(not bottom_middle and str(inputStr[r+1][c+1]).isdigit()):
        build_number(r+1, c+1)
        perform_check(r, c)
        
    else:
        return False
    
symbols = ['*']
ans = []
for x, r in enumerate(inputStr):
    for y, c in enumerate(r):
        if c in symbols:
            perform_check(x, y)
            if(len(numbers)<=2):
                ans.append(numbers)
                numbers = []

ansd = 0

for x in ans:
    product = 1
    if(len(x) == 1):
        continue
    for y in x:
        product*=y
    ansd += product

print(ansd)

            