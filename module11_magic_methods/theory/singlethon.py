
#---- the first implementation ----
class Singleton(object):
    __instance__ = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls, **kwargs)

        return cls.__instance
    
    class MyClass(Singleton):
        pass



class Singleton1(object):
    __instance__ = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance[cls] = super(Singelton1, cls).__call__(*args, **kwargs)

        return cls.__instance
    
    #Python 3
    class MyClass(Singleton1):
        pass

    #Python 2
    class MyClass:
        __metaclass__= Singleton1



