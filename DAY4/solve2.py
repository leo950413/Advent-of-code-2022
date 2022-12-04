with open("input.txt") as f:
    
    content = f.read().splitlines()
    s = 0
    
    for line in content:
        
        a,b = line.split(",")
        a1,a2 = a.split("-")
        b1,b2 = b.split("-")
        if int(b1) > int(a1):
            t1,t2 = a1,a2
            a1,a2 = b1,b2
            b1,b2 = t1,t2
        
        if int(b2) >= int(a1):
            
            s += 1
            
    print(s)