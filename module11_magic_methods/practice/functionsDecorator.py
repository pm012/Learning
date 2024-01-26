from time import sleep
import datetime
from typing import Any

def time_this(original_function):
    print('Decorating')
    def inner_function(*args, **kwargs):
        print('Start time')
        before = datetime.datetime.now()
        func = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print('Elapsed time = {}'.format(after-before))
        return func

    return inner_function

def time_all_class_method(cls):
    class NewCls(object):
        def __init__(self, *args, **kwargs) -> None:
            self.oInstance = cls(*args, **kwargs)

        def __getattribute__(self, item: str) -> Any:
            """                       
            
            This dunder method is called every time when the access is gained to any NewCls object attribute. 
            This function tries to get attribute from NewCls at first. 

            1. If it's impossible it tries to get attribute from self.oInstance (instance of the decorated class).
            2. If it is possible to get attribute from self.oInstance and the attribute is a method of the instance, then 'time_this' is applied.

            
            """
            try:
                attr = super(NewCls, self).__getattribute__(item)
            except AttributeError:
                pass
            else:
                return attr
            attr = self.oInstance.__getattribute__(item)
            if type(attr) == type(self.__init__):
                return time_this(attr)
            else:
                return attr

    return NewCls


@time_all_class_method
class Foo(object):
    def foo_function(self):
        print('Entering foo_function')
        sleep(2)
        print('Exit foo_function')

    def baz_func(self):
        print('Entering baz_function')
        sleep(2)
        print('Exit baz_function')

test = Foo()
test.foo_function()
test.baz_func()
