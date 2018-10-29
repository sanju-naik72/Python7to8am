a = 1000 # global variable
def fun1():
    print(a)
    a = 50 # local variable
    print(a)

fun1()
