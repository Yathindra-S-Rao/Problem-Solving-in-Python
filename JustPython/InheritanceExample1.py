class Calculus:
    def summation(self, val1, val2):
        return val1 + val2

class FeatureMultiply():
    def multiply(self, val1, val2):
        return val1 * val2

class Derived(Calculus, FeatureMultiply):
    def devide(self, val1, val2):
        return val1 / val2

ob = Derived()
print(ob.summation(2, 3))
print(ob.multiply(4, 5))
print(ob.devide(100, 5))
