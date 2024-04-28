# Lambda function
"""
SyntaxL=:
lambda argument: manipulate(argument)

"""

# def add(a, b):
#     s = a + b
#     return s

# add = lambda x, y : x+y
"""
lambda is basically used to shorten the function in one line

In above example, add is function name,
x,y are arguments
x + y is action performed to get result

"""
# print(add(6, 6))

def x(val):
    return val[1]

a = [(1, 3), (4555, 500), (555, 34)]
# a.sort(key=lambda x: x[1])  # lambda functions
a.sort(key=x)

print(a)