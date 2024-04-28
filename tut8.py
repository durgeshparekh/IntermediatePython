# advance slicing

list1 = [3, 4, 5, 6, 7, 8, 9]
# print(list1[1:50])
# print(list1[:50])  # if blank then it takes 0 by default 0 to 50
# print(list1[-2:])  # start from right -1,-2,-3... gives output [8,9] because it print value from [-2:0]
# print(list1[:-3])  # start from right 0,-1,-2,-3... gives output [3, 4, 5, 5, 6] because it print value from [0:-3]
# print(list1[-2:-5])
# 3 - 1 = 2

print(list1[::2])  # [3, 5, 6, 8] it will skip 2 numbers and print accordingly
print(list1[::-1])  # [9, 8, 7, 6, 5, 5, 4, 3] reverse the list



