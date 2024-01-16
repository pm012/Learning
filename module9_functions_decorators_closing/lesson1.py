#Case 1
def sum(a,b):
    return a+b

new_sum = sum

print(new_sum(3,6))

#Case2
def operations(a, b, func):
    return func(a,b)

print(operations(3, 6, sum))

#Case3
#--------------
def minus(a, b):
    return a-b

def power(a):
    return pow(a, 2)

def get_result(operator):
    if operator == '+':
        return sum
    if operator == '-':
        return minus
    if operator == '*':
        return power

sum_fun = get_result('+')   #'-', '*'
print(sum_fun(9,3))

#--------------------------------------
# caryvannya - return function
#closure - gets function
message = 'goodbye'
def outer_func(name):
    message = 'Hello'
    def inner_func(message, name):
        greeting = f'{message} {name}'
        return greeting
    
    return inner_func(message, name)

print(message)
print(outer_func('Serhii'))
#---------------------------------------
#TODO
def factorial(n, cache={}):
    if n < 0:
        raise ValueError
    
    def counter(n):
        result = 1
        for value in range(1, n+1):
            if value in cache:
                result = cache[value]
            else:
                result = value * cache.get(value-1,1) #if no value -1 then return 1 by default
                cache[value] = result
                print('{} not in cache {}'.format(value, result))
        return result
    return counter(n)
        

    
    
print('-------start----------')    
print(factorial(3))
print('-------end----------')    

#-----------------------
def outer_function(variable):
    def inner_func_one(arg):
        print(f'Function one with variable {variable} {arg}')

    def inner_func_two(argon):
        print(f'Function two with variable {variable} {argon}')

    return inner_func_one, inner_func_two

    
currying = outer_function("Hello")
inner_one, inner_two = currying

inner_one('Mike')
inner_two('Roman')







