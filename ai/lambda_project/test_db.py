import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

def test_connection():
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),  # Usa 'localhost' como valor por defecto
            user=os.getenv("DB_USER", "root"),      # Usa 'root' como valor por defecto
            password=os.getenv("DB_PASSWORD", ""),  # Usa '' como valor por defecto
            database=os.getenv("DB_NAME", "test_db"),  # Usa 'test_db' como valor por defecto
            port=3306,  # Asegúrate de especificar el puerto
            cursorclass=pymysql.cursors.DictCursor
        )
        print("✅ Conexión exitosa a MySQL")
        connection.close()
    except pymysql.MySQLError as e:
        print(f"❌ Error de MySQL: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    test_connection()