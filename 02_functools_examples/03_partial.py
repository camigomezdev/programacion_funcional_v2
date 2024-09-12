from functools import partial


# Definimos una función que calcula el precio final después de aplicar un descuento
def aplicar_descuento(precio, descuento):
    return precio - (precio * descuento)


# Creamos versiones especializadas de la función para diferentes descuentos
descuento_10 = partial(aplicar_descuento, descuento=0.10)
descuento_20 = partial(aplicar_descuento, descuento=0.20)
descuento_30 = partial(aplicar_descuento, descuento=0.30)

# Lista de precios de productos
precios = [100, 200, 300, 400, 500]

# Aplicamos diferentes descuentos a los precios
precios_con_descuento_10 = list(map(descuento_10, precios))
precios_con_descuento_20 = list(map(descuento_20, precios))
precios_con_descuento_30 = list(map(descuento_30, precios))

print("Precios originales:", precios)
print("Precios con 10% de descuento:", precios_con_descuento_10)
print("Precios con 20% de descuento:", precios_con_descuento_20)
print("Precios con 30% de descuento:", precios_con_descuento_30)
