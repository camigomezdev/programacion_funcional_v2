from itertools import product, count
from data import GrupoUsuarios, usuarios

print("Product equivale a bucles for anidados "
      "en una expresión de generador.")
grupo_usuarios = GrupoUsuarios("CodigoFacilito", usuarios)
print(grupo_usuarios)

# product_iter = product(range(3), grupo_usuarios)
product_iter = product(count(5), grupo_usuarios)

for prod in product_iter:
    print(prod)
