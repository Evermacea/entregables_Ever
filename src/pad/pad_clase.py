import pandas as pd
import kagglehub
import os
import zipfile
import matplotlib
import plotly.express as px
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import tkinter
import sys # Importamos la libreria sys
# tkinter._test()
import numpy as np


class Pad_clase:
    def __init__(self):
        pass
        sys.stdout.reconfigure(encoding='utf-8') 
        
    def download_dataset_zip(self):
        print("Descargando dataset desde Kaggle...")
        dataset_path = kagglehub.dataset_download("zynicide/wine-reviews")
        print("Ruta al dataset:", dataset_path)
        return dataset_path
    
    def extract_zip_files(self,dataset_path):
        zip_files = [f for f in os.listdir(dataset_path) if f.endswith('.zip')]
        if zip_files:
            zip_file = os.path.join(dataset_path, zip_files[0])
            extract_dir = os.path.join(dataset_path, "extracted")
            os.makedirs(extract_dir, exist_ok=True)
            print(f"Extrayendo {zip_file} en {extract_dir}...")
            with zipfile.ZipFile(zip_file, "r") as z:
                z.extractall(extract_dir)
            return extract_dir
        else:
            # Si no se encuentra un ZIP, se verifica si existen archivos CSV en la ruta
            csv_files = [f for f in os.listdir(dataset_path) if f.endswith('.csv')]
            if csv_files:
                print("No se encontró archivo ZIP pero se detectaron archivos CSV; se asume que el dataset ya se encuentra extraído.")
                return dataset_path
            else:
                raise FileNotFoundError("No se encontró ningún archivo .zip ni archivos .csv en la ruta del dataset")
    

    def create_csv(self, csv_dir):
        os.makedirs('src/static/csv', exist_ok=True)

        csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
        print(f"Archivos CSV encontrados: {csv_files}")

        if not csv_files:
            raise FileNotFoundError("No se encontraron archivos CSV en el directorio extraído")

        df_list = []  # Lista para almacenar los DataFrames

        for file in csv_files:
            file_path = os.path.join(csv_dir, file)
            print(f"Leyendo {file_path}...")

            try:
                df = pd.read_csv(file_path, encoding="utf-8")
                print(f"Primeras filas del archivo {file}:{df.head()}")  # Imprime las primeras filas
                df_list.append(df)  # Guardamos el DataFrame en la lista
                print(f"CSV cargado correctamente: {file}")
            except Exception as e:
                print(f"Error al leer {file}: {e}")

        if not df_list:  # Si no se logró leer ningún archivo
            raise ValueError("No se pudo cargar ningún archivo CSV correctamente")

        df_final = pd.concat(df_list, ignore_index=True)  # Unimos todos los CSVs en uno solo
        print(f"CSVs combinados correctamente, tamaño final: {df_final.shape}")

        return df_final  # Retornamos el DataFrame consolidado


    
    # def grafico_normal(self,df):
    #     cantidad = len(df)
    #     # cantidad = 209306
    #     np.random.seed(0)
    #     generados = np.random.randn(cantidad)
    #     serie = pd.Series(generados)
    #     df["random_g"] = serie
    #     df.to_csv("dataset_nuevo.csv")
    #     #plt.figure()
    #     df["num_units"].plot(kind = 'barh')
    #     #print(df["random_g"].describe())
    #     #plt.show()
    #     plt.savefig("grafico_normal_2_line.png")
    #     #plt.legend(loc='datos aleatorios')
    
    # def grafico_df_xy(self,df):
    #     if "random_g" not in df.columns:
    #         np.random.seed(0)
    #         df["random_g"] = np.random.randn(len(df))
        
    #     # Definir las columnas que se quieren graficar
    #     columnas = ["crash_month", "random_g"]
        
    #     # (Opcional) Si deseas reiniciar el índice de df:
    #     df.reset_index(drop=True, inplace=True)
        
    #     # Seleccionar las columnas y graficar
    #     df1 = df[columnas]
    #     df1.plot()
    #     plt.xlabel("Índice")
    #     plt.title("Gráfico de crash_month y random_g")
    #     plt.savefig("grafico_normal_3.png")
    #     plt.show()
    
    # def graficos_agrupados(self,df = pd.DataFrame(), lista_columnas=[]):
    #     for col in lista_columnas:
    #         conteo = df[col].value_counts().sort_index()
    #         plt.figure()
    #         conteo.plot(kind= "bar")
    #         plt.xlabel(col)
    #         plt.ylabel("cantidad")
    #         plt.show()

# padclase = Pad_clase()          
# dataset_path = padclase.download_dataset_zip()
# csv_dir = padclase.extract_zip_files(dataset_path)
# df = padclase.create_csv(csv_dir)
# print(df.describe(),df.count,df.info())
# df.to_csv("dataset_kaggle.csv")
# padclase.grafico_normal(df)
# padclase.grafico_df_xy(df)
#209306
#print(df.describe(),df.count,df.info())