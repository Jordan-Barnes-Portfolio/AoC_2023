#conditions: 12 red, 13 green, 14 blue

with open("day2input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


numR = 0
numB = 0
numG = 0

ans = 0

for line in lines:
    
    numR = 0
    numB = 0
    numG = 0
    
    maxR, maxB, maxG = 0, 0, 0
    
    num = ""
    color = ""
    met = False
    
    for i, x in enumerate(line):
        
        if(x == ":"):
            met = True

            num = ""
            
            numR, numB, numG = 0, 0, 0
            maxR, maxB, maxG = 0, 0, 0
            
            color = ""
            
            continue
        
        elif(not met):
            continue
        

        if x.isdigit():
            num += x
            continue
        
        elif x != " " and x != ",":
            color += x
        
        if color == "red":
            numR += int(num)
            num = ""
            color = ""
            if(i == len(line)-1):
                maxR = max(numR, maxR)
                maxG = max(numG, maxG)
                maxB = max(numB, maxB)
                
                numR = 0
                numB = 0
                numG = 0
                
                num = ""
                color = ""
            continue
        
        if color == "blue":
            numB += int(num)
            num = ""
            color = ""
            if(i == len(line)-1):
                maxR = max(numR, maxR)
                maxG = max(numG, maxG)
                maxB = max(numB, maxB)
                
                numR = 0
                numB = 0
                numG = 0
                
                num = ""
                color = ""
            continue
        
        if color == "green":
            numG += int(num)
            num = ""
            color = ""
            if(i == len(line)-1):
                maxR = max(numR, maxR)
                maxG = max(numG, maxG)
                maxB = max(numB, maxB)
                
                numR = 0
                numB = 0
                numG = 0
                
                num = ""
                color = ""
            continue
        
        if x == ";":
            
            maxR = max(numR, maxR)
            maxG = max(numG, maxG)
            maxB = max(numB, maxB)
            
            numR = 0
            numB = 0
            numG = 0
            
            num = ""
            color = ""
            
            continue
    ans += (maxR * maxB * maxG)
        

print(ans)