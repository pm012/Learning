class Product:
    def __init__(self, value_one, value_two):
        self.one = value_one
        self.two = value_two

    def __call__(self):
        return self.one * self.two


test = Product(5, 7)
print(test())

# Створює декторатор
class Product:
    def __call__(self, value_one, value_two):
        return value_one * value_two

test = Product()
print(test(3, 9))

# Створює декторатор
#@Product