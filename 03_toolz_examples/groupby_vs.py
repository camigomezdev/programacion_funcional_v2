import itertools
import toolz

transacciones = [4, 5, 6, 7, 3, 1, 1, 4, 5]

print("--------------")
print("itertools")
transacciones_ordenadas = sorted(transacciones)
grupos = itertools.groupby(transacciones_ordenadas)

for grupo, values in grupos:
    print(f"Grupo {grupo}: {list(values)}")

print("--------------")
print("Toolz")

# Agrupar
grupos = toolz.itertoolz.groupby(lambda x: x, transacciones)

for grupo, values in grupos.items():
    print(f"Grupo {grupo}: {values}")
