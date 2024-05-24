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
    consulta1 = "select Nombre_Estacion, Numero_Vagones_Estacion from Caracteristicas_Estacion where Numero_Vagones_Estacion = 5 or Numero_Vagones_Estacion = 6 group by Nombre_Estacion order by Numero_Vagones_Estacion asc"
    cursor.execute(consulta1)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_car = cursor.fetchall()
    car_es = pd.DataFrame(rows_car, columns=['Nombre_Estacion', 'Numero_Vagones_Estacion'])

    # Ejecutar la consulta SQL para obtener los datos de la tabla "Numeros Vagones"
    consulta2 = "select Nombre_Estacion, Numero_Vagones_Estacion from Caracteristicas_Estacion where Numero_Vagones_Estacion = 0 or Numero_Vagones_Estacion = 1 group by Nombre_Estacion order by Numero_Vagones_Estacion asc"
    cursor.execute(consulta2)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_carr = cursor.fetchall()
    car_ess = pd.DataFrame(rows_carr, columns=['Nombre_Estacion', 'Numero_Vagones_Estacion'])

    # Ejecutar la consulta SQL para obtener los datos de la tabla "Numeros Accesos"
    consulta3 = "select Nombre_Estacion, Numero_Accesos_Estacion from Caracteristicas_Estacion where Numero_Accesos_Estacion = 2 group by Nombre_Estacion"
    cursor.execute(consulta3)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_ac = cursor.fetchall()
    nu_ac = pd.DataFrame(rows_ac, columns=['Nombre_Estacion', 'Numero_Accesos_Estacion'])

    # Ejecutar la consulta SQL para obtener los datos de la tabla "Numeros Accesos"
    consulta4 = "select Nombre_Estacion, Numero_Accesos_Estacion from Caracteristicas_Estacion where Numero_Accesos_Estacion = 0 group by Nombre_Estacion"
    cursor.execute(consulta4)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_acc = cursor.fetchall()
    nu_acc = pd.DataFrame(rows_acc, columns=['Nombre_Estacion', 'Numero_Accesos_Estacion'])

    # Ejecutar la consulta SQL para obtener los datos de la tabla "Biciestaciones"
    consulta5 = "select nombre_estacion, biciestacion from caracteristicas_estacion where biciestacion >= 1"
    cursor.execute(consulta5)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_bi = cursor.fetchall()
    bici = pd.DataFrame(rows_bi, columns=['Nombre_Estacion', 'Biciestacion'])

     # Ejecutar la consulta SQL para obtener los datos de la tabla "Biciestaciones"
    consulta6 = "select nombre_estacion, biciestacion from caracteristicas_estacion where biciestacion = 0"
    cursor.execute(consulta6)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_bii = cursor.fetchall()
    bicii = pd.DataFrame(rows_bii, columns=['Nombre_Estacion', 'Biciestacion'])

    # Ejecutar la consulta SQL para obtener los datos de la tabla "Componentes_wifi"
    consulta7 = "select Componente_Wifi, count(Componente_Wifi) , rank() over (order by Componente_Wifi desc) as pato from Caracteristicas_Estacion group by Componente_Wifi order by pato"
    cursor.execute(consulta7)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_wi = cursor.fetchall()
    co_wi = pd.DataFrame(rows_wi, columns=['Componente_Wifi', 'wifi','pato'])

    # Ejecutar la consulta SQL para obtener los datos de la tabla "Componentes_wifi"
    consulta8 = "select Nombre_Estacion, Componente_Wifi from Caracteristicas_Estacion  where Componente_Wifi = 'No'"
    cursor.execute(consulta8)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_wii = cursor.fetchall()
    co_wii = pd.DataFrame(rows_wii, columns=['Nombre_Estacion', 'Componente_Wifi'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "Cantidad de estaciones por troncal"
    consulta9 = "select t.Troncal_Estacion, count(e.Codigo_Estacion) as Numero_Estaciones from Datos_Troncal t join Estaciones_Troncales e on e.Id_Trazado_Troncal = t.Id_Trazado_Troncal group by t.Troncal_Estacion"
    cursor.execute(consulta9)

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

        html.H2("Primer escenario:"),
        html.P("En este escenario se busca analisar sobre las estaciones que tienen mayor número de vagones, entre 5 - 6; tambien las estaciones con menor número de vagones, entre 0 - 1"),

        dcc.Graph(
            id='Tabla1',
            figure=px.bar(car_es, x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Estaciones con cinco o seís vagones',color_discrete_sequence=["#f3bc26"])
        ),

        dcc.Graph(
            id='Tabla2',
            figure=px.bar(car_ess, x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Estaciones con cero o un vagon')
        ),

        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H2("Segundo escenario:"),
        html.P("En este escenario buscamos todas las estaciones con el maximo de accesos (2) y tambien las que no tienen un acceso"),

         dcc.Graph(
            id='Tabla3',
            figure=px.bar(nu_ac, x='Nombre_Estacion', y='Numero_Accesos_Estacion', title='Estaciones con el máximo de accesos',color_discrete_sequence=["#dc143c"])
        ),

        dcc.Graph(
            id='Tabla4',
            figure=px.bar(nu_acc, x='Nombre_Estacion', y='Numero_Accesos_Estacion', title='Estaciones sin accesos',color_discrete_sequence=["#f3b407"])
        ),

        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H2("Tercer escenario:"),
        html.P("En este escenario se desea encontrar las estaciones que cuentan con biciestación y las estaciones que no cuentan con este servicio"),

        dcc.Graph(
            id='Tabla5',
            figure=px.bar(bici, x='Nombre_Estacion', y='Biciestacion', title='Estaciones con Biciestaciones',color_discrete_sequence=["#f1666d"])
        ),

        dcc.Graph(
            id='Tabla6',
            figure=px.bar(bicii, x='Nombre_Estacion', y='Biciestacion', title='Estaciones sin Biciestaciones')
        ),


        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H2("Cuarto escenario:"),
        html.P("En este escenario se señala el porcentaje de las estaciones que poseen algun componente de Wifi, cuales no lo poseen y cuales siguen pendientes"),

        dcc.Graph(
            id='Tabla7',
            figure=px.pie(co_wi, values='wifi', names='Componente_Wifi', title='Porcentaje de estaciones con Componente_Wifi',color_discrete_sequence=["#9c0720"])
        ),


        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H2("Quinto escenario:"),
        html.P("En este escenario se observa la cantidad de estaciones que hay por troncal"),

        dcc.Graph(
            id='Tabla9',
            figure=px.pie(can_es, names='Troncal_Estacion', values='Numero_Estaciones', title='Cantidad de estaciones por Troncal')
        ), 

        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H2("Sexto escenario:"),
        html.P("En este ultimo escenario se busca señalar las estaciones exactas que se encuentran en total en la NQS-G y la NQS-E"),

        dcc.Graph(
            id='Tabla10',
            figure=px.bar(nqs_es, x='Nombre_Estacion', y='Codigo_Estacion', title='Todas las estaciones que estan en la NQS',color_discrete_sequence=["#9c0720"])
        ),

        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H2("Conclusiones por participante del grupo:"),
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

