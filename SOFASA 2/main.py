import tkinter as tk

from cabina_3D import Cabina3D
from vehiculos import Vehiculos
from resistencias import Resistencias
from calculos import Calculos
from simulacion import Simulacion
from interfaz import Interfaz


class Aplicacion:

    def __init__(self, root):

        self.root = root

        
        # INTERFAZ
      
        self.interfaz = Interfaz(
            root,
            self.ingresar_vehiculos,
            self.cambiar_velocidad,
            self.encender_sistema,
            self.iniciar_secado,
            self.detener,
            self.reiniciar
        )

      
        # CABINA 3D
       
        self.cabina = Cabina3D(
            self.interfaz.area_simulacion
        )

        
        # MÓDULOS DE LA SIMULACIÓN
       

        self.vehiculos = Vehiculos(
            self.cabina
        )

        self.resistencias = Resistencias(
            self.cabina
        )

        self.calculos = Calculos()

        self.simulacion = Simulacion(
            self.cabina,
            self.vehiculos,
            self.resistencias,
            self.calculos
        )

       
        # VELOCIDAD
       

        self.velocidad_actual = 2.0

        
        # CONECTAR REDIBUJADO
       

        self.cabina.establecer_callback(
            self.dibujar
        )

       
        # DIBUJADO INICIAL
        

        self.dibujar()

     
        # INICIAR ACTUALIZACIÓN
        

        self.actualizar_movimiento()
        self.actualizar_temperatura()

    
    # VEHÍCULOS
    

    def ingresar_vehiculos(self):

        cantidad = self.interfaz.obtener_cantidad()

        self.simulacion.ingresar_vehiculos(
            cantidad
        )

        total = self.vehiculos.cantidad_total()

        self.interfaz.actualizar_mensaje(
            f"Se ingresaron {cantidad} vehículo(s) a la cola."
        )

        self.actualizar_interfaz()

        self.dibujar()

   
    # VELOCIDAD
   
    def cambiar_velocidad(self, valor):

        try:
            self.velocidad_actual = float(valor)

        except ValueError:
            self.velocidad_actual = 2.0

  
    # ENCENDER SISTEMA
    

    def encender_sistema(self):

        self.simulacion.encender_sistema()

        self.interfaz.actualizar_estado(
            "ENCENDIDO"
        )

        self.interfaz.actualizar_mensaje(
            "Sistema encendido. Resistencias activas."
        )

        self.dibujar()

    
    # INICIAR SECADO
   

    def iniciar_secado(self):

        if not self.simulacion.esta_encendido():

            self.interfaz.actualizar_mensaje(
                "Primero debes encender el sistema."
            )

            return

        self.simulacion.iniciar_secado()

        self.interfaz.actualizar_estado(
            "SECANDO"
        )

        self.interfaz.actualizar_mensaje(
            "Proceso de secado iniciado."
        )

   
    # DETENER
   

    def detener(self):

        self.simulacion.detener()

        if self.simulacion.esta_encendido():

            self.interfaz.actualizar_estado(
                "ENCENDIDO"
            )

        else:

            self.interfaz.actualizar_estado(
                "APAGADO"
            )

        self.interfaz.actualizar_mensaje(
            "Proceso detenido."
        )

   
    # REINICIAR temoeratura privisonal
  

    def reiniciar(self):

        self.simulacion.reiniciar()

        self.interfaz.actualizar_temperatura(
            25.0
        )

        self.interfaz.actualizar_estado(
            "APAGADO"
        )

        self.interfaz.actualizar_capacidad(
            0
        )

        self.interfaz.actualizar_mensaje(
            "Sistema listo para iniciar."
        )

        self.dibujar()

   
    # ACTUALIZACIÓN DEL MOVIMIENTO
    

    def actualizar_movimiento(self):

        self.simulacion.actualizar_movimiento(
            self.velocidad_actual
        )

        self.actualizar_interfaz()
        self.dibujar()

        self.root.after(
            30,
            self.actualizar_movimiento
        )

    
    # ACTUALIZACIÓN DE TEMPERATURA
   
    def actualizar_temperatura(self):

        self.simulacion.actualizar_temperatura()

        temperatura = (
            self.simulacion.obtener_temperatura()
        )

        self.interfaz.actualizar_temperatura(
            temperatura
        )

        self.root.after(
            500,
            self.actualizar_temperatura
        )


    # ACTUALIZAR INFORMACIÓN
    

    def actualizar_interfaz(self):

        cantidad = (
            self.vehiculos.cantidad_dentro()
        )

        self.interfaz.actualizar_capacidad(
            cantidad
        )

    
    # DIBUJAR TODO
    

    def dibujar(self):

        canvas = self.interfaz.area_simulacion

        canvas.delete("all")

        self.cabina.dibujar_cabina()

        self.resistencias.dibujar()

        self.vehiculos.dibujar()

# INICIAR PROGRAMA

if __name__ == "__main__":

    root = tk.Tk()

    app = Aplicacion(root)

    root.mainloop()