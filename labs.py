#objetos principales
#habitacion: tipo(indubidual o doble) numero de habitacion, disponibilidad, reservante
#hotel gestionalisacion y reservacion de habitaciones
#huesped: nombre, identificacion, tiempo de estadia

#relaciones
#el huesped puede reservar una o mas habitaciones
#una habitacion solo puede ser reservada por una persona
#el hotel se encarga de gestionar que habitaciones estan disponibles y quienes las reservan

class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponible = True
        self.huesped = None

    def reservar(self, huesped):
        if self.disponible:
            self.disponible = False
            self.huesped = huesped
            print(f'Habitación {self.numero} reservada para {huesped.nombre}.')
        else:
            print(f'Lo siento, la habitación {self.numero} no está disponible.')

    def liberar(self):
        if not self.disponible:
            print(f'Habitación {self.numero} liberada. Estaba ocupada por {self.huesped.nombre}.')
            self.disponible = True
            self.huesped = None
        else:
            print(f'La habitación {self.numero} ya está libre.')

class Huesped:
    def __init__(self, nombre):
        self.nombre = nombre

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        disponibles = [h for h in self.habitaciones if h.disponible]
        if disponibles:
            print('Habitaciones disponibles:')
            for habitacion in disponibles:
                print(f'Habitación {habitacion.numero} - Tipo: {habitacion.tipo}')
        else:
            print('No hay habitaciones disponibles.')

    def reservar_habitacion(self, numero, huesped):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                habitacion.reservar(huesped)
                return
        print(f'La habitación {numero} no existe.')

# Ejemplo de uso
hotel = Hotel("Hotel Python")

# Crear habitaciones
habitacion1 = Habitacion(101, "Individual")
habitacion2 = Habitacion(102, "Doble")
habitacion3 = Habitacion(103, "Doble")

# Agregar habitaciones al hotel
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)
hotel.agregar_habitacion(habitacion3)

# Crear un huésped
huesped1 = Huesped("Juan Pérez")

# Mostrar habitaciones disponibles
hotel.mostrar_habitaciones_disponibles()

# Reservar una habitación
hotel.reservar_habitacion(101, huesped1)

# Mostrar habitaciones disponibles después de la reserva
hotel.mostrar_habitaciones_disponibles()

# Liberar la habitación
habitacion1.liberar()

# Mostrar habitaciones disponibles después de liberar
hotel.mostrar_habitaciones_disponibles()
