#   Create a class called Juice which contains name and capacity as it's parameter
#   __str__ magic method converts the object value into human readble string format as it's defined
#   __add__ magic method overrides the + operator and uses the user defined method body

class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def __str__(self):
        return (self.name + ' (' + str(self.capacity)+'L)')

    def __add__(self, other):
        return Juice(self.name + '&' + other.name, self.capacity + other.capacity)

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(str(result))
