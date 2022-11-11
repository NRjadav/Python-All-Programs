
class salary:
    def __init__(self,currentsalary,bonus):
        self.currentsalary=currentsalary
        self.bonus=bonus

    def annualsalary(self):
        return self.currentsalary*12 + self.bonus

class employee:
    def __init__(self,name,depart,salary,bonus):
        self.name=name
        self.depart=depart
        self.salary=salary
        self.bonus=bonus

        self.main_salary=salary(self.salary,self.bonus)

    def total_sal(self):
        return self.main_salary.annualsalary()

emp=employee("nilesh","IT",10000,1500)
print(emp.total_sal)            
