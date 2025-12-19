# Encapsulation 

class Car:
    
    def __init__(self, brand, color, modal, price, year):
        self.brand = brand
        self.color = color
        self.modal = modal
        self.__price = price or 0
        self.year = year
        
    def get_price(self):
        return  f'INR. {self.__price:.2f}'
        
    def set_price(self, price):
        self.__price = price
        return 'Price updated successfully.'
        
c1 = Car('Suzuki', 'Red', 'ZXI+', None, 2023)
print(c1.get_price())



c1.brand = 'Benz'
print(c1.brand)

print(c1.set_price(945000))
print(c1.get_price())
