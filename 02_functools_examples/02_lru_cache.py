from functools import lru_cache
import time


@lru_cache(maxsize=10)
def factorial(n):
    print(f"Llamado de la función con valor {n}")
    if n == 1:
        print(f"Resultado de la función con valor {n} = {1}")
        return 1

    x = n * factorial(n-1)
    print(f"Resultado de la función con valor {n} = {x}")
    return x


tic = time.time()
print('Resultado:', factorial(10))
print(factorial.cache_info())
print((time.time() - tic)*60)
print('-------')

tic = time.time()
print(factorial.cache_info())
print('Resultado:', factorial(15))
print((time.time() - tic)*60)
print('-------')

tic = time.time()
print(factorial.cache_info())
print('Resultado:', factorial(3))
print((time.time() - tic)*60)
print('-------')
