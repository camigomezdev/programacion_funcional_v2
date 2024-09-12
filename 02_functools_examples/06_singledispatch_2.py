import json
import functools


# Definimos una función genérica para serializar datos
@functools.singledispatch
def serializar(obj):
    raise TypeError(f"No se puede serializar el tipo {type(obj)}")


# Registramos una implementación para el tipo int
@serializar.register(int)
def _(obj):
    return json.dumps({"tipo": "entero", "valor": obj})


# Registramos una implementación para el tipo str
@serializar.register(str)
def _(obj):
    return json.dumps({"tipo": "cadena", "valor": obj})


# Registramos una implementación para el tipo list
@serializar.register(list)
def _(obj):
    return json.dumps({"tipo": "lista", "valor": [serializar(item) for item in obj]})


# Ejemplos de uso
print(serializar(42))          # {"tipo": "entero", "valor": 42}
print(serializar("hola"))      # {"tipo": "cadena", "valor": "hola"}
# {"tipo": "lista", "valor": [{"tipo": "entero", "valor": 1}, {"tipo": "cadena", "valor": "dos"}]}
print(serializar([1, "dos"]))
