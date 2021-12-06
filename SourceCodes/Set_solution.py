set_1 = {1, 2, 3, 4, 5, 6, 7, 8}
set_2 = {4, 5, 6, 7}

set_3 = set_1 & set_2  # Intersection
set_4 = set_1 | set_2  # Union

print(set_3)  # Result: 4,5,6,7
print(set_4)  # Result: 1,2,3,4,5,6,7,8

for i in set_4:  # Result: 1,2,3,4,5,6,7,8
    print(i)
