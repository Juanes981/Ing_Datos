import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import psycopg2 

try:
    # Intentamos establecer una conexión con la base de datos PostgreSQL
    connection = psycopg2.connect(
        host='localhost',  # Dirección del servidor de base de datos
        user='postgres',  # Nombre de usuario
        password='123456789',  # Contraseña del usuario
        database='Carga_datos',  # Nombre de la base de datos a la que queremos conectarnos
        port='5433' # Puerto en el que está escuchando el servidor de base de datos
    )

    print("Conexión exitosa") # Si la conexión es exitosa, imprimimos un mensaje
    cursor = connection.cursor() # Creamos un objeto cursor para ejecutar comandos SQL

    # Tabla1 Estaciones_Troncales_Transmilenio	
    cursor.execute("SELECT * FROM Estaciones_Troncales_Transmilenio")  # Ejecutamos una consulta SQL para seleccionar todos los datos de la tabla "Estaciones_Troncales_Transmilenio"
    rows=cursor.fetchall()  # Obtenemos todas las filas resultantes de la consulta
    
    for row in rows:
        print(row)

    # Inicializar la aplicación Dash
    app = dash.Dash(__name__)

    fig = px.bar (rows, x=0, y=1, color_discrete_sequence=-['#b52a64'])

    # Diseño de la aplicación
    app.layout = html.Div(children=[

        html.Img(src = 'Mer.drawio.png'),
        
        html.P('Hola'),

        html.H1(children='Mi Dashboard con Dash'),

        html.Div(children='''
            Ejemplo sencillo de un dashboard usando Dash y Plotly.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
])

    if __name__ == '__main__':
        app.run_server(debug=False)


except Exception as ex:
    print(ex) # Si ocurre algún error durante la ejecución del bloque try, lo capturamos y lo imprimimos
    
finally:
    connection.close() # Finalmente, independientemente de si hubo éxito o error, cerramos la conexión a la base de datos
    print("Conexión finalizada") # Imprimimos un mensaje para indicar que la conexión ha sido cerrada

