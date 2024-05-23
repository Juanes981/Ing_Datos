import pandas as pd
from dash import Dash, html, dcc
import psycopg2
import plotly.express as px

try:
    # Establecer conexión con la base de datos PostgreSQL
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456789',
        database='Ing_datos',
        port='5433',
    )
    print("Conexión exitosa")

    # Crear un cursor para ejecutar comandos SQL
    cursor = connection.cursor()


    # Ejecutar la consulta SQL para obtener los datos de la tabla "Numeros Vagones"
    consulta1 = "select Nombre_Estacion, Numero_Vagones_Estacion from Caracteristicas_Estacion"
    cursor.execute(consulta1)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_car = cursor.fetchall()
    car_es = pd.DataFrame(rows_car, columns=['Nombre_Estacion', 'Numero_Vagones_Estacion'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "Numeros Accesos"
    consulta2 = "select Nombre_Estacion, Numero_Accesos_Estacion from Caracteristicas_Estacion"
    cursor.execute(consulta2)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_ac = cursor.fetchall()
    nu_ac = pd.DataFrame(rows_ac, columns=['Nombre_Estacion', 'Numero_Accesos_Estacion'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "Biciestaciones"
    consulta3 = "select Nombre_Estacion, Biciestacion from Caracteristicas_Estacion"
    cursor.execute(consulta3)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_bi = cursor.fetchall()
    bici = pd.DataFrame(rows_bi, columns=['Nombre_Estacion', 'Biciestacion'])

    # Ejecutar la consulta SQL para obtener los datos de la tabla "Componentes_wifi"
    consulta4 = "select Nombre_Estacion, Componente_Wifi from Caracteristicas_Estacion"
    cursor.execute(consulta4)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_wi = cursor.fetchall()
    co_wi = pd.DataFrame(rows_wi, columns=['Nombre_Estacion', 'Componente_Wifi'])

    # Ejecutar la consulta SQL para obtener los datos de la tabla "Estaciones mas optimas"
    consulta5 = "select Nombre_Estacion, Numero_Vagones_Estacion, Numero_Accesos_Estacion, Biciestacion, Componente_Wifi from Caracteristicas_Estacion where Numero_Vagones_Estacion > 4 and Numero_Accesos_Estacion = 2 and Biciestacion > 1 and Componente_Wifi = 'Si'"
    cursor.execute(consulta5)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_mao = cursor.fetchall()
    mas_op = pd.DataFrame(rows_mao, columns=['Nombre_Estacion', 'Numero_Vagones_Estacion', 'Numero_Accesos_Estacion', 'Biciestacion', 'Componente_Wifi'])

    
    # Ejecutar la consulta SQL para obtener los datos de la tabla "Estaciones menos optimas"
    consulta6 = "select Nombre_Estacion, Numero_Vagones_Estacion, Numero_Accesos_Estacion, Biciestacion, Componente_Wifi from Caracteristicas_Estacion where Numero_Vagones_Estacion <= 1 and Numero_Accesos_Estacion = 1 and Biciestacion <= 1 and Componente_Wifi = 'No'"
    cursor.execute(consulta6)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_men = cursor.fetchall()
    men_op = pd.DataFrame(rows_men, columns=['Nombre_Estacion', 'Numero_Vagones_Estacion', 'Numero_Accesos_Estacion', 'Biciestacion', 'Componente_Wifi'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "Cantidad de estaciones por troncal"
    consulta7 = "select t.Troncal_Estacion, count(e.Codigo_Estacion) as Numero_Estaciones from Datos_Troncal t join Estaciones_Troncales e on e.Id_Trazado_Troncal = t.Id_Trazado_Troncal group by t.Troncal_Estacion"
    cursor.execute(consulta7)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    can_es = pd.DataFrame(rows_can, columns=['Troncal_Estacion', 'Numero_Estaciones'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "Selecciona todas las estaciones que estan en la NQS"
    consulta8 = "select Nombre_Estacion, Codigo_Estacion from Estaciones_Troncales where Id_Trazado_Troncal in (select Id_Trazado_Troncal from Datos_Troncal where Troncal_Estacion = 'NQS-E' OR Troncal_Estacion = 'NQS-G')"
    cursor.execute(consulta8)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_nqs = cursor.fetchall()
    nqs_es = pd.DataFrame(rows_nqs, columns=['Nombre_Estacion', 'Codigo_Estacion'])

    # Cerrar el cursor
    cursor.close()

    # Crear la aplicación Dash
    app = Dash(__name__)

    # Definir el layout de la aplicación
    app.layout = html.Div(children=[
        
        html.H1("Analisis Estaciones Trasmilenio"),
        html.H2("Integrantes :"),
        html.P("-Gabriela Aldana"),
        html.P("-Camila Camacho"),
        html.P("-Juan Esteban Torres"),
        html.P("-Juan Diego Susunaga (Jori was here u.u)"),
        html.H3("Idea proyecto:"),
        html.P("-La idea que tenemos para este proyecto es usar la base de datos de Trasmilenio más reciente en donde podemos analizar sobre las estaciones troncales"),
        html.P("-Para este proyecto decidimos plantear cinco escenarios con su respectivo analisis y gráfica"),

        html.H3("Primer escenario:"),

        dcc.Graph(
            id='Tabla1',
            figure=px.bar(car_es.iloc[0:10], x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Estaciones con mayor numeros de vagones')),

        html.H2("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H3("Segundo escenario:"),

        dcc.Graph(
            id='Tabla1',
            figure=px.bar(car_es.iloc[0:10], x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Estaciones con mayor numeros de vagones')),

        html.H2("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H3("Tercer escenario:"),

        dcc.Graph(
            id='Tabla1',
            figure=px.bar(car_es.iloc[0:10], x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Estaciones con mayor numeros de vagones')),

        html.H2("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H3("Cuarto escenario:"),

        dcc.Graph(
            id='Tabla1',
            figure=px.bar(car_es.iloc[0:10], x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Estaciones con mayor numeros de vagones')),

        html.H2("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H3("Quinto escenario:"),

        dcc.Graph(
            id='Tabla1',
            figure=px.bar(car_es.iloc[0:10], x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Estaciones con mayor numeros de vagones')),

        html.H2("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),
    ])

    # Ejecutar la aplicación
    if __name__ == '__main__':
        app.run_server(debug=True)

except Exception as ex:
    print(ex)

finally:
    if connection is not None:
        connection.close()
        print("Conexión cerrada")

