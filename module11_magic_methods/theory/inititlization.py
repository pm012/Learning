class Foo:

    def __new__(cls, *args, **kwargs):
        print('Static method')
        instance = super(Foo, cls).__new__(cls)
        return instance



    def __init__(self, value=None):
        print('Call constructor')
        self.value = value

test = Foo(1)
print (test.value)