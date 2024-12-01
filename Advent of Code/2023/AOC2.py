with open ("2input.txt") as f:
    s = f.readlines()


## part 1: 
'''
r = 0
for i, x in enumerate(s):
    groups = x.strip().split(":")[1].split(";")
    for g in groups:
        m = {"red" : 0, "green": 0, "blue": 0}
        for e in g.split(","):
            a,b = e.split()
            m[b] = int(a)
        if m["red"] > 12 or m["green"] > 13 or m["blue"] > 14: 
            break
    else: 
        r += i + 1
#print(r)

'''

## part 2: 


r = 0
for i, x in enumerate(s):
    groups = x.strip().split(":")[1].split(";")
    tm = {"red" : 0, "green": 0, "blue": 0}
    for g in groups:
        m = {"red" : 0, "green": 0, "blue": 0}
        for e in g.split(","):
            a,b = e.split()
            m[b] = int(a)
        for k in tm: 
            tm[k] = max(tm[k], m[k])
    r += int(tm["red"]) * int(tm["blue"]) * int(tm["green"])

print(r)
