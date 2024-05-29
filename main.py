from datetime import datetime
import matplotlib as plt
import numpy as np
import csv

def clean_quotes(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        rows = list(reader)

    with open(output_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in rows:
            cleaned_row = [cell.replace('"', '') for cell in row]
            writer.writerow(cleaned_row)

    print("✅😉 Datos Limpios")

input_file = 'data.csv'
output_file = 'clean.csv'
# clean_quotes(input_file, output_file)  # CORRER ESTO PARA LIMPIAR ARCHIVOS

def type_corrections():
    with open(output_file, mode='r', newline='', encoding='utf-8-sig') as f:
        data = csv.reader(f)
        next(data) #Saltear el título
        for row in data:
            #Convertir fechas
            row[1] = datetime.strptime(row[1],'%Y-%m-%d')
            row[2] = datetime.strptime(row[2],'%Y-%m-%d')

            #Convertir números
            row[3] = int(row[3])
            row[7] = int(row[3])
            row[10] = int(row[3])
            row[12] = int(row[3])
            row[14] = int(row[3])
            row[20] = int(row[3])
            row[22] = int(row[3])
            row[23] = int(row[3])

    print("🔥 Corrected")

# Porcentajes de recupero por provincia
# Denuncias de Recuperados / robos , comparación diaria => [El tipo de denunicas] doble line chart
# Regiones con más denuncias