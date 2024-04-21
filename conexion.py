import pyodbc

class ConexionBD:
    @staticmethod
    def obtener_conexion():
        try:
            conexion = pyodbc.connect(
                "Driver={ODBC Driver 17 for SQL Server};"
                "Server=tcp:sistemasoperativosupc.database.windows.net,1433;"
                "Database=SO-Project;"
                "UID=KarimS21;"
                "PWD=SOupc2024;"
                "Encrypt=yes;"
                "TrustServerCertificate=no;"
                "Connection Timeout=30;"
            )
            return conexion
        except Exception as e:
            print("Error connecting to SQL Server.")
            print(e)
