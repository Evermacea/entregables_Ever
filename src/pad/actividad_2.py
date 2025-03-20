import pandas as pd
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt # Importamos la librería para gráficos
import plotly.express as px # Importamos la librería para gráficos interactivos
import seaborn as sns
import os
from openpyxl import load_workbook

class Actividad_2(): # Una sola dimensión
    def __init__(self):
        self.ruta_raiz = "src/pad"
        self.ruta_actividad_2 = "{}/actividad_2/".format(self.ruta_raiz)
        self.ruta_guardado = os.path.join(self.ruta_actividad_2, "resultados.xlsx") 

        # Crear la carpeta si no existe
        if not os.path.exists(self.ruta_actividad_2):
            os.makedirs(self.ruta_actividad_2)
        np.random.seed(101) # Semilla para reproducibilidad

    def ejercicio1(self):
        array = np.arange(10, 30)  # Genera un array desde 10 hasta 29
        print(f'Solución del ejercicio 1: {array}')
        df = pd.DataFrame(array)  # Convierte el array en un DataFrame
        # Verifica si el archivo ya existe para evitar sobrescribirlo
        if os.path.exists(self.ruta_guardado):
            with pd.ExcelWriter(self.ruta_guardado, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
                df.to_excel(writer, sheet_name="Hoja1", index=False, header=False)
        else:
            df.to_excel(self.ruta_guardado, sheet_name="Hoja1", index=False, header=False, engine="openpyxl")


    def ejercicio2(self):
        matriz = np.ones((10, 10))  # Crea una matriz de 10x10 llena de unos
        suma = np.sum(matriz)  # Calcula la suma de todos los elementos
        print(f'Solución del ejercicio 2 : {suma}')
        df = pd.DataFrame([[suma]])  # Convertir el resultado en DataFrame con una celda
        # Verifica si el archivo ya existe para evitar sobrescribirlo
        if os.path.exists(self.ruta_guardado):
            with pd.ExcelWriter(self.ruta_guardado, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
                df.to_excel(writer, sheet_name="Hoja2", index=False, header=False)
        else:
            df.to_excel(self.ruta_guardado, sheet_name="Hoja2", index=False, header=False, engine="openpyxl")


    def ejercicio3(self):
        array1 = np.random.randint(1, 11, 5)  # Genera 5 números aleatorios entre 1 y 10
        array2 = np.random.randint(1, 11, 5)  # Genera otro array con 5 números aleatorios entre 1 y 10
        producto = array1 * array2  # Producto elemento a elemento
        print("Array 1:", array1)
        print("Array 2:", array2)
        print("Solución ejercicio 3 :", producto)

        # Convertir los datos en un DataFrame
        df = pd.DataFrame({"Array1": array1, "Array2": array2, "Producto": producto})
        # Verifica si el archivo ya existe para evitar sobrescribirlo
        if os.path.exists(self.ruta_guardado):
            with pd.ExcelWriter(self.ruta_guardado, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
                df.to_excel(writer, sheet_name="Hoja3", index=False)
        else:
            df.to_excel(self.ruta_guardado, sheet_name="Hoja3", index=False, engine="openpyxl")

    def ejercicio4(self):
        matriz = np.fromfunction(lambda i, j: (i+1) + (j+1), (4, 4))  # Crea la matriz 4x4 con valores i+j
        print("Solución ejercicio 4: \nMatriz generada:\n", matriz)
        determinante = np.linalg.det(matriz)  # Calcula el determinante

        # Creamos listas organizadas para que el DataFrame tenga un buen formato
        datos = []
        datos.append(["Matriz generada:"])
        datos.extend(matriz.tolist())  # Agregamos la matriz
        datos.append([])  # Fila vacía
        datos.append(["Determinante:", determinante])  # Determinante

        try:
            inversa = np.linalg.inv(matriz)  # Calcula la inversa
            print("Inversa de la matriz:\n", inversa)
            datos.append([])  # Fila vacía
            datos.append(["Inversa de la matriz:"])
            datos.extend(inversa.tolist())  # Agregamos la matriz inversa
        except np.linalg.LinAlgError:
            datos.append([])  # Fila vacía
            datos.append([f'Para este caso, la matriz no tiene inversa. Ya que su determinante es: {determinante}.'])  # Mensaje en caso de no tener inversa

        # Convertimos la lista estructurada en un DataFrame
        df_resultado = pd.DataFrame(datos)

        # Guardamos en la hoja 4 del archivo Excel sin sobrescribir el archivo completo
        with pd.ExcelWriter(self.ruta_guardado, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
            df_resultado.to_excel(writer, sheet_name="Hoja4", index=False, header=False)


    def ejercicio5(self):
        array = np.random.rand(100)  # Generamos 100 números aleatorios entre 0 y 1
        max_valor = np.max(array)  # Valor máximo
        min_valor = np.min(array)  # Valor mínimo
        max_indice = np.argmax(array)  # Índice del valor máximo
        min_indice = np.argmin(array)  # Índice del valor mínimo
        
        print("Solución del ejercicio 5 \nArray :\n", array)
        print(f"Valor máximo: {max_valor} índice {max_indice}")
        print(f"Valor mínimo: {min_valor} índice {min_indice}")
        datos = [] # Creamos los datos organizados en una lista
        datos.append(["Array generado:"])
        datos.extend([[valor] for valor in array])  # Agregamos los valores del array en una columna
        datos.append([])  # Fila vacía
        datos.append(["Valor máximo:", max_valor, "Índice:", max_indice])
        datos.append(["Valor mínimo:", min_valor, "Índice:", min_indice])
        df_resultado = pd.DataFrame(datos) # Convertimos la lista en un DataFrame

        # Guardamos en la Hoja5 del Excel sin sobrescribir el archivo completo
        with pd.ExcelWriter(self.ruta_guardado, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
            df_resultado.to_excel(writer, sheet_name="Hoja5", index=False, header=False)

    def ejercicio6(self):
        array_3x1 = np.array([[1], [2], [3]])  # Matriz de 3 filas y 1 columna
        array_1x3 = np.array([[4, 5, 6]])  # Matriz de 1 fila y 3 columnas
        resultado = array_3x1 + array_1x3  # Broadcasting para obtener una matriz 3x3
        print("Solución del ejercicio 6 \nArray 3x1:\n", array_3x1)
        print("Array 1x3:\n", array_1x3)
        print("Suma con broadcasting:\n", resultado)
        # Organizar los datos en listas para el Excel
        datos = [["Array 3x1:"]] + array_3x1.tolist() + [[]]  # Separa con una fila vacía
        datos += [["Array 1x3:"]] + array_1x3.tolist() + [[]]  
        datos += [["Suma con broadcasting:"]] + resultado.tolist()  
        df_resultado = pd.DataFrame(datos) # Convertimos la lista en DataFrame
        # Guardamos en la Hoja6 del Excel sin sobrescribir el archivo completo
        with pd.ExcelWriter(self.ruta_guardado, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
            df_resultado.to_excel(writer, sheet_name="Hoja6", index=False, header=False)


    def ejercicio7(self):
        matriz_5x5 = np.arange(1, 26).reshape(5, 5)  # Matriz de 5x5 con valores del 1 al 25
        submatriz_2x2 = matriz_5x5[1:3, 1:3]  # Extraemos desde la segunda fila y segunda columna
        print("Solución del ejercicio 7 \nMatriz 5x5:\n", matriz_5x5)
        print("Submatriz 2x2 extraída:\n", submatriz_2x2)
        # Convertimos en listas para estructurarlo en el Excel
        datos = [["Matriz 5x5:"]] + matriz_5x5.tolist() + [[]]
        datos += [["Submatriz 2x2 extraída:"]] + submatriz_2x2.tolist()
        # Guardamos en la Hoja7 del Excel sin sobrescribir el archivo completo
        with pd.ExcelWriter(self.ruta_guardado, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
            pd.DataFrame(datos).to_excel(writer, sheet_name="Hoja7", index=False, header=False)


    def ejercicio8(self):
        array_zeros = np.zeros(10, dtype=int)  # Array de 10 ceros
        print("Solución del ejercicio 8 \nArray original:\n", array_zeros)
        array_modificado = array_zeros.copy()  # Hacemos una copia antes de modificar
        array_modificado[3:7] = 5  # Modificamos los valores de los índices 3 a 6
        print("Array modificado:\n", array_modificado)
        # Estructuramos los datos para el Excel
        datos = [
            ["Array original:"],
            [", ".join(map(str, array_zeros))],  # Guardamos el original
            [],
            ["Array modificado:"],
            [", ".join(map(str, array_modificado))]  # Guardamos el modificado
        ]
        # Guardamos en la Hoja8 del Excel sin afectar otras hojas
        with pd.ExcelWriter(self.ruta_guardado, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
            pd.DataFrame(datos).to_excel(writer, sheet_name="Hoja8", index=False, header=False)

    def ejercicio9(self):
        matriz = np.arange(1, 10).reshape(3, 3)  # Matriz 3x3 con valores del 1 al 9
        print("Solución del ejercicio 9 \nMatriz original:\n", matriz)

        matriz_invertida = matriz[::-1]  # Invierte el orden de las filas
        print("\nMatriz con filas invertidas:\n", matriz_invertida)

        # Estructuramos los datos para el Excel
        datos = [
            ["Matriz original:"],
            *matriz.tolist(),
            [],
            ["Matriz con filas invertidas:"],
            *matriz_invertida.tolist()
        ]
        # Guardamos en la Hoja9 del Excel sin afectar las demás hojas
        with pd.ExcelWriter(self.ruta_guardado, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
            pd.DataFrame(datos).to_excel(writer, sheet_name="Hoja9", index=False, header=False)

    def ejercicio10(self):
        array = np.random.rand(10)  # Crea un array de 10 números aleatorios entre 0 y 1
        print("Solución del ejercicio 10 \nArray original:\n", array)

        mayores_a_05 = array[array > 0.5]  # Filtra solo los valores mayores a 0.5
        print("\nValores mayores a 0.5:\n", mayores_a_05)

        # Estructuramos los datos para que cada número esté en su propia celda
        datos = [["Array original:"]] + [[num] for num in array] + [[""], ["Valores mayores a 0.5:"]] + [[num] for num in mayores_a_05]

        # Si no hay valores mayores a 0.5, agregamos un mensaje
        if mayores_a_05.size == 0:
            datos.append(["No hay valores mayores a 0.5"])

        # Guardamos en la Hoja10 sin afectar otras hojas
        with pd.ExcelWriter(self.ruta_guardado, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
            pd.DataFrame(datos).to_excel(writer, sheet_name="Hoja10", index=False, header=False)

    # A partir de aquí empezaré con la sección de ejercicios que requieren gráficos según la actividad en la plataforma

    def ejercicio11(self, num=100):
        x = np.random.rand(num)
        y = np.random.rand(num)
        
        plt.figure(figsize=(6, 6))
        plt.scatter(x, y, color='red', alpha=0.5, edgecolors='k')
        plt.xlabel("Valores de X")
        plt.ylabel("Valores de Y")
        plt.title("Gráfico de Dispersión con 100 Puntos Aleatorios")

        ruta_guardado = os.path.join(self.ruta_actividad_2, "grafico_dispersion_ejercicio_11.png")  # Ruta completa
        plt.savefig(ruta_guardado)  
        plt.close()

    def ejercicio12(self, n=100, devolver_datos=False):

        x = np.linspace(-2 * np.pi, 2 * np.pi, n) # Generamos x en el rango de -2π a 2π con n puntos
        y_sin = np.sin(x) # Función seno sin ruido

        # Función seno con ruido gaussiano
        ruido = np.random.normal(0, 0.1, size=x.shape)  # Ruido Gaussiano con media 0 y desviación 0.1
        y_con_ruido = y_sin + ruido

        # Si solo queremos los datos, los devolvemos
        if devolver_datos:
            return x, y_sin, y_con_ruido

        # Graficamos (solo si devolver_datos es False)
        plt.figure(figsize=(8, 6))
        plt.plot(x, y_sin, label="y = sin(x)", color='blue', linewidth=2)  # Línea de referencia
        plt.scatter(x, y_con_ruido, label="y = sin(x) + ruido", color='red', alpha=0.6)  # Puntos con ruido

        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Gráfico de dispersión de y = sin(x) + ruido gaussiano")
        plt.legend()
        plt.grid()

        # Guardar la imagen en la carpeta actividad_2
        ruta_guardado = os.path.join(self.ruta_actividad_2, "grafico_seno_ruido_ejercicio_12.png")
        plt.savefig(ruta_guardado)
        plt.close()

    def ejercicio13(self):
        # Definir el rango de valores para x e y
        x = np.linspace(-5, 5, 100)  # 100 puntos entre -5 y 5
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y) # Crear la malla de coordenadas
        Z = np.cos(X) + np.sin(Y) # Aplicar la función z = cos(x) + sin(y)

        # Crear la figura y el gráfico de contorno
        plt.figure(figsize=(8, 6))
        contorno = plt.contourf(X, Y, Z, cmap="coolwarm", levels=50)  # Mapa de color
        plt.colorbar(contorno)  # Agregar barra de colores
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Gráfico de Contorno de z = cos(x) + sin(y)")

        # Guardar la imagen en la carpeta actividad_2
        ruta_guardado = os.path.join(self.ruta_actividad_2, "grafico_contorno_ejercicio_13.png")
        plt.savefig(ruta_guardado)
        plt.close()

    def ejercicio14(self, n=1000):

        # Generar 1000 puntos aleatorios
        x = np.random.randn(n)
        y = np.random.randn(n)
        plt.figure(figsize=(6, 6)) # Crear el gráfico de dispersión
        
        # Usar hexbin para visualizar la densidad de puntos
        plt.hexbin(x, y, gridsize=30, cmap="coolwarm", mincnt=1)
        plt.colorbar(label="Densidad")
        
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.title("Gráfico de dispersión con densidad de puntos")

        # Guardar el gráfico en la carpeta actividad_2
        ruta_guardado = os.path.join(self.ruta_actividad_2, "grafico_dispersión_densidad_ejercicio_14.png")
        plt.savefig(ruta_guardado)
        plt.close()

    def ejercicio15(self, n=100):
        # Obtenemos los datos exactos llamando a ejercicio12()
        x, y_sin, _ = self.ejercicio12(n, devolver_datos=True) 
        X, Y = np.meshgrid(x, y_sin)         # Creamos la cuadrícula con meshgrid usando los mismos datos
        Z = np.sin(X) + np.cos(Y)  # Aplicamos la función para el contorno

        plt.figure(figsize=(8, 6)) # Crear gráfico de contorno lleno
        contorno = plt.contourf(X, Y, Z, levels=50, cmap="coolwarm")  # Contorno lleno
        plt.colorbar(contorno, label="Valor de Z")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Gráfico de Contorno Lleno basado en y = sin(x)")

        # Guardar en la carpeta actividad_2
        ruta_guardado = os.path.join(self.ruta_actividad_2, "grafico_contorno_lleno_ejercicio_15.png")
        plt.savefig(ruta_guardado)
        plt.close()

    def ejercicio16(self, n=100):
        x, y_sin, y_con_ruido = self.ejercicio12(n, devolver_datos=True)
        plt.figure(figsize=(8, 6)) # Crear la figura
        
        plt.plot(x, y_sin, label=r"$y = \sin(x)$", color='blue', linewidth=2) # Graficar la función seno sin ruido
        plt.scatter(x, y_con_ruido, label=r"$y = \sin(x) + \text{ruido gaussiano}$", color='red', alpha=0.6) # Graficar la función seno con ruido

        # Etiquetas de los ejes
        plt.xlabel(r"$\text{Eje X}$")  
        plt.ylabel(r"$\text{Eje Y}$")  
        plt.title(r"$\text{Gráfico de Dispersión}$") # Título del gráfico
        plt.legend() # Mostrar la leyenda con formato LaTeX

        # Guardar en la carpeta actividad_2
        ruta_guardado = os.path.join(self.ruta_actividad_2, "grafico_dispersión_etiquetas_ejercicio_16.png")
        plt.savefig(ruta_guardado)
        plt.close()

    def ejercicio16_1(self, n=1000):
        # Generamos 1000 números aleatorios con distribución normal (media=0, desviación estándar=1)
        datos = np.random.randn(n)
        plt.figure(figsize=(8, 6)) # Crear la figura
        plt.hist(datos, bins=30, color='red', edgecolor='black', alpha=0.7, density=True) # Generar el histograma con 30 bins

        # Etiquetas de los ejes
        plt.xlabel("Valor")
        plt.ylabel("Densidad")
        plt.title("Histograma de distribución normal") # Título del gráfico

        ruta_guardado = os.path.join(self.ruta_actividad_2, "histograma_distribucion_normal_ejercicio_16.1.png") # Guardar en la carpeta actividad_2
        plt.savefig(ruta_guardado)
        plt.close()
        
    def ejercicio17(self):
        datos1 = np.random.normal(loc=0, scale=1, size=1000)  # Media=0, Desviación estándar=1
        datos2 = np.random.normal(loc=3, scale=1.5, size=1000)  # Media=3, Desviación estándar=1.5
        plt.figure(figsize=(8, 6)) # Geáfica

        # Histograma de ambos conjuntos de datos
        plt.hist(datos1, bins=30, color='blue', edgecolor='black', alpha=0.6, label=r'$\mu=0, \sigma=1$')
        plt.hist(datos2, bins=30, color='red', edgecolor='black', alpha=0.6, label=r'$\mu=3, \sigma=1.5$')

        # Etiquetas de los ejes
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        plt.title("Histograma de dos distribuciones normales") # Título del gráfico
        plt.legend() # Agregar la leyenda

        ruta_guardado = os.path.join(self.ruta_actividad_2, "histograma_doble_distribucion_ejercicio_17.png") # Guardar en la carpeta actividad_2
        plt.savefig(ruta_guardado)
        plt.close()
        return datos1, datos2
    
    def ejercicio18(self):
        # Conjunto de datos con distribución normal
        datos = np.random.normal(loc=0, scale=1, size=1000)  # Media=0, Desviación estándar=1
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))   # Configuración de la figura con 3 subgráficos
        bins_list = [10, 30, 50] # Lista de bins a probar

        for i, bins in enumerate(bins_list):
            axes[i].hist(datos, bins=bins, color='red', edgecolor='black', alpha=0.7)
            axes[i].set_title(f"Histograma con {bins} bins")
            axes[i].set_xlabel("Valor")
            axes[i].set_ylabel("Frecuencia")

        plt.tight_layout() # Ajustar el layout

        # Guardar en la carpeta actividad_2
        ruta_guardado = os.path.join(self.ruta_actividad_2, "histograma_bins_ejercicio_18.png")
        plt.savefig(ruta_guardado)
        plt.close()
        return datos # Esto se hace para poder acceder a los datos desde otra función

    def ejercicio19(self):

        datos = self.ejercicio18() # Llamamos los datos generados en el ejercicio18()
        fig, axes = plt.subplots(1, 3, figsize=(18, 5)) # Configuración de la figura con 3 subgráficos
        bins_list = [10, 30, 50] # Lista de bins a probar
        media = np.mean(datos) # Calculamos la media de los datos

        for i, bins in enumerate(bins_list):
            axes[i].hist(datos, bins=bins, color='red', edgecolor='black', alpha=0.7)
            axes[i].axvline(media, color='blue', linestyle='dashed', linewidth=2, label=f"Media: {media:.2f}")  # Línea vertical en la media
            axes[i].set_title(f"Histograma con {bins} bins")
            axes[i].set_xlabel("Valor")
            axes[i].set_ylabel("Frecuencia")
            axes[i].legend()  # Añadir la leyenda para la media

        plt.tight_layout() # Ajustar el layout
        # Guardar en la carpeta actividad_2
        ruta_guardado = os.path.join(self.ruta_actividad_2, "histograma_con_media_ejercicio_19.png")
        plt.savefig(ruta_guardado)
        plt.close()

    def ejercicio20(self):

        datos1, datos2 = self.ejercicio17() # Llamamos los datos generados en el ejercicio 17
        # Crear el histograma superpuesto
        plt.figure(figsize=(8, 6))
        plt.hist(datos1, bins=30, color='blue', edgecolor='black', alpha=0.5, label="Datos 1")
        plt.hist(datos2, bins=30, color='red', edgecolor='black', alpha=0.5, label="Datos 2")

        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        plt.title("Histogramas Superpuestos de dos Distribuciones")
        plt.legend()

        # Guardar la imagen
        ruta_guardado = os.path.join(self.ruta_actividad_2, "histograma_superpuesto_ejercicio_20.png")
        plt.savefig(ruta_guardado)
        plt.close()

matr = Actividad_2() # Instancia de la clase y el llamado de cada una de las funciones dentro de la clase
matr.ejercicio1()
matr.ejercicio2()
matr.ejercicio3()
matr.ejercicio4()
matr.ejercicio5()   
matr.ejercicio6()
matr.ejercicio7()
matr.ejercicio8()
matr.ejercicio9()
matr.ejercicio10()
matr.ejercicio11()
matr.ejercicio12()
matr.ejercicio13()
matr.ejercicio14()
matr.ejercicio15()
matr.ejercicio16()
matr.ejercicio16_1()
matr.ejercicio17()
matr.ejercicio18()
matr.ejercicio19()
matr.ejercicio20()