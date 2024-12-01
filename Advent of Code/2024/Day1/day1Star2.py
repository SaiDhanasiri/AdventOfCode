with open ("day1Text") as f:
    s = f.readlines()


left = []
right = []
ans = 0

for x in s: 
    l, r = x.split("   ")
    left.append(l)
    right.append(r)

ans = {}

for i in range(len(left)):
    count = 0
    for j in range(len(right)): 
        if int(left[i]) == int(right[j]):
            count+=1
    ans[int(left[i])] = count

returnVal = 0

for x in left: 
    returnVal += int(x) * ans[int(x)]

print(returnVal)

