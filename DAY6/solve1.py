with open("input.txt") as f:
    
    content = f.read()
    s = ""
    
    for cnt,i in enumerate(content):
    
        if len(s) == 4: # change it to 14 for 2nd problem
            
            t = 1
            for j in s:
                
                if(s.count(j) > 1):t = 0
            if t:
                
                print(cnt)
                break

            else:
                
                s = s[1:]
                
        s += i