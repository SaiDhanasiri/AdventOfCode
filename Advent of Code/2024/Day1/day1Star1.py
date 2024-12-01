with open ("day1Text") as f:
    s = f.readlines()


left = []
right = []
ans = 0

for x in s: 
    l, r = x.split()
    left.append(l)
    right.append(r)


left = sorted(left)
right = sorted(right)

for i in range(len(left)):
    ans += abs(int(left[i]) - int(right[i]))


print(ans)


