a = 50
print(a)
def fun1():
    global a
    print(a)
    fun2()
    print(a)
    a = False
    print(a)

def fun2():
    print(b)
    print(a)
    c = 99.25
    print(c)

b = 45
print(a+b)
fun1()
fun2()
