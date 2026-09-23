"""Valet Parking - GTA"""

import os

print('Bienvenido al Valet Parking de GTA Online')

#Base de datos para saber que vehiculo tengo y en que garage se encuentra. Evitemos duplicidad, a demas incluir los vehiculos del logro "Vive la vida"

class Vehiculo: 
    def __init__(self, nombre):
        self.nombre = nombre.strip().title()

    def to_dict(self):
        return{"nombre": self.nombre}

class Garage:
    def __init__(self, garage, capacidad_maxima):
        self.garage = garage.strip().title()
        self.capacidad_maxima = capacidad_maxima.strip().title()
        self.vehiculos = []

@property
def espacio_disponible(self):
    return self.capacidad_maxima - len(self.vehiculo)

def agregar_vehiculo(self, vehiculo):
    if self.espacio_disponible > 0: 
        self.vehiculos.append(vehiculo)
        return True
    return False

def to_dict(self):
    return{
        "garage": self.garage,
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
    print(f'El garaje {garage.nombre} tiene capacidad de {capacidad} vehiculos')

def registrar_coche(self, nombre_coche, nombre_garage):
    #1. Valida si existen duplicados 
    garage_actual = self.existe_vehiculo(nombre_coche)
    if garage_actual:
        print(f'El vehiculo {nombre_coche} ya se encuentra en {garage_actual}')
        return
    
    #2. Busca garage destino
    garage_destino = next((g for g in self.garages if g.nombre.lower() == nombre_garage.strip().lower()), None)
    if not garage_destino: 
        print(f'El garage {nombre_garage} no existe')
        return

    #3. Agrega el vehiculo 
    
