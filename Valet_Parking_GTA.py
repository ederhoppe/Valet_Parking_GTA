"""Valet Parking - GTA"""

import os
import json

print('Bienvenido al Valet Parking de GTA Online\n')

class Vehiculo: 
    def __init__(self, nombre):
        self.nombre = nombre.strip().title()

    def to_dict(self):
        return {"nombre": self.nombre}

class Garage:
    def __init__(self, nombre, capacidad_maxima):
        self.nombre = nombre.strip().title()
        self.capacidad_maxima = int(capacidad_maxima)
        self.vehiculos = []

    @property
    def espacio_disponible(self):
        return self.capacidad_maxima - len(self.vehiculos)

    def agregar_vehiculo(self, vehiculo):
        if self.espacio_disponible > 0: 
            self.vehiculos.append(vehiculo)
            return True
        return False

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "vehiculos": [v.to_dict() for v in self.vehiculos],
            "capacidad_maxima": self.capacidad_maxima
        }

class GestorGTA: 
    def __init__(self, archivo_db="garages_gta.json"):
        self.archivo_db = archivo_db
        self.garages = []
        self.cargar_datos()

    def existe_vehiculo(self, nombre_vehiculo):
        nombre_normalizado = nombre_vehiculo.strip().lower()
        for g in self.garages:
            for v in g.vehiculos: 
                if v.nombre.lower() == nombre_normalizado:
                    return g.nombre
        return None

    def agregar_garage(self, nombre, capacidad):
        garage = Garage(nombre, capacidad)
        self.garages.append(garage)
        self.guardar_datos()
        print(f'El garaje "{garage.nombre}" tiene capacidad de {capacidad} vehículos.')

    def registrar_coche(self, nombre_coche, nombre_garage):
        # 1. Valida si existen duplicados 
        garage_actual = self.existe_vehiculo(nombre_coche)
        if garage_actual:
            print(f'El vehículo "{nombre_coche}" ya se encuentra en "{garage_actual}".')
            return
        
        # 2. Busca garage destino
        garage_destino = next((g for g in self.garages if g.nombre.lower() == nombre_garage.strip().lower()), None)
        if not garage_destino: 
            print(f'El garaje "{nombre_garage}" no existe.')
            return

        # 3. Agrega el vehículo 
        coche = Vehiculo(nombre_coche)
        if garage_destino.agregar_vehiculo(coche):
            self.guardar_datos()
            print(f'"{coche.nombre}" guardado en "{garage_destino.nombre}". Espacio restante: {garage_destino.espacio_disponible}')
        else:
            print(f'El garaje "{garage_destino.nombre}" está LLENO ({garage_destino.capacidad_maxima}/{garage_destino.capacidad_maxima}).')

    def mostrar_inventario(self):
        print("\n" + "="*45)
        print("     INVENTARIO DE GARAJES Y VEHÍCULOS GTA")
        print("="*45)
        if not self.garages:
            print("No hay garajes registrados aún.")
            print("="*45 + "\n")
            return

        for g in self.garages:
            print(f"\n🏢 Garaje: {g.nombre}")
            print(f"   Capacidad: {len(g.vehiculos)}/{g.capacidad_maxima} (Disponibles: {g.espacio_disponible})")
            if g.vehiculos:
                for idx, v in enumerate(g.vehiculos, 1):
                    print(f"   └─ [{idx}] {v.nombre}")
            else:
                print("   └─ (Garaje vacío)")
        print("="*45 + "\n")

    def guardar_datos(self):
        datos = [g.to_dict() for g in self.garages]
        with open(self.archivo_db, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        if not os.path.exists(self.archivo_db):
            return
        try:
            with open(self.archivo_db, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for g_data in datos:
                    garaje = Garage(g_data["nombre"], g_data["capacidad_maxima"])
                    for v_data in g_data["vehiculos"]:
                        garaje.vehiculos.append(Vehiculo(v_data["nombre"]))
                    self.garages.append(garaje)
        except Exception as e:
            print(f"Error al cargar datos: {e}")

# Ejemplo de ejecución e ingreso de datos
if __name__ == "__main__":
    app = GestorGTA()

    # Si la lista de garajes está vacía, agregamos los garajes por primera vez
    if not app.garages:
        app.agregar_garage("Departamento Eclipse Towers", 10)
        app.agregar_garage("Taller de Garaje (Agency)", 20)

    # Registro de vehículos
    app.registrar_coche("Elegy RH8", "Departamento Eclipse Towers")
    app.registrar_coche("Zentorno", "Departamento Eclipse Towers")
    
    # Intento de registrar un duplicado
    app.registrar_coche("Zentorno", "Taller de Garaje (Agency)")

    # Mostrar inventario completo
    app.mostrar_inventario()
