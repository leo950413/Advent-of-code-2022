score = {"X" : 1 , "Y" : 2 , "Z" : 3}
def ans(c1,c2):
    a = 0
    if c1 == c2: a = 3
    elif c1 == "X" and c2 == "Y":
        a = 6
    elif c1 == "Y" and c2 == "Z":
        a = 6
    elif c1 == "Z" and c2 == "X":
        a = 6
    
    return a + score[c2]

with open("input.txt") as f:
    content = f.read().splitlines()

    s = 0
    
    for line in content:
        
        c1,c2 = line.split(" ")
        c1 = chr(ord(c1) + 23)
        s += ans(c1,c2)
    
    print(s)