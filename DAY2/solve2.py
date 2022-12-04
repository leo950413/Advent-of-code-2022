score = {"X" : 1 , "Y" : 2 , "Z" : 3}
def ans(c1,res):
   
   if res == "Y": return 3 + score[c1]
   elif res == "Z":
       if c1 == "X":
           return 6 + score["Y"]
       elif c1 == "Y":
           return 6 + score["Z"]
       else:
           return 6 + score["X"]
   else:
        if c1 == "X":
            return score["Z"]
        elif c1 == "Y":
            return score["X"]
        else:
            return score["Y"]
        
with open("input.txt") as f:
    content = f.read().splitlines()

    s = 0
    
    for line in content:
        
        c1,c2 = line.split(" ")
        c1 = chr(ord(c1) + 23)
        s += ans(c1,c2)
    
    print(s)