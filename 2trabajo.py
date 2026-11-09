class BatcuevaSystem:
    """Sistema de acceso de la Baticueva con datos confidenciales encapsulados."""

    NIVELES_VALIDOS = ("Verde", "Amarillo", "Rojo")

    def __init__(self, mando_central_pass, nivel_alerta="Verde"):
        self.__mando_central_pass = mando_central_pass   # atributo privado
        self.__nivel_alerta = nivel_alerta               # atributo privado

    def obtener_alerta(self):
        """Devuelve el nivel de alerta actual."""
        return self.__nivel_alerta

    def cambiar_alerta(self, nueva_alerta, clave_ingresada):
        """Cambia el nivel de alerta solo si la clave coincide exactamente."""
        if clave_ingresada != self.__mando_central_pass:
            print("Acceso denegado: clave incorrecta. El nivel de alerta no fue modificado.")
            return False

        if nueva_alerta not in self.NIVELES_VALIDOS:
            print(f"Nivel inválido. Opciones: {', '.join(self.NIVELES_VALIDOS)}")
            return False

        self.__nivel_alerta = nueva_alerta
        print(f"Acceso concedido. Nivel de alerta cambiado a: {nueva_alerta}")
        return True


baticueva = BatcuevaSystem("IamBatman2026", "Verde")

print("Estado inicial")
print(f"Alerta actual: {baticueva.obtener_alerta()}")

print("Intento con clave CORRECTA")
baticueva.cambiar_alerta("Rojo", "IamBatman2026")
print(f"Alerta actual: {baticueva.obtener_alerta()}")

print("Intento con clave INCORRECTA")
baticueva.cambiar_alerta("Verde", "Joker123")
print(f"Alerta actual: {baticueva.obtener_alerta()}")

print("Intento de acceso directo al atributo privado")
try:
    print(baticueva.__nivel_alerta)
except AttributeError as e:
    print(f"Error: {e}")
 