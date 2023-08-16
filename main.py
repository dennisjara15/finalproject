from datetime import datetime
import requests
import pandas as pd
from pandas import json_normalize
import json
from sqlalchemy import create_engine
from config import Config

# Función para obtener los datos de clima de una ciudad y convertirlos a CSV
def get_weather_data(city, coordinates):
    # (Código de la función get_weather_data, igual al explicado anteriormente)

# Leer las credenciales de conexión a la base de datos desde el archivo config.py
config = Config()

# Establecer la conexión a la base de datos PostgreSQL utilizando SQLalchemy
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

# Función para cargar datos de CSV a la base de datos
def load_data_to_database(csv_path):
    df = pd.read_csv(csv_path)
    table_name = "weather_data"
    df.to_sql(table_name, engine, if_exists="append", index=False)
    print(f"Datos cargados en la tabla '{table_name}'.")

# Ruta de los archivos CSV generados previamente
csv_paths = ["data_analytics/openweather/tiempodiario_20230101.csv", "data_analytics/openweather/tiempodiario_20230102.csv", ...]

# Cargar datos de todos los archivos CSV a la base de datos
for csv_path in csv_paths:
    load_data_to_database(csv_path)