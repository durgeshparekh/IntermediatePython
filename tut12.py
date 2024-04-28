# Join function

sample_list = ['chalk', 'duster', 'board', 'pen']

"""
print like this: chalk and duster and board and pen

"""
# without using join function
for item in sample_list:
    if item != 'pen':
        print(item, 'and ', end='')
    else:
        print(item)

print(' and '.join(sample_list))  # using join function same output we will get