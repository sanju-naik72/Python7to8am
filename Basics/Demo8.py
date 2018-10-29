def fun1():
    print("Function 1")
    print(a)

a = 1000 # Global Variable

def fun2():
    print("Function 2")
    print(a)

fun2()
fun1()
