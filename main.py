class Asiento:

    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro


    def cambiarColor(self, color):

        colores = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']

        if color in colores:

           self.color = color
            
class Motor:

    def __init__(self, numeroCilindro, tipo, registro):
        self.numeroCilindro = numeroCilindro
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):

        if  type(registro) == int:

            self.registro = registro

    def asignarTipo(self, tipo):

        tipos = ['electrico', 'gasolina']

        if tipo in tipos:
            self.tipo = tipo


class Auto:

    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados = None):
        
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados


    def cantidadAsientos(self):

        n_asientos = 0

        for asiento in self.asientos:
            if asiento != None:
                n_asientos += 1

        return n_asientos

    def verificarIntegridad(self):

        if self.registro == self.motor.registro:

            for r_asiento in list(self.asientos):

                if r_asiento.registro != self.registro:
                    return "Las piezas no son originales"


            return "Auto original"

        else:

            return "Las piezas no son originales" 

