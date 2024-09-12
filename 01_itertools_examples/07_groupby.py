from itertools import groupby

# Lista de transacciones
transacciones = [
    {"compra_id": 1, "tipo": "compra", "monto": 100},
    {"compra_id": 2, "tipo": "venta", "monto": 50},
    {"compra_id": 3, "tipo": "compra", "monto": 200},
    {"compra_id": 4, "tipo": "venta", "monto": 150},
    {"compra_id": 5, "tipo": "compra", "monto": 300},
]

# Ordenamos la lista de transacciones por tipo
transacciones_ordenadas = sorted(transacciones, key=lambda x: x["tipo"])

# Usamos itertools.groupby para agrupar las transacciones por tipo
grupos = groupby(transacciones_ordenadas, key=lambda x: x["tipo"])

# Imprimimos los grupos
for grupo, values in grupos:
    print(f"Grupo {grupo}:")
    for value in values:
        print(f"-- {value}")
