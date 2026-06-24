# part 1
# 1
i = 1
while i <= 5:
    print(i)
    i += 1
# 2
i = 10
while i >= 1:
    print(i)
    i -= 1
# 3
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(total)    
# 4
items = [2,4,6,8]
i = 0
while i < len(items):
    if items[i] > 5:
        print(items[i])
        break
    i += 1    
# 5
i = 2
while i <= 10:
    print(i)
    i += 2   
# 6
agents = ["alpha","bravo","charlie"]
i = 0
while i < len(agents):
    print(agents[i])
    i += 1          
# 7
scores = {"alpha":80,"bravo":95,"charlie":70}
item = scores.items()
i = 0
for x in item:
    for y in x:
        print(y)
# 8
start = 1
i = 2
while start * i < 100:
    start *= 2
    print(start)        

