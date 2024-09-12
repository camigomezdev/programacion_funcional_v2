from itertools import zip_longest
from data import GrupoUsuarios, GeneradorNumerosAleatorios, usuarios

print("-------------")
print("Zip")
# numbers = GeneradorNumerosAleatorios(10, minimo=1, maximo=20)
grupo_usuarios = GrupoUsuarios(usuarios)
zip_short = zip(range(10), grupo_usuarios)
for dato in zip_short:
    print(f"{dato}")

print("-------------")
print("Zip longest")
# numbers = GeneradorNumerosAleatorios(10, minimo=1, maximo=20)
grupo_usuarios = GrupoUsuarios(usuarios)
zip_long = zip_longest(range(10), grupo_usuarios)
for dato in zip_long:
    print(f"{dato}")
