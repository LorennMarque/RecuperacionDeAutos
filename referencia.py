import matplotlib.pyplot as plt
import numpy as np

# Definición de la base de datos
productos = ['Smartphone', 'Laptop', 'Tablet', 'Auriculares', 'Smartwatch']
cantidad_vendida = [150, 80, 200, 300, 120]
precio_venta = [700, 1200, 450, 150, 250]

# Creación de los gráficWos
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Gráfico de barras para la cantidad vendida por producto
axs[0].bar(productos, cantidad_vendida, color='blue')
axs[0].set_title('Cantidad Vendida por Producto')
axs[0].set_xlabel('Producto')
axs[0].set_ylabel('Cantidad Vendida')

# Gráfico de líneas para mostrar la relación entre cantidad vendida y precio de venta
axs[1].plot(productos, precio_venta, label='Precio de Venta (USD)', color='red', marker='o')
axs[1].set_title('Precio de Venta por Producto')
axs[1].set_xlabel('Producto')
axs[1].set_ylabel('Precio de Venta (USD)')

plt.tight_layout()
plt.show()