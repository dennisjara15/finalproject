class Config:
    # Configuración de la conexión a la base de datos PostgreSQL
    DB_USERNAME = "tu_usuario_db"
    DB_PASSWORD = "tu_contraseña_db"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "nombre_base_de_datos"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"