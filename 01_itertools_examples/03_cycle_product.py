from itertools import cycle, product
from data import GrupoUsuarios, usuarios

# Intial data
print("-----------")
print("Cycle genera un ciclo infinito con los datos suministrados")
grupo_usuarios = GrupoUsuarios(usuarios)
cycle_iter = cycle(grupo_usuarios)

# for x in range(20):
#     print(next(cycle_iter))

for user in cycle_iter:
    print(user["nombre"])

print("-----------")
print("Enumerate crea tuplas de cada "
      "dato dado con un indice consecutivo")
grupo_usuarios = GrupoUsuarios(usuarios)
for enum in enumerate(grupo_usuarios, start=1):
    print(enum)


print("-----------")
print("Product equivale a bucles for anidados "
      "en una expresión de generador.")
grupo_usuarios = GrupoUsuarios(usuarios)
# product_iter = product(range(3), grupo_usuarios)
product_iter = product(['a', 'b', 'c'], grupo_usuarios)


for prod in product_iter:
    print(prod)
