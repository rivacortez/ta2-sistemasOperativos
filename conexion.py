import pyodbc


                server   = 'sistemasoperativosupc.database.windows.net'
                database = 'SO-Project'
                username = 'KarimS21'
                password = 'SOupc2024'
            
           
connection_string = f'DRIVER=((SQL Server)}; SERVER={server} ;DATABASE={database}; UID={username}; PWD={password}'

def connect():
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print(f"No se pudo conectar a la base de datos: {e}")
