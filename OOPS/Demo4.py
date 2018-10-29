class Employee:
    def assign(self):
        self.idno = 101
        self.name = "Rama"
    def display(self):
        print(self.idno)
        print(self.name)

e1 = Employee()
e1.assign()
e1.display()
print("-------------------")
e2 = Employee()
e2.assign()
e2.display()