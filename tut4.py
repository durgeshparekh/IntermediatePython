"""
Iterable - 
Iterator -
Iteration -

"""


def gen(n):
    for i in range(n):
        yield i


ob1 = gen(6)
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))
i = 345

