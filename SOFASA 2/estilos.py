class Estilos:

   
    # COLORES PRINCIPALES
    

    FONDO = "#101018"
    FONDO_PANEL = "#181820"
    FONDO_BOTON = "#30303a"
    FONDO_BOTON_ACTIVO = "#40404c"

    BLANCO = "white"
    GRIS_CLARO = "#bbbbc5"
    GRIS = "#aaaaaf"

   
    # FUENTES
   

    FUENTE_TITULO = (
        "Arial",
        20,
        "bold"
    )

    FUENTE_SUBTITULO = (
        "Arial",
        11,
        "bold"
    )

    FUENTE_NORMAL = (
        "Arial",
        10
    )

    FUENTE_TEMPERATURA = (
        "Arial",
        18,
        "bold"
    )

    FUENTE_ESTADO = (
        "Arial",
        11
    )

    FUENTE_VEHICULO = (
        "Arial",
        10,
        "bold"
    )

    # CONFIGURACIÓN DE BOTONES
    
    @classmethod
    def boton(cls):
        return {
            "bg": cls.FONDO_BOTON,
            "fg": cls.BLANCO,
            "activebackground": cls.FONDO_BOTON_ACTIVO,
            "activeforeground": cls.BLANCO
        }

   
    # CONFIGURACIÓN DE ENTRADAS
    

    @classmethod
    def entrada(cls):
        return {
            "bg": cls.FONDO,
            "fg": cls.BLANCO,
            "insertbackground": cls.BLANCO,
            "justify": "center"
        }

    
    # CONFIGURACIÓN DEL SLIDER
    

    @classmethod
    def escala(cls):
        return {
            "bg": cls.FONDO_PANEL,
            "fg": cls.BLANCO,
            "highlightthickness": 0,
            "troughcolor": cls.FONDO_BOTON
        }