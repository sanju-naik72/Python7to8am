#Function with default values
def fun1(no=0,name=None,salary=0.0):
    print("IDNO = ",no)
    print("NAME = ",name)
    print("SALARY = ",salary)

fun1()
print("------------------")
fun1(101)
print("------------------")
fun1(name="Ravi")
print("------------------")
fun1(salary=125000.00,no=101)
