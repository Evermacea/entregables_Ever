import json # Importamos la librería json
import requests # Importamos la librería requests
import sys # Importamos la librería sys

class Ingestiones():
    def __init__(self):
        self.ruta_static = "src/pad/static/"
        sys.stdout.reconfigure(encoding='utf-8') 

    def leer_api(self, ruta):
        response = requests.get(ruta) # Hacemos una petición GET a la API
        return response.json() # Retornamos el contenido de la API en formato JSON

    def escribir_json(self, nombre_archivo, datos):
        ruta_json = f"{self.ruta_static}json/{nombre_archivo}.json"
        with open(ruta_json, mode="w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False)

ingestion = Ingestiones() # Crear instancia de la clase
print(ingestion.ruta_static)

datos_json = ingestion.leer_api("https://dattebayo-api.onrender.com/clans") # Llamamos a la función leer_api
print("Datos del archivo json :", json.dumps(datos_json, ensure_ascii=False)) 

ingestion.escribir_json("clanes_naruto", datos_json)  # Guardamos los datos en un archivo JSON
print("Archivo json creado con éxito 🎉✨🤸‍♂️")
