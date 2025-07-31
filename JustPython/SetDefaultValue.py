# @author: Yathindra S.
# Program to set default values to Name and email address when inputs are blank

class Customer:
    
    def __init__(self, name, email):
        self.cust_name = name or 'Customer'
        self.cust_email = email or 'default@gmail.com'
    
    def __repr__(self):
        return f'Customer Name: {self.cust_name} \nEmail : {self.cust_email}'
    
if __name__=='__main__':
    objs = [Customer('Ravi', 'ravi@gmail.com'), Customer('', '')]
    for i in objs:
        print(i)

# ====================================================        
# Output
# Customer Name: Ravi 
# Email : ravi@gmail.com
# Customer Name: Customer 
# Email : default@gmail.com
