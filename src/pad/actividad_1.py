import json # Importamos la librería json
import requests # Importamos la librería requests
import sys # Importamos la librería os
class Ingestiones():
    def __init__(self):
        self.ruta_static = "src/pad/static/"
        sys.stdout.reconfigure(encoding='utf-8') # Configuramos la salida estándar para que acepte caracteres especiales

    def leer_api(self, ruta):
        response = requests.get(ruta) # Hacemos una petición GET a la API
        return response.json() # Retornamos el contenido de la API en formato JSON

    def escribir_json(self, nombre_archivo, datos): # Esta clase escribe en un archivo json, los datos extraidos desde la api con la información del anime Naruto
        ruta_json = "{}json/{}.json".format(self.ruta_static, nombre_archivo) # Creamos el nombre del archivo con la extensión .json
        with open(ruta_json, mode="w", encoding="utf-8") as archivo:
            json.dump(datos, archivo)   # Guardamos los datos en un archivo JSON con el nombre especificado


# crear instancia de la clase
ingestion = Ingestiones()
print(ingestion.ruta_static)
datos_json = ingestion.leer_api("https://dattebayo-api.onrender.com/clans") # Llamamos a la función leer_api con la ruta de la API
print("Datos del archivo json : ",datos_json)

ingestion.escribir_json("clanes_naruto", datos_json)  # Guardamos los datos en un archivo JSON cuyo nombre es "clanes_naruto"
print("Archivo json creado con éxito yuju! 🎉✨🤸‍♂️")