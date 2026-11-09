class Mago:
    def __init__(self, nombre, mana_base):
        self.nombre = nombre
        self.mana_base = mana_base
        self.mana_actual = mana_base

    def mostrar_estado(self):
        print(f"{self.nombre} | Maná: {self.mana_actual}/{self.mana_base}")

    def _consumir_mana(self, costo):
        """Descuenta maná si hay suficiente. Devuelve True/False."""
        if self.mana_actual >= costo:
            self.mana_actual -= costo
            return True
        print(f"{self.nombre} no tiene suficiente maná (necesita {costo}, tiene {self.mana_actual}).")
        return False


class MagoFuego(Mago):
    def __init__(self, nombre, mana_base, temperatura_llama):
        super().__init__(nombre, mana_base)
        self.temperatura_llama = temperatura_llama

    def lanzar_bola_fuego(self):
        costo = 30
        if self._consumir_mana(costo):
            print(f"{self.nombre} lanza una bola de fuego a {self.temperatura_llama}°C. "
                  f"¡El enemigo arde en llamas! (-{costo} de maná)")


class MagoHielo(Mago):
    def __init__(self, nombre, mana_base, grosor_escudo_hielo):
        super().__init__(nombre, mana_base)
        self.grosor_escudo_hielo = grosor_escudo_hielo

    def congelar_terreno(self):
        costo = 25
        if self._consumir_mana(costo):
            print(f"{self.nombre} congela el terreno. Su escudo de hielo de "
                  f"{self.grosor_escudo_hielo} cm lo protege. (-{costo} de maná)")


if __name__ == "__main__":
    mago_fuego = MagoFuego("Ignis", 100, 1200)
    mago_hielo = MagoHielo("Glacia", 90, 15)

    mago_fuego.mostrar_estado()
    mago_fuego.lanzar_bola_fuego()
    mago_fuego.mostrar_estado()

    print()

    mago_hielo.mostrar_estado()
    mago_hielo.congelar_terreno()
    mago_hielo.mostrar_estado()