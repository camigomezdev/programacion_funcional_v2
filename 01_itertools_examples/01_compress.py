from itertools import compress
from data import GeneradorNumerosAleatorios, GrupoUsuarios, usuarios

grupo_usuarios = GrupoUsuarios("CodigoFacilito", usuarios)
print(grupo_usuarios)

filter_random = GeneradorNumerosAleatorios(
    len(grupo_usuarios.usuarios), minimo=0, maximo=1)

print("------------")

# Filtra elementos de los datos que tengan un elemento correspondiente
# en los selectores que se evalúe como Verdadero.
# compress(data, sel)
compress_iter = compress(grupo_usuarios, filter_random)

for dato in compress_iter:
    print(dato)
