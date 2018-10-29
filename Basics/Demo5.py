def fun1():
    print("Function 1")
    fun2()

def fun3():
    fun2()
    print("Function 3")

def fun4():
    print("Function 4")
    fun3()
    
def fun2():
    print("Function 2")

fun1()
fun2()
fun3()
fun4()
