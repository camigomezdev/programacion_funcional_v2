from itertools import cycle, product, count
from data import GrupoUsuarios, usuarios

# Intial data
print("-----------")
print("Cycle genera un ciclo infinito con los datos suministrados")
grupo_usuarios = GrupoUsuarios("CodigoFacilito", usuarios)
print(grupo_usuarios)

cycle_iter = cycle(grupo_usuarios)

for x in range(20):
    print(next(cycle_iter))

# for user in cycle_iter:
#     print(user["nombre"])
