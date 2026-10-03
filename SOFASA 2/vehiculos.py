class Vehiculos:

    def __init__(self, cabina):
        self.cabina = cabina

        self.vehiculos = []
        self.cola_vehiculos = []

        self.max_vehiculos = 10
        self.proximo_numero = 1

        # Distancia mínima entre vehículos
        self.distancia_minima = 2.8

    def ingresar(self, cantidad):

        disponibles = (
            self.max_vehiculos
            - len(self.vehiculos)
            - len(self.cola_vehiculos)
        )

        cantidad = min(cantidad, disponibles)

        for _ in range(cantidad):

            self.cola_vehiculos.append(
                self.proximo_numero
            )

            self.proximo_numero += 1

        self.intentar_ingreso()

    def intentar_ingreso(self):

        if not self.cola_vehiculos:
            return

        # Si no hay vehículos dentro, entra directamente el primero.
        if not self.vehiculos:

            numero = self.cola_vehiculos.pop(0)

            self.vehiculos.append({
                "numero": numero,
                "x": -6.0,
                "z": 0
            })

            return

        # Buscar el vehículo que está más cerca de la entrada.
        vehiculo_entrada = min(
            self.vehiculos,
            key=lambda v: v["x"]
        )

        # El siguiente vehículo solo puede entrar
        # cuando exista suficiente espacio.
        posicion_entrada = -6.0

        distancia = (
            vehiculo_entrada["x"]
            - posicion_entrada
        )

        if distancia < self.distancia_minima:
            return

        numero = self.cola_vehiculos.pop(0)

        self.vehiculos.append({
            "numero": numero,
            "x": posicion_entrada,
            "z": 0
        })

    def mover(self, velocidad):

        if not self.vehiculos:

            self.intentar_ingreso()

            return

        # Ordenamos del que va adelante
        # al que va atrás.
        self.vehiculos.sort(
            key=lambda v: v["x"],
            reverse=True
        )

        desplazamiento = velocidad * 0.03

        for i, vehiculo in enumerate(self.vehiculos):

            nueva_x = (
                vehiculo["x"]
                + desplazamiento
            )

            # Si hay un vehículo adelante,
            # respetar la distancia mínima.
            if i > 0:

                vehiculo_anterior = (
                    self.vehiculos[i - 1]
                )

                posicion_maxima = (
                    vehiculo_anterior["x"]
                    - self.distancia_minima
                )

                nueva_x = min(
                    nueva_x,
                    posicion_maxima
                )

            vehiculo["x"] = nueva_x

        # Eliminar vehículos que ya salieron
        # de la cabina.
        vehiculos_dentro = []

        for vehiculo in self.vehiculos:

            if vehiculo["x"] <= 6.8:

                vehiculos_dentro.append(
                    vehiculo
                )

        self.vehiculos = vehiculos_dentro

        # Intentar ingresar el siguiente
        # vehículo de la cola.
        self.intentar_ingreso()

    def dibujar(self):

        for vehiculo in self.vehiculos:

            self.dibujar_vehiculo(
                vehiculo["x"],
                vehiculo["z"],
                vehiculo["numero"]
            )

    def dibujar_vehiculo(
        self,
        x,
        z,
        numero
    ):

        # Cuerpo
        self.cabina.cubo(
            x,
            -1.25,
            z,
            2.0,
            0.8,
            3.0,
            "#3d82ff"
        )

        # Parte superior
        self.cabina.cubo(
            x - 0.1,
            -0.75,
            z,
            1.2,
            0.45,
            2.4,
            "#5aa0ff"
        )

        # Parte delantera
        self.cabina.cubo(
            x - 0.1,
            -0.72,
            z - 1.22,
            0.8,
            0.25,
            0.05,
            "#15151d"
        )

        # Parte trasera
        self.cabina.cubo(
            x - 0.1,
            -0.72,
            z + 1.22,
            0.8,
            0.25,
            0.05,
            "#15151d"
        )

        # Ruedas
        posiciones_x = [
            x - 0.65,
            x + 0.65
        ]

        posiciones_z = [
            z - 1.5,
            z + 1.5
        ]

        for rueda_x in posiciones_x:

            for rueda_z in posiciones_z:

                self.cabina.cubo(
                    rueda_x,
                    -1.85,
                    rueda_z,
                    0.35,
                    0.25,
                    0.55,
                    "#15151d"
                )

        # Número del vehículo
        px, py, _ = self.cabina.proyectar(
            x,
            -0.25,
            z
        )

        self.cabina.canvas.create_text(
            px,
            py,
            text=f"V{numero}",
            fill="white",
            font=("Arial", 10, "bold")
        )

    def reiniciar(self):

        self.vehiculos.clear()
        self.cola_vehiculos.clear()

        self.proximo_numero = 1

    def cantidad_dentro(self):

        return len(self.vehiculos)

    def cantidad_total(self):

        return (
            len(self.vehiculos)
            + len(self.cola_vehiculos)
        )