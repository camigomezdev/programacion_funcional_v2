from functools import singledispatch, partial


@singledispatch
def add(a, b):
    raise NotImplementedError("Unsupported type")


@add.register
def _(a: int, b):
    if isinstance(b, int):
        print("Type's argument:", type(a), type(b))
        return a + b
    elif isinstance(b, list):
        print("Type's argument:", type(a), type(b))
        return a + sum(b)
    else:
        raise NotImplementedError("Unsupported type combination")


@add.register
def _(a: list, b):
    if isinstance(b, list):
        print("Type's argument:", type(a), type(b))
        return sum(a) + sum(b)
    else:
        raise NotImplementedError("Unsupported type combination")


# Enteros
print(add(4, 10))

# Listas
print(add([3, 4, 5], [6, 5, 7]))

# Enteros y listas
print(add(4, [6, 5, 7]))
