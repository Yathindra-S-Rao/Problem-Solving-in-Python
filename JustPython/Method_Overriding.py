class Employee:
    
    def __init__(self, name, org):
        self.name = name
        self.company = org
        
    def get_employee_details(self):
        return f'{self.name} {self.company}'

class Details(Employee):
    
    def get_employee_details(self):
        return f'{self.name} is working in {self.company}'
        

if __name__=='__main__':
    obj = Details('Yathindra', 'Capgemini')
    print(obj.get_employee_details())
