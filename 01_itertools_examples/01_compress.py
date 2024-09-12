from itertools import compress
from data import grupo_usuarios, GeneradorNumerosAleatorios


filter_random = GeneradorNumerosAleatorios(len(grupo_usuarios.usuarios),
                                           minimo=0, maximo=1)

filtro = list(filter_random)
print(filtro)

# Filtra elementos de los datos que tengan un elemento correspondiente
# en los selectores que se evalúe como Verdadero.
# compress(data, sel)
compress_iter = compress(grupo_usuarios, filtro)
for i in compress_iter:
    print(i)
