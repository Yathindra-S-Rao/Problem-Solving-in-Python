class EmployeeTable:
    
    def __init__(self, employee_id, employee_name, employee_phone):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_phone = employee_phone

    def __str__(self):
        return "EMPID\tEMPNAME\tEMPPHONE\n" + self.employee_id + "\t" +self.employee_name + "\t" + self.employee_phone + "\n"

emp1 = EmployeeTable("133589", "Yathindra S", "8050589148")
print(emp1)
