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
# 9
data = [3,7,2,-1,5]
i = 0
total = 0
while i < len(data):
    if data[i] < 0:
        break
    total += data[i]
    i += 1
print(total)
# 10

# part 2
# 1
items = ["a","x","b","x","x"]
i =0
while i < len(items):
        items.remove("x")
        i += 1
print(items)   
# 2
matrix = [[1,2],[3,4],[5,6]]
i = 0

while i < len(matrix):
    y = matrix[i]
    
    x = 0
    while x < len(y):
        print(y[x])
        x += 1
    i += 1
# 3
num = [1,2,3,4,5]
i = len(num) -1
while i >= 0:
    print(num[i])
    i -= 1
# 4
data = [10, 30, 55, 20, 80]
i = 0
while i < len(data):
    if data[i] > 50:
        print([i])
    i += 1    

    