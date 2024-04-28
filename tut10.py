# enumerate function

a = ['CodeWithDurgesh', 'Zee', 'Sony Liv', '9XM']

# program to find list item which index divided by 2
# without using enumerate
# i = 0
# for item in a:
#     i = i + 1
#     if i % 2 == 0:
#         print(item)

for i, item in enumerate(a):
    if (i+1) % 2 == 0:
        print(item)
