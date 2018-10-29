class Employee:
    c_name = "sathya"
    c_cno = 987643210
    def assign(self,id,na):
        self.idno = id
        self.name = na
    def display(self):
        print(Employee.c_name)
        print(Employee.c_cno)
        print(self.idno)
        print(self.name)