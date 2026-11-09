class NaveEspacial:
    """TAD que representa una nave espacial pilotada por un jugador."""

    def __init__(self, nombre, piloto, nivel_escudo=100):
        self.nombre = nombre
        self.piloto = piloto
        self.nivel_escudo = nivel_escudo

    def __str__(self):
        return (f"Nave: {self.nombre} | "
                f"Piloto: {self.piloto} | "
                f"Nivel de escudo: {self.nivel_escudo}")

nave1 = NaveEspacial("Halcón Milenario", "Han Solo", 100)
nave2 = NaveEspacial("X-Wing", "Luke Skywalker", 100)

print("=== Características iniciales de las naves ===")

print(nave1)
print(nave2)


class NaveEspacial:
    """TAD que representa una nave espacial pilotada por un jugador."""

    ESCUDO_MAXIMO = 100

    def __init__(self, nombre, piloto, nivel_escudo=100):
        self.nombre = nombre
        self.piloto = piloto
        self.nivel_escudo = nivel_escudo

    def __str__(self):
        return (f"Nave: {self.nombre} | "
                f"Piloto: {self.piloto} | "
                f"Nivel de escudo: {self.nivel_escudo}")

    def recibir_disparo(self, dano):
        """Resta daño al escudo. Si baja de 0, la nave es destruida."""
        self.nivel_escudo -= dano
        print(f"{self.nombre} recibió un disparo de {dano} de daño.")

        if self.nivel_escudo < 0:
            self.nivel_escudo = 0
            print(f"¡{self.nombre} ha sido destruida!")
        else:
            print(f"Escudo restante: {self.nivel_escudo}")

    def recargar_escudo(self, cantidad):
        """Aumenta el escudo (sin superar el máximo)."""
        if self.nivel_escudo == 0:
            print(f"{self.nombre} está destruida, no se puede recargar el escudo.")
            return

        self.nivel_escudo = min(self.nivel_escudo + cantidad, self.ESCUDO_MAXIMO)
        print(f"Escudo de {self.nombre} recargado. Nivel actual: {self.nivel_escudo}")


nave = NaveEspacial("Halcón Milenario", "Han Solo", 100)

print("Estado inicial de la nave:")
print(nave)

print("Iniciando sumulación de la batalla...")
nave.recibir_disparo(30)
nave.recibir_disparo(45)

print("Intentando recargar el escudo... ")
nave.recargar_escudo(20)

print("Recibiendo un disparo")
print(nave)

