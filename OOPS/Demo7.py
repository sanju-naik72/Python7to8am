class Employee:
    comp_name = "sathya"
    comp_cno = 7896541230
    @staticmethod
    def showCompanyDetails():
        print(Employee.comp_name)
        print(Employee.comp_cno)

Employee.showCompanyDetails()

