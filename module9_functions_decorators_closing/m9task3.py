""""
function caching_fibonacci() should calculate fibonacci numbers:
It should contain inner function fibonacci(n) that will calculate Fibonacci number
caching_fibonacci should return function fibonacci 

"""

def caching_fibonacci():
    cache = [0,1]
    def fibonacci(n):
        if n ==0:
            return 0
        if n ==1:
            return 1        
        if len(cache)<n:            
            cache.append(fibonacci(n-1)+fibonacci(n-2))
        return cache[n-1]
    return fibonacci

f = caching_fibonacci()
print(f(8))