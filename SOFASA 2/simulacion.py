class Simulacion:

    def __init__(
        self,
        cabina,
        vehiculos,
        resistencias,
        calculos
    ):
        self.cabina = cabina
        self.vehiculos = vehiculos
        self.resistencias = resistencias
        self.calculos = calculos

        self.sistema_encendido = False
        self.secado_activo = False

    # SISTEMA

    def encender_sistema(self):
        self.sistema_encendido = True
        self.resistencias.encender()

    def apagar_sistema(self):
        self.sistema_encendido = False
        self.resistencias.apagar()

    # SECADO
    

    def iniciar_secado(self):
        if self.sistema_encendido:
            self.secado_activo = True

    def detener(self):
        self.secado_activo = False

    # VEHÍCULOS

    def ingresar_vehiculos(self, cantidad):
        self.vehiculos.ingresar(cantidad)

    def actualizar_movimiento(self, velocidad):
        if not self.secado_activo:
            return

        self.vehiculos.mover(velocidad)

    # TEMPERATURA

    def actualizar_temperatura(self):
        if not self.sistema_encendido:
            return

        self.calculos.aumentar_temperatura()

    def obtener_temperatura(self):
        return self.calculos.obtener_temperatura()

    
    # ESTADOS

    def esta_encendido(self):
        return self.sistema_encendido

    def esta_secando(self):
        return self.secado_activo

    
    # REINICIAR

    def reiniciar(self):
        self.secado_activo = False
        self.sistema_encendido = False

        self.vehiculos.reiniciar()
        self.resistencias.apagar()
        self.calculos.reiniciar()