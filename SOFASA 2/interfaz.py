import tkinter as tk


class Interfaz:

    def __init__(
        self,
        root,
        ingresar_vehiculos,
        cambiar_velocidad,
        encender_sistema,
        iniciar_secado,
        detener,
        reiniciar
    ):
        self.root = root

        # main conectado 
        self.ingresar_vehiculos = ingresar_vehiculos
        self.cambiar_velocidad = cambiar_velocidad
        self.encender_sistema = encender_sistema
        self.iniciar_secado = iniciar_secado
        self.detener = detener
        self.reiniciar = reiniciar

        # Variables visuales
        self.temperatura = tk.StringVar(value="25 °C")
        self.estado = tk.StringVar(value="Estado: APAGADO")
        self.capacidad = tk.StringVar(
            value="Vehículos dentro: 0 / 10"
        )
        self.mensaje = tk.StringVar(
            value="Sistema listo para iniciar."
        )

        self.crear_interfaz()

    def crear_interfaz(self):

   
        # VENTANA PRINCIPAL
        

        self.root.title(
            "Simulador - Cabina de Secado de Pintura"
        )

        self.root.geometry("1200x750")
        self.root.minsize(1000, 650)
        self.root.configure(bg="#101018")

    
        # TÍTULO

        titulo = tk.Label(
            self.root,
            text="CABINA DE SECADO DE PINTURA",
            bg="#101018",
            fg="white",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            pady=(15, 10)
        )

        # CONTENEDOR PRINCIPAL
       

        contenedor = tk.Frame(
            self.root,
            bg="#101018"
        )

        contenedor.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

      
        # ÁREA DE SIMULACIÓN
       
        self.area_simulacion = tk.Canvas(
            contenedor,
            bg="#181820",
             highlightthickness=0
)

        self.area_simulacion.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
)

       
        # PANEL DE CONTROL
       

        self.panel_control = tk.Frame(
            contenedor,
            bg="#181820",
            width=300
        )

        self.panel_control.pack(
            side="right",
            fill="y"
        )

        self.panel_control.pack_propagate(False)

        self.crear_panel_control()

    def crear_panel_control(self):

        
        # VEHÍCULOS
        
        tk.Label(
            self.panel_control,
            text="CANTIDAD DE VEHÍCULOS",
            bg="#181820",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(
            pady=(20, 5)
        )

        self.entrada_vehiculos = tk.Entry(
            self.panel_control,
            bg="#101018",
            fg="white",
            insertbackground="white",
            justify="center",
            font=("Arial", 12)
        )

        self.entrada_vehiculos.insert(
            0,
            "1"
        )

        self.entrada_vehiculos.pack(
            padx=20,
            fill="x"
        )

        tk.Button(
            self.panel_control,
            text="INGRESAR VEHÍCULOS",
            command=self.ingresar_vehiculos,
            bg="#30303a",
            fg="white",
            activebackground="#40404c",
            activeforeground="white"
        ).pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # VELOCIDAD
       
        tk.Label(
            self.panel_control,
            text="VELOCIDAD",
            bg="#181820",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(
            pady=(15, 5)
        )

        self.velocidad = tk.Scale(
            self.panel_control,
            from_=0.5,
            to=5.0,
            resolution=0.5,
            orient="horizontal",
            bg="#181820",
            fg="white",
            highlightthickness=0,
            troughcolor="#30303a",
            command=self.cambiar_velocidad
        )

        self.velocidad.set(2.0)

        self.velocidad.pack(
            padx=20,
            fill="x"
        )

       
        # TEMPERATURA
      

        tk.Label(
            self.panel_control,
            text="TEMPERATURA",
            bg="#181820",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            self.panel_control,
            textvariable=self.temperatura,
            bg="#181820",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack()

        
        # ESTADO
        

        tk.Label(
            self.panel_control,
            textvariable=self.estado,
            bg="#181820",
            fg="#bbbbc5",
            font=("Arial", 11)
        ).pack(
            pady=10
        )

       
        # BOTONES PRINCIPALES
        

        tk.Button(
            self.panel_control,
            text="ENCENDER SISTEMA",
            command=self.encender_sistema,
            bg="#30303a",
            fg="white",
            activebackground="#40404c",
            activeforeground="white"
        ).pack(
            padx=20,
            pady=5,
            fill="x"
        )

        tk.Button(
            self.panel_control,
            text="INICIAR SECADO",
            command=self.iniciar_secado,
            bg="#30303a",
            fg="white",
            activebackground="#40404c",
            activeforeground="white"
        ).pack(
            padx=20,
            pady=5,
            fill="x"
        )

        tk.Button(
            self.panel_control,
            text="DETENER",
            command=self.detener,
            bg="#30303a",
            fg="white",
            activebackground="#40404c",
            activeforeground="white"
        ).pack(
            padx=20,
            pady=5,
            fill="x"
        )

        tk.Button(
            self.panel_control,
            text="REINICIAR",
            command=self.reiniciar,
            bg="#30303a",
            fg="white",
            activebackground="#40404c",
            activeforeground="white"
        ).pack(
            padx=20,
            pady=5,
            fill="x"
        )

        
        # CAPACIDAD
        

        tk.Label(
            self.panel_control,
            textvariable=self.capacidad,
            bg="#181820",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(
            pady=(20, 5)
        )

        # MENSAJE

        tk.Label(
            self.panel_control,
            textvariable=self.mensaje,
            bg="#181820",
            fg="#aaaaaf",
            wraplength=250,
            justify="center",
            font=("Arial", 10)
        ).pack(
            padx=20,
            pady=10
        )

    # ACTUALIZAR INFORMACIÓN

    def actualizar_temperatura(self, temperatura):
        self.temperatura.set(
            f"{temperatura:.1f} °C"
        )

    def actualizar_estado(self, estado):
        self.estado.set(
            f"Estado: {estado}"
        )

    def actualizar_capacidad(self, cantidad):
        self.capacidad.set(
            f"Vehículos dentro: {cantidad} / 10"
        )

    def actualizar_mensaje(self, mensaje):
        self.mensaje.set(
            mensaje
        )

    def obtener_cantidad(self):
        try:
            cantidad = int(
                self.entrada_vehiculos.get()
            )

            if cantidad < 1:
                return 1

            if cantidad > 10:
                return 10

            return cantidad

        except ValueError:
            return 1

    def obtener_velocidad(self):
        return self.velocidad.get()