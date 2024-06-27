import math
points = [(1, 2), (4, 6), (5, 8), (2, 1)]

def euclideanDistance(tuple1, tuple2):
    x1, y1 = tuple1
    x2, y2 = tuple2
    
    res = math.sqrt((x2 - x1) **2 + (y2-y1) **2)
    return res
    
length = len(points)
list1 = []
i = 0
j = 0
for p in range(length):
    for _ in range(j,length - 1):
        list1.append(euclideanDistance(points[i], points[_ + 1]))
         
    i+= 1
    j += 1


min(list1)
