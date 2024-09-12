from toolz import itertoolz

# Lista de transacciones
transacciones = [
    {"compra_id": 1, "tipo": "compra", "monto": 100},
    {"compra_id": 2, "tipo": "venta", "monto": 50},
    {"compra_id": 3, "tipo": "compra", "monto": 200},
    {"compra_id": 4, "tipo": "venta", "monto": 150},
    {"compra_id": 5, "tipo": "compra", "monto": 300},
]

# Usamos itertools.groupby para agrupar las transacciones por tipo
grupos = itertoolz.groupby("tipo", transacciones)

# Imprimimos los grupos
for grupo, values in grupos.items():
    print(f"Grupo {grupo}:")
    for value in values:
        print(f"-- {value}")
