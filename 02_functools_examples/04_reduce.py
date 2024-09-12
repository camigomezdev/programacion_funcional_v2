from functools import reduce


def add(acumulador, value):
    result = acumulador + value
    print(f"{acumulador = }, {value = }, result={result}")
    return result


data_list = [1, 2, 3, 4, 5, 6, 7]
result = reduce(add, data_list)

print(result)
# 28
