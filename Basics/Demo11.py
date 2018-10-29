a = 1000
def fun1():
    global a
    print(id(a))
    a = 50
    print(a)
    

print(a)
print(id(a))
fun1()
print(a)
    
    
