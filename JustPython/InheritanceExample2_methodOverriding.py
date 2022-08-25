class Bank:
    def get_rate_of_interest(self):
        return 10.0

class SBI(Bank):
    def get_rate_of_interest(self):
        return 5.5

class AxisBank(Bank):
    def get_rate_of_interest(self):
        return 6.3

class AxisBank_Deposite(AxisBank):
    def create_fixed_deposite(self):
        return "Fixed deposit account has been created"

axis = AxisBank_Deposite()
sbi = SBI()

print("Axis bank's RoI is ", axis.get_rate_of_interest())
print("Create FD : ", axis.create_fixed_deposite())
print("SBI's RoI is ", sbi.get_rate_of_interest())