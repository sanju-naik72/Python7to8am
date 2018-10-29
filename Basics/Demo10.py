a = 100 # global variable
def fun1():    
    a = 90 # local variable
    print(a)
    print(id(a))

print(a)
print(id(a))
fun1()
print(a)
