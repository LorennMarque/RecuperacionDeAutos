import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Función para cargar los datos
def cargar_datos(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        # Leer la primera línea para obtener los nombres de las columnas
        columnas = f.readline().strip().split('","')
        # Eliminar comillas dobles de los extremos
        columnas[0] = columnas[0].lstrip('"')
        columnas[-1] = columnas[-1].rstrip('"')
        # Lista para almacenar los datos
        datos = []
        # Leer las líneas restantes y dividirlas en columnas
        for linea in f:
            valores = linea.strip().split('","')
            # Eliminar comillas dobles de los extremos
            valores[0] = valores[0].lstrip('"')
            valores[-1] = valores[-1].rstrip('"')
            datos.append(valores)
    return columnas, datos

# Cargar los datos desde el archivo CSV
columnas, data = cargar_datos('data.csv')

# Obtener las fechas de tramite
fechas_tramite = [datetime.strptime(date, '%Y-%m-%d') for date in [row[1] for row in data]]

# Graficar la cantidad de trámites por día
plt.figure(figsize=(10, 5))
plt.hist(fechas_tramite, bins=31, color='skyblue')
plt.title('Cantidad de trámites por día')
plt.xlabel('Fecha')
plt.ylabel('Cantidad de trámites')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Graficar la cantidad de trámites por provincia
provincias = np.unique([row[5] for row in data])
cantidad_tramites_provincia = [np.sum([row[5] == provincia for row in data]) for provincia in provincias]

plt.figure(figsize=(10, 5))
plt.bar(provincias, cantidad_tramites_provincia, color='lightgreen')
plt.title('Cantidad de trámites por provincia')
plt.xlabel('Provincia')
plt.ylabel('Cantidad de trámites')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
