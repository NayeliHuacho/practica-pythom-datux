class Conductor:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.horarios = []  # Horarios ocupados por el conductor (solo horas, no fechas)

    def agregar_horario(self, horario):
        if horario not in self.horarios:
            self.horarios.append(horario)
        else:
            raise ValueError(f"El horario {horario} ya está asignado al conductor {self.nombre}.")


class Bus:
    def __init__(self, id, capacidad):
        self.id = id
        self.capacidad = capacidad
        self.ruta = None
        self.horarios = []  # Lista de horarios asignados al bus
        self.conductores_asignados = []

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, horario):
        if horario not in self.horarios:
            self.horarios.append(horario)
        else:
            raise ValueError(f"El horario {horario} ya está registrado para el bus {self.id}.")

    def asignar_conductor(self, conductor, horario):
        if horario not in self.horarios:
            raise ValueError(f"El horario {horario} no está registrado para el bus {self.id}.")
        if any(horario in c.horarios for c in self.conductores_asignados):
            raise ValueError(f"El horario {horario} ya está ocupado por otro conductor en el bus {self.id}.")
        conductor.agregar_horario(horario)
        self.conductores_asignados.append(conductor)


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, id, capacidad):
        self.buses.append(Bus(id, capacidad))

    def agregar_conductor(self, id, nombre):
        self.conductores.append(Conductor(id, nombre))

    def buscar_bus(self, id):
        return next((bus for bus in self.buses if bus.id == id), None)

    def buscar_conductor(self, id):
        return next((conductor for conductor in self.conductores if conductor.id == id), None)

    def menu(self):
        while True:
            print("\n--- Sistema de Gestión de Tickets de Buses ---")
            print("1. Agregar bus")
            print("2. Agregar ruta a bus")
            print("3. Registrar horario a bus")
            print("4. Agregar conductor")
            print("5. Agregar horario a conductor")
            print("6. Asignar bus a conductor")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            try:
                if opcion == "1":
                    id = input("Ingrese ID del bus: ")
                    capacidad = int(input("Ingrese capacidad del bus: "))
                    self.agregar_bus(id, capacidad)
                    print("Bus agregado correctamente.")

                elif opcion == "2":
                    id = input("Ingrese ID del bus: ")
                    bus = self.buscar_bus(id)
                    if not bus:
                        print("Bus no encontrado.")
                        continue
                    ruta = input("Ingrese la ruta del bus: ")
                    bus.agregar_ruta(ruta)
                    print("Ruta agregada correctamente.")

                elif opcion == "3":
                    id = input("Ingrese ID del bus: ")
                    bus = self.buscar_bus(id)
                    if not bus:
                        print("Bus no encontrado.")
                        continue
                    horario = input("Ingrese horario (HH:MM): ")
                    bus.registrar_horario(horario)
                    print("Horario registrado correctamente.")

                elif opcion == "4":
                    id = input("Ingrese ID del conductor: ")
                    nombre = input("Ingrese nombre del conductor: ")
                    self.agregar_conductor(id, nombre)
                    print("Conductor agregado correctamente.")

                elif opcion == "5":
                    id = input("Ingrese ID del conductor: ")
                    conductor = self.buscar_conductor(id)
                    if not conductor:
                        print("Conductor no encontrado.")
                        continue
                    horario = input("Ingrese horario (HH:MM): ")
                    conductor.agregar_horario(horario)
                    print("Horario agregado al conductor correctamente.")

                elif opcion == "6":
                    bus_id = input("Ingrese ID del bus: ")
                    conductor_id = input("Ingrese ID del conductor: ")
                    horario = input("Ingrese horario (HH:MM): ")

                    bus = self.buscar_bus(bus_id)
                    conductor = self.buscar_conductor(conductor_id)

                    if not bus:
                        print("Bus no encontrado.")
                        continue
                    if not conductor:
                        print("Conductor no encontrado.")
                        continue

                    bus.asignar_conductor(conductor, horario)
                    print("Conductor asignado al bus correctamente.")

                elif opcion == "7":
                    print("Saliendo del sistema.")
                    break

                else:
                    print("Opción no válida.")

            except ValueError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    admin = Admin()
    admin.menu()
