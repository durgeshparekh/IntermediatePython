# *args and **kwargs tutorial
#  *vars and **kvars tutorial

#  args example
def function_1(*argsjoke):
    # print(type(argsjoke))
    if len(argsjoke) == 3:
        print("The name of the student is", argsjoke[0], 'and age is', argsjoke[1], 'and roll no is', argsjoke[2])
    else:
        print("The name of the student is", argsjoke[0], 'and age is', argsjoke[1])


lis = ['Durgesh', 27, 56789]


# function_1(*lis)


# kwargs example
def print_marks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


markList = {"Durgesh": 100, "Henil": 95, "Kirti": 98, "Chhatrapal": 96, "Maulik": 88}

# print_marks(**markList)


# important note args and kwargs names are user defined. number of * (star) will identified as args and kwargs


def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)

    for key, value in kwargs.items():
        print(key, value)


master("normal arg", *lis, **markList)

