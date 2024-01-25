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
            #TODO add comment
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
