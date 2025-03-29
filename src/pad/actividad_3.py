# Importar librerias
import pandas as pd
import numpy as np
import os
import sys # Importamos la libreria sys
from pad_clase import Pad_clase

class Actividad_3():
    def __init__(self):
        sys.stdout.reconfigure(encoding='utf-8') 
        self.ruta_raiz = "src/pad"
        self.ruta_actividad_3 = "{}/actividad_3/".format(self.ruta_raiz)
        self.ruta_guardado = os.path.join(self.ruta_actividad_3, "resultados.xlsx")
        os.makedirs(self.ruta_actividad_3, exist_ok=True)
        # Importar la función de la clase para extraer la base de datos de Kaggle
        padclase = Pad_clase()          
        dataset_path = padclase.download_dataset_zip()
        csv_dir = padclase.extract_zip_files(dataset_path)
        self.df = padclase.create_csv(csv_dir)
      
    def ejercicio_1(self):
        # Simulación de capturar el resultado desde el notebook
        datos1 = {
            'Granadilla': [20],
            'Tomates': [50]    
        }
        d1 = pd.DataFrame(datos1)  # Convertimos a DataFrame
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio1.csv")
        d1.to_csv(ruta_csv, index=False)

    def ejercicio_2(self):
        d2 =pd.DataFrame({
        'Granadilla': [20, 49],
        'Tomates': [50, 100]    
        }, index =['ventas 2021','ventas 2022'])
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio2.csv")
        d2.to_csv(ruta_csv, index=False)

    def ejercicio_3(self):
        utensilios = pd.Series(
            ["3 unidades", "2 unidades", "4 unidades", "5 unidades"],
            index=["Cuchara", "Tenedor", "Cuchillo", "Plato"],
            name="Cocina"
        )
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio3.csv")
        utensilios.to_csv(ruta_csv, index=False)
    
    def ejercicio_4(self): # Este ejercicio me generó problemas por ser la base de datos tan grande, lo que hice fue dividirlo en archivos csv más pequeños para poder guardar por partes toda la base de datos
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio4.csv")
        self.df.to_csv(ruta_csv, index=False) # Guardar el dataset completo en un CSV
        print(f"Archivo guardado en: {ruta_csv}")

        # Si el dataset tiene más de 50,000 filas, lo dividimos en partes más pequeñas
        if self.df.shape[0] > 50000:
            chunk_size = 25000  # Tamaño de cada fragmento
            for i, chunk in enumerate(pd.read_csv(ruta_csv, chunksize=chunk_size)):
                ruta_parte = os.path.join(self.ruta_actividad_3, f"ejercicio4_part{i+1}.csv")
                chunk.to_csv(ruta_parte, index=False)
                print(f"Guardado: {ruta_parte}")


    def ejercicio_5(self):
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio5.csv")
        self.df.head().to_csv(ruta_csv, index=False) # Guardar el dataset completo en un CSV    

    def ejercicio_6(self):
        self.df.info()
        num_entradas = self.df.shape[0]
        print(f"El DataFrame tiene {num_entradas} entradas.")
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio6.csv")
        df_info = pd.DataFrame({"Número de entradas": [num_entradas]})
        df_info.to_csv(ruta_csv, index=False)
        
    def ejercicio_7(self):
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio7.csv")
        precio_promedio = self.df['price'].mean()
        df_precio = pd.DataFrame({"Promedio de precio": [precio_promedio]})
        df_precio.to_csv(ruta_csv, index=False)
        
    
    def ejercicio_8(self):
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio8.csv")
        precio_maximo = self.df['price'].max()
        df_precio = pd.DataFrame({"El precio máximo es: ": [precio_maximo]})
        df_precio.to_csv(ruta_csv, index=False)

    def ejercicio_9(self):
        Vinos_california = self.df[self.df['country']=='US']
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio9.csv")
        Vinos_california.to_csv(ruta_csv, index=False)
    
    def ejercicio_10(self):
        indice_mas_caro = self.df['price'].idxmax() # Índice del vino con el precio más alto
        vino_mas_caro = self.df.loc[indice_mas_caro] # Información del vino más caro
        # Mostrar el resultado
        print("El vino más caro de California es:")
        print(vino_mas_caro)

        # Guardar la información en un CSV
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio10.csv")
        vino_mas_caro.to_frame().T.to_csv(ruta_csv, index=False)
    
    def ejercicio_11(self):
        Vinos_california = self.df[self.df['country']=='US']
        uvas_mas_comunes = Vinos_california['variety'].value_counts().sort_values(ascending=False).reset_index() # Sobre la base del ejercicio 9 hago el filtro
        uvas_mas_comunes.columns = ['Variety', 'Count']
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio11.csv")
        uvas_mas_comunes.to_csv(ruta_csv, index=False)
    
    def ejercicio_12(self):
        Vinos_california = self.df[self.df['country']=='US']
        uvas_mas_comunes = Vinos_california['variety'].value_counts().sort_values(ascending=False).reset_index() # Sobre la base del ejercicio 9 hago el filtro
        uvas_mas_comunes.columns = ['Variety', 'Count']
        top10= uvas_mas_comunes.head(10)
        ruta_csv = os.path.join(self.ruta_actividad_3, "ejercicio12.csv")
        top10.to_csv(ruta_csv, index=False)

    def ejecutar(self): # Función para ejecutar todos los ejercicios
        self.ejercicio_1()
        self.ejercicio_2()
        self.ejercicio_3()
        self.ejercicio_4()
        self.ejercicio_5()
        self.ejercicio_6()
        self.ejercicio_7()
        self.ejercicio_8()
        self.ejercicio_9()
        self.ejercicio_10()
        self.ejercicio_11()
        self.ejercicio_12()

act3 = Actividad_3() # Instnancia de la clase
act3.ejecutar() # Activar o llamar la función que ejcuta todos los puntos