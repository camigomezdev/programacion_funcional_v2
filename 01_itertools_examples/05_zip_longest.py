from itertools import zip_longest, count
from data import GrupoUsuarios, usuarios


print("-------------")
print("Zip")
# numbers = GeneradorNumerosAleatorios(10, minimo=1, maximo=20)
grupo_usuarios = GrupoUsuarios("CodigoFacilito", usuarios)
print(grupo_usuarios)

zip_short = zip(count(1), grupo_usuarios)
for dato in zip_short:
    print(f"{dato}")


print("-------------")
print("Zip longest")
# numbers = GeneradorNumerosAleatorios(10, minimo=1, maximo=20)
grupo_usuarios = GrupoUsuarios("CodigoFacilito", usuarios)
print(grupo_usuarios)

zip_long = zip_longest(range(10), grupo_usuarios)
for dato in zip_long:
    print(f"{dato}")
