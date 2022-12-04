with open("input.txt") as f:
    
    content = f.read()
    
    num = []
    for r in content.split("\n"*2):
           
        s = 0
             
        for i in r.split("\n"):
            s += int(i)
        
        num.append(s)
    
    num.sort()
    print(num[-1],sum(num[::-1][0:3]))