def get_priority(chr):
    if chr.isupper():   
        return ord(chr) - 38
    else:
        return ord(chr) - 96
    
with open("input.txt") as f:
    
    content = f.read().splitlines()
    
    line_lst = []
    s = 0
    for lines in content:
        if len(line_lst) == 2: 
            line_lst.append(lines)
            same_lst = []
            
            for c in line_lst[0]:
                if c not in same_lst:
                    same_lst.append(c)

            n1 = []

            for c in line_lst[1]:
                if c in same_lst and c not in n1:
                   n1.append(c)
                   
            n2 = []
            
            for c in line_lst[2]:
                if c in n1 and c not in n2:
                   n2.append(c)
                   
            s += get_priority(n2[0])
            line_lst = []
            
        else: line_lst.append(lines)
        
print(s)