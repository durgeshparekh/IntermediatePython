"""
List comprehension
Dictionary comprehension
Set comprehension

"""

list_1 = [1, 32, 4, 5, 45, 3, 4, 5, 53, 4, 4, 6, 6, 7, 7, 5, 343, 343, 5, 4]
divided_by_3 = []
for item in list_1:
    if item % 3 == 0:
        divided_by_3.append(item)

print('without using list comprehension divided_by_3: ', divided_by_3)

print('using list comprehension:', [item for item in list_1 if item % 3 == 0])

#  dictionary comprehension
dict1 = {'a': 45, 'b': 65, 'A': 5}
print({k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})


#  set comprehension
squared = {x**2 for x in [1,2,3,4,5,5,5,5,4,4]}
print(squared)


#  generator comprehension
gen = (i for i in range(56) if i % 3 == 0)
for item in gen:
    print(item)
