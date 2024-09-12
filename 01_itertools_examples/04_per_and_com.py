from itertools import (
    combinations, permutations, combinations_with_replacement)

# Intial data
nombres = ['Eduardo', 'Jani', 'Mary']

print(f"Permutaciones de {nombres}")
permutations_iter = permutations(nombres)
for index, dato in enumerate(permutations_iter, start=1):
    print(f"Permutación {index}: {dato}")

print("-------------")
print(f"Combinaciones de {nombres}")
combinations_iter = combinations(nombres, 2)
for index, com in enumerate(combinations_iter):
    print(f"Combinación {index}: {com}")

print("-------------")
print(f"Combinaciones con elementos repetidos de {nombres}")
com_with_replace = combinations_with_replacement(nombres, 2)
for index, com_w_r in enumerate(com_with_replace):
    print(f"Combinación {index}: {com_w_r}")
