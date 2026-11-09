class Transformer:
    def __init__(self, nombre):
        self.nombre = nombre

    def transformarse(self):
        return f"{self.nombre} se transforma en su forma alterna."


class AutobotCoche(Transformer):
    def __init__(self, nombre, velocidad_max=300):
        super().__init__(nombre)
        self.velocidad_max = velocidad_max

    def transformarse(self):
        return f"{self.nombre}: ¡Se convierte en un deportivo a {self.velocidad_max} km/h!"


class AutobotAvion(Transformer):
    def __init__(self, nombre):
        super().__init__(nombre)

    def transformarse(self):
        return f"{self.nombre}: ¡Despliega las alas y vuela a velocidad supersónica!"


class AutobotDinosaurio(Transformer):
    def __init__(self, nombre):
        super().__init__(nombre)

    def transformarse(self):
        return f"{self.nombre}: ¡Se transforma en un T-Rex robótico!"


if __name__ == "__main__":
    ejercito = [
        AutobotCoche("Bumblebee", 300),
        AutobotAvion("Jetfire"),
        AutobotDinosaurio("Grimlock"),
        AutobotCoche("Sideswipe", 280),
    ]

    print("¡Autobots, transformaos!")
    for transformer in ejercito:
        print(transformer.transformarse())



        