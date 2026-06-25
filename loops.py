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
# 5
secret = 42
guesses = [10,30,42]
i = 0
while i < len(guesses):
    if guesses[i] == secret:
        print(i + 1)
    i += 1

# part 3
# 1
# You need one loop for the entire list and another loop for the inner list.
# 2
# If you use break in the inner loop it will return to the outer loop and if you use break in the outer loop it will stop the loop completely
# 3
# Once it finds the specific value, it will stop the inner search and return to the outer loop and move to another list.
# 4
# If I want there to be a loop but not print anything, then I say continue if so and so and it will return to the beginning of the loop.
# 5
# It will continue to run on the inner loop until it finishes and it will return to the outer loop.

# Practice
# 1
matrix = [
    [2, 4, 6],
    [3, 99, 5],
    [8, 1, 7]]
# for list in matrix:
#     for rows in list:
#         if rows > 50:
#             print(rows)
#             break
row =0
while row < len(matrix):
    col = 0
    while col < len(matrix[row]):
        if matrix[row][col] > 50:
            print(matrix[row][col])
            break
        col+= 1
    row +=1        

# 2
matrix = [
    [5, -1, 8],
    [3, 4, -1],
    [9, 2, 6]]
row = 0    
while row < len(matrix):
    col = 0
    while col < len(matrix[row]):
        if matrix[row][col] < 0:
            col +=1
            continue
            
            
        else:
            print(matrix[row][col])
        col +=1
    
    row += 1        