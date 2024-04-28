import bisect

number = 31
a = [1, 2, 3, 30, 6, 7, 8, 9, 34]
print(bisect.bisect(a, number))  # get the index to sort the given list

bisect.insort(a, number)  # insert the number variable value to their sorted place in given array
print(a)

