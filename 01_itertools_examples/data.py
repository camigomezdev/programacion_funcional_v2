import random


class GrupoUsuarios:
    def __init__(self, name, usuarios):
        self.name = name
        self.usuarios = usuarios
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.usuarios):
            raise StopIteration
        usuario = self.usuarios[self.indice]
        self.indice += 1
        return usuario

    def __str__(self):
        return f"El grupo {self.name} tiene {len(self.usuarios)} usuarios"


class GeneradorNumerosAleatorios:
    def __init__(self, cantidad, minimo, maximo):
        self.cantidad = cantidad  # Cantidad de números a generar
        self.minimo = minimo      # Valor mínimo del rango
        self.maximo = maximo      # Valor máximo del rango
        self.generados = 0        # Contador interno para controlar el número de generados

    def __iter__(self):
        return self

    def __next__(self):
        if self.generados >= self.cantidad:
            raise StopIteration
        self.generados += 1
        generado = random.randint(self.minimo, self.maximo)
        # print("Aleatorio generado:", generado)
        return generado

    def __str__(self):
        return (f"Se generaran {self.cantidad} números aleatorios entre el"
                "{self.minimo} y {self.maximo}")


usuarios = [
    {'nombre': 'Ed', 'edad': 28, 'email': 'ed@example.com', 'rol': 'user'},
    {'nombre': 'Bob', 'edad': 34, 'email': 'bob@example.com', 'rol': 'admin'},
    {'nombre': 'Charlie', 'edad': 22, 'email': 'charlie@example.com', 'rol': 'user'},
    {'nombre': 'Camila', 'edad': 40, 'email': 'camila@example.com', 'rol': 'admin'},
    {'nombre': 'Mary', 'edad': 22, 'email': 'mary@example.com', 'rol': 'user'},
    {'nombre': 'Dana', 'edad': 40, 'email': 'dana@example.com', 'rol': 'admin'},
]
