with open("input.txt") as f:
    
    content = f.read().splitlines()
    s = 0
    for line in content:
        
        a,b = line.split(",")
        a1,a2 = a.split("-")
        b1,b2 = b.split("-")
        
        if (int(b1) <= int(a1) and int(b2) >= int(a2)) or (int(a1) <= int(b1) and int(a2) >= int(b2)):
            
            s += 1
            
    print(s)