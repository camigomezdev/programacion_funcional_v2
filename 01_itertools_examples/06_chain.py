from sys import getsizeof
from itertools import chain, zip_longest
from data import GrupoUsuarios, usuarios

nombres = ['Fatima', 'Ed', 'Jani']
grupo_usuarios = GrupoUsuarios("CodigoFacilito", usuarios)
print(f"Size of lista {getsizeof(list(chain(nombres, grupo_usuarios)))}")

grupo_usuarios = GrupoUsuarios("CodigoFacilito", usuarios)
print(f"Size of iter: {getsizeof(chain(nombres, grupo_usuarios))}")

print("-----------")
for dato in chain(nombres, grupo_usuarios):
    print(dato)
