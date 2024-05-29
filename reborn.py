from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import csv
import csv
from datetime import datetime

def clean_quotes(input_file, output_file):
    rows = []

    with open(input_file, mode='r', newline='', encoding='utf-8-sig') as f:
        data = csv.reader(f)
        header = next(data) 
        for row in data:
            if row[0] != "tramite_tipo":
                cleaned_row = [cell.replace('"', '') for cell in row]
                cleaned_row[1] = datetime.strptime(cleaned_row[1], '%Y-%m-%d')
                cleaned_row[2] = datetime.strptime(cleaned_row[2], '%Y-%m-%d')
                
                # Convertir números
                cleaned_row[3] = int(cleaned_row[3])
                cleaned_row[14] = int(cleaned_row[14])
                cleaned_row[20] = int(cleaned_row[20])
                cleaned_row[22] = int(cleaned_row[22])
                cleaned_row[23] = int(cleaned_row[23])

                rows.append(cleaned_row)
            else:
                header = [cell.replace('"', '') for cell in row]

    # Ordenar las filas por cleaned_row[1] (la fecha)
    rows.sort(key=lambda x: x[1])

    with open(output_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)  # Escribir el encabezado
        for row in rows:
            # Convertir la fecha de nuevo a string para escribir en el CSV
            row[1] = row[1].strftime('%Y-%m-%d')
            row[2] = row[2].strftime('%Y-%m-%d')
            writer.writerow(row)

input_file = 'data.csv'
output_file = 'output.csv'
# clean_quotes(input_file, output_file)

# Cantidad de recupero por provincia
def recuperados_por_provincia(provincias, cantidad_recuperos ):
    # Creación de los gráficos
    fig, axs = plt.subplots(1, 1, figsize=(10, 6))  # 1 fila, 1 columna

    # Gráfico de barras para la cantidad vendida por producto
    axs.bar(provincias, cantidad_recuperos, color='blue')
    axs.set_title('Cantidad de recupero por provincia')
    axs.set_xlabel('Provincias')
    axs.set_ylabel('Cantidad de recuperos')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

provincias_recuperos = {}
with open(output_file, mode='r', newline='', encoding='utf-8') as f:
    data = csv.reader(f)
    next(data)
    for row in data:
        if row[5] not in provincias_recuperos:
            cantidad_recuperos = 0
            # provincias_recuperos.append(row[5])
            if row[0] == "COMUNICACIÓN DE RECUPERO":
                cantidad_recuperos += 1

            provincias_recuperos[row[5]] = cantidad_recuperos
        else:
            if row[0] == "COMUNICACIÓN DE RECUPERO":
                provincias_recuperos[row[5]] += 1


provincias = provincias_recuperos.keys()
recuperos= provincias_recuperos.values()

recuperados_por_provincia(provincias, recuperos)

# # Denuncias de Recuperados / robos , comparación diaria => [El tipo de denunicas] doble line chart
def denuncias_recuperados_robos(cantidad_denuncias, fechas):
    fig, axs = plt.subplots(1, 1, figsize=(10, 6))  # 1 fila, 1 columna
    axs.plot(cantidad_denuncias, fechas, color='red', marker='o')
    axs.set_title('Denuncias Diarias en Enero')
    axs.set_xlabel('Días')
    axs.set_ylabel('Cantidad de denuncias')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

cantidad_denuncias_fechas = {}
print(cantidad_denuncias_fechas)

for day in range(31):
    if day < 10:
        fecha_actual = f"2022-01-0{day}"
    else:
        fecha_actual = f"2022-01-{day}"

    cantidad_denuncias_fechas[fecha_actual] = 0

print(cantidad_denuncias_fechas)

with open(output_file, mode='r', newline='', encoding='utf-8') as f:
    data = csv.reader(f)
    next(data)
    for row in data:
        if row[1] not in cantidad_denuncias_fechas:
            denuncias = 0
            # provincias_recuperos.append(row[5])
            if row[0] == "DENUNCIA DE ROBO O HURTO / RETENCION INDEBIDA":
                denuncias += 1

            cantidad_denuncias_fechas[row[1]] = denuncias
        else:
            if row[0] == "DENUNCIA DE ROBO O HURTO / RETENCION INDEBIDA":
                cantidad_denuncias_fechas[row[1]] += 1

cantidad_denuncias = cantidad_denuncias_fechas.keys()
fechas= cantidad_denuncias_fechas.values()

denuncias_recuperados_robos(cantidad_denuncias, fechas)

def regiones_con_mas_denuncias(regiones, cantidad_denuncias):
    print(f"{regiones=}")
    print(f"{cantidad_denuncias}")

    # Creación de los gráficWos
    fig, axs = plt.subplots(1, 1, figsize=(10, 15))

    # Gráfico de barras para la cantidad vendida por producto
    axs.bar(regiones, cantidad_denuncias, color='red')   
    axs.set_title('Cantidad de denuncias por región (TOP 10)') 
    axs.set_xlabel('Regiones')
    axs.set_ylabel('Cantidad de denuncias')
    plt.tight_layout()
    plt.show()

cantidad_denuncias_regionales = {}
with open(output_file, mode='r', newline='', encoding='utf-8') as f:
    data = csv.reader(f)
    next(data)
    for row in data:
        if row[4] not in cantidad_denuncias_regionales:
            denuncias = 0
            if row[0] == "DENUNCIA DE ROBO O HURTO / RETENCION INDEBIDA":
                denuncias += 1

            cantidad_denuncias_regionales[row[4]] = denuncias
        else:
            if row[0] == "DENUNCIA DE ROBO O HURTO / RETENCION INDEBIDA":
                cantidad_denuncias_regionales[row[4]] += 1

regiones = cantidad_denuncias_regionales.keys()
cantidad_denuncias = cantidad_denuncias_regionales.values()


diccionario_ordenado_por_valores = sorted(cantidad_denuncias_regionales.items(), key=lambda item: item[1], reverse=True)

regiones = []
cantidad_denuncias = []

for i in range(10):
    region, denuncia = diccionario_ordenado_por_valores[i]
    regiones.append(region)
    cantidad_denuncias.append(denuncia)

regiones_con_mas_denuncias(regiones, cantidad_denuncias)
