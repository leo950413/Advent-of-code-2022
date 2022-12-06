with open("input.txt") as f:
    
    content = f.read().splitlines()
    ans = ""    
    arr = [[],[],[],[],[],[],[],[],[]]
    for i in content[:8]:
        x = 0
        y = 0
        for x in range(1,34,4):
            if i[x].isalpha():
                arr[x//4].append(i[x])
    for n in arr:
        n.reverse()
    
    for j in content[10:]:
        num = int(j.split("from")[0].replace("move","").replace(" ",""))
        f = int(j.split("from")[1].split("to")[0].replace(" ",""))
        t = int(j.split("from")[1].split("to")[1].replace(" ",""))
        idx = len(arr[f-1])-num
        target = arr[f-1][idx:]
        target.reverse()
        arr[f-1] = arr[f-1][:idx]
        for i in target:
            arr[t-1].append(i)

    
    
    for i in arr:
        
        ans += i[-1]
        
    print(ans) 
