count = 0 

def safe(level):
    difference = [] 
    for i in range(len(level) - 1):
        difference.append(level[i+1] - level[i])
    
    posDiff = all(1 <= x <= 3 for x in difference)
    negDiff = all(-1 >= x >= -3 for x in difference)

    return posDiff or negDiff

for report in open("Day2Text"):
    levels = list(map(int, report.split()))
    if any(safe(levels[:index] + levels[index + 1:] for index in range(len(levels)))):
        count+=1


print(count)


