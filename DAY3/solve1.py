def get_priority(chr):
    
    if chr.isupper():
        
        return ord(chr) - 38
    
    else:
        
        return ord(chr) - 96
    
with open("input.txt") as f:
    content = f.read().splitlines()
    
    h = []
    sum = 0
    
    for lines in content:
        firstpart, secondpart = lines[:len(lines)//2], lines[len(lines)//2:]
        for chr in firstpart:
            if chr not in h:
                h.append(chr)
        for chr in secondpart:
            if chr in h:
                sum += get_priority(chr)
                h = []
                

                
                
    print(sum)