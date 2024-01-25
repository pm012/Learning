def class_decorator(cls):
    cls.magic_value = 50
    return cls

@class_decorator
class Foo:
    attr = 0


test = Foo()
print(test.attr)
print(test.magic_value)