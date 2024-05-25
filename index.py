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

    # Ejecutar la consulta SQL para obtener los datos de la tabla "Cantidad de estaciones por troncal"
    consulta1 = "select t.Troncal_Estacion, count(e.Codigo_Estacion) as Numero_Estaciones from Datos_Troncal t join Estaciones_Troncales e on e.Id_Trazado_Troncal = t.Id_Trazado_Troncal group by t.Troncal_Estacion"
    cursor.execute(consulta1)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    can_es = pd.DataFrame(rows_can, columns=['Troncal_Estacion', 'Numero_Estaciones'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "El numero de vagones por la troncal Autonorte"
    consulta2 = "select c.Nombre_Estacion, c.numero_vagones_estacion from caracteristicas_estacion c join estaciones_troncales es on c.nombre_estacion = es.nombre_estacion join datos_troncal d on d.id_trazado_troncal = es.id_trazado_troncal  where troncal_estacion = 'Autonorte'"
    cursor.execute(consulta2)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    nor_v = pd.DataFrame(rows_can, columns=['Nombre_Estacion', 'Numero_Vagones_Estacion'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "El numero de vagones por la troncal Americas"
    consulta3 = "select c.Nombre_Estacion, c.numero_vagones_estacion from caracteristicas_estacion c join estaciones_troncales es on c.nombre_estacion = es.nombre_estacion join datos_troncal d on d.id_trazado_troncal = es.id_trazado_troncal  where troncal_estacion = 'Americas'"
    cursor.execute(consulta3)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    ame_v = pd.DataFrame(rows_can, columns=['Nombre_Estacion', 'Numero_Vagones_Estacion'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "El numero de vagones por la troncal Calle 26"
    consulta4 = "select c.Nombre_Estacion, c.numero_vagones_estacion from caracteristicas_estacion c join estaciones_troncales es on c.nombre_estacion = es.nombre_estacion join datos_troncal d on d.id_trazado_troncal = es.id_trazado_troncal  where troncal_estacion = 'Calle 26'"
    cursor.execute(consulta4)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    cal_v = pd.DataFrame(rows_can, columns=['Nombre_Estacion', 'Numero_Vagones_Estacion'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "El numero de vagones por la troncal NQS"
    consulta5 = "select c.Nombre_Estacion, c.numero_vagones_estacion from caracteristicas_estacion c join estaciones_troncales es on c.nombre_estacion = es.nombre_estacion join datos_troncal d on d.id_trazado_troncal = es.id_trazado_troncal  where d.Troncal_Estacion in ('NQS-E', 'NQS-G') "
    cursor.execute(consulta5)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    nqs_v = pd.DataFrame(rows_can, columns=['Nombre_Estacion', 'Numero_Vagones_Estacion'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "El numero de vagones por la troncal Caracas"
    consulta6 = "select c.Nombre_Estacion, c.numero_vagones_estacion from caracteristicas_estacion c join estaciones_troncales es on c.nombre_estacion = es.nombre_estacion join datos_troncal d on d.id_trazado_troncal = es.id_trazado_troncal  where d.Troncal_Estacion in ('Caracas-S', 'Caracas-T') "
    cursor.execute(consulta6)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    car_v = pd.DataFrame(rows_can, columns=['Nombre_Estacion', 'Numero_Vagones_Estacion'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "El numero de vagones por la troncal Autonorte"
    consulta7 = "select c.Nombre_Estacion, c.Numero_Accesos_Estacion from caracteristicas_estacion c join estaciones_troncales es on c.nombre_estacion = es.nombre_estacion join datos_troncal d on d.id_trazado_troncal = es.id_trazado_troncal  where troncal_estacion = 'Autonorte'"
    cursor.execute(consulta7)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    nor_a = pd.DataFrame(rows_can, columns=['Nombre_Estacion', 'Numero_Accesos_Estacion'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "El numero de vagones por la troncal Americas"
    consulta8 = "select c.Nombre_Estacion, c.Numero_Accesos_Estacion from caracteristicas_estacion c join estaciones_troncales es on c.nombre_estacion = es.nombre_estacion join datos_troncal d on d.id_trazado_troncal = es.id_trazado_troncal  where troncal_estacion = 'Americas'"
    cursor.execute(consulta8)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    ame_a = pd.DataFrame(rows_can, columns=['Nombre_Estacion', 'Numero_Accesos_Estacion'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "El numero de vagones por la troncal Calle 26"
    consulta9 = "select c.Nombre_Estacion, c.Numero_Accesos_Estacion from caracteristicas_estacion c join estaciones_troncales es on c.nombre_estacion = es.nombre_estacion join datos_troncal d on d.id_trazado_troncal = es.id_trazado_troncal  where troncal_estacion = 'Calle 26'"
    cursor.execute(consulta9)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    cal_a = pd.DataFrame(rows_can, columns=['Nombre_Estacion', 'Numero_Accesos_Estacion'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "El numero de vagones por la troncal NQS"
    consulta10 = "select c.Nombre_Estacion, c.Numero_Accesos_Estacion from caracteristicas_estacion c join estaciones_troncales es on c.nombre_estacion = es.nombre_estacion join datos_troncal d on d.id_trazado_troncal = es.id_trazado_troncal  where d.Troncal_Estacion in ('NQS-E', 'NQS-G') "
    cursor.execute(consulta10)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    nqs_a = pd.DataFrame(rows_can, columns=['Nombre_Estacion', 'Numero_Accesos_Estacion'])


    # Ejecutar la consulta SQL para obtener los datos de la tabla "El numero de vagones por la troncal Caracas"
    consulta11 = "select c.Nombre_Estacion, c.Numero_Accesos_Estacion from caracteristicas_estacion c join estaciones_troncales es on c.nombre_estacion = es.nombre_estacion join datos_troncal d on d.id_trazado_troncal = es.id_trazado_troncal  where d.Troncal_Estacion in ('Caracas-S', 'Caracas-T') "
    cursor.execute(consulta11)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    car_a = pd.DataFrame(rows_can, columns=['Nombre_Estacion', 'Numero_Accesos_Estacion'])

    consulta12 = "select d.Troncal_Estacion, count(*) AS Numero_Estaciones_Con_Wifi from Datos_Troncal d join Estaciones_Troncales es on d.Id_Trazado_Troncal = es.Id_Trazado_Troncal join Caracteristicas_Estacion c on es.Nombre_Estacion = c.Nombre_Estacion where c.Componente_Wifi = 'Si' group by d.Troncal_Estacion; "
    cursor.execute(consulta12)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    tr_co = pd.DataFrame(rows_can, columns=['Troncal_Estacion', 'Numero_Estaciones_Con_Wifi'])

    consulta13 = "select troncal_estacion, sum(biciestacion) from datos_troncal join estaciones_troncales es on datos_troncal.id_trazado_troncal = es.id_trazado_troncal join caracteristicas_estacion c on es.nombre_estacion = c.nombre_estacion group by troncal_estacion "
    cursor.execute(consulta13)

    # Obtener los resultados de la consulta y cargarlos en un DataFrame de pandas
    rows_can = cursor.fetchall()
    tr_bi = pd.DataFrame(rows_can, columns=['Troncal_Estacion', 'Biciestacion'])

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
        html.P("-Juan Diego Susunaga"),
        html.H3("Idea proyecto:"),
        html.P("-La idea que tenemos para este proyecto es usar la base de datos de Trasmilenio más reciente en donde podemos analizar sobre las estaciones troncales"),
        html.P("-Para este proyecto decidimos plantear cinco escenarios con su respectivo analisis y gráfica"),

        html.H2("Primer escenario:"),
        html.P("-Este escenario es para analizar cuantas estaciones hay por troncal, con estos datos se eligen las 5 troncales con más estaciones, esto debido a que se piensan usar para desarrollar los escenarios dos y tres que se explicaran más adelante"),

        dcc.Graph(
            id='Tabla1',
            figure=px.pie(can_es, names='Troncal_Estacion', values='Numero_Estaciones', title='Cantidad de estaciones por Troncal')
        ), 

        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban:"),
        html.P("-Juan Diego: "),

        html.H2("Segundo escenario:"),
        html.P("-En este escenario se busca identificar los vagones de las estaciones de cada una de las 5 troncales seleccionadas (NQS, Caracas, Autonorte, Américas y calle 26) esto para poder encontrar cual es la troncal y estación con una mayor cantidad de vagones"),

        dcc.Graph(
            id='Tabla2',
            figure=px.bar(nor_v, x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Numero de vagones en el Autonorte',color_discrete_sequence=["#42FC67"])
        ),

        dcc.Graph(
            id='Tabla3',
            figure=px.bar(ame_v, x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Numero de vagones en Américas',color_discrete_sequence=["#FF0000"])
        ),

        dcc.Graph(
            id='Tabla4',
            figure=px.bar(cal_v, x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Numero de vagones en la calle 26', color_discrete_sequence=["#EFB810"])
        ),

        dcc.Graph(
            id='Tabla5',
            figure=px.bar(nqs_v, x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Numero de vagones en la NQS',color_discrete_sequence=["#1e97f3"])
        ),

        dcc.Graph(
            id='Tabla6',
            figure=px.bar(car_v, x='Nombre_Estacion', y='Numero_Vagones_Estacion', title='Numero de vagones en Caracas',color_discrete_sequence=["#EF6C00"])
        ),

        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H2("Tercer escenario:"),
        html.P("-En este escenario se busca identificar los accesos de las estaciones de cada una de las 5 troncales seleccionadas (NQS, Caracas, Autonorte, Américas y calle 26) esto para poder encontrar cual es la troncal y estación con una mayor cantidad de accesos"),

         dcc.Graph(
            id='Tabla6',
            figure=px.scatter(nor_a, x='Nombre_Estacion', y='Numero_Accesos_Estacion', size = 'Numero_Accesos_Estacion', title='Numero de accesos en el Autonorte',color_discrete_sequence=["#42FC67"])
        ),

        dcc.Graph(
            id='Tabla7',
            figure=px.scatter(ame_a, x='Nombre_Estacion', y='Numero_Accesos_Estacion', size = 'Numero_Accesos_Estacion', title='Numero de accesos en Américas',color_discrete_sequence=["#FF0000"])
        ),

        dcc.Graph(
            id='Tabla8',
            figure=px.scatter(cal_a, x='Nombre_Estacion', y='Numero_Accesos_Estacion', size = 'Numero_Accesos_Estacion', title='Numero de accesos en la calle 26',color_discrete_sequence=["#EFB810"])
        ),

        dcc.Graph(
            id='Tabla9',
            figure=px.scatter(nqs_a, x='Nombre_Estacion', y='Numero_Accesos_Estacion', size = 'Numero_Accesos_Estacion', title='Numero de accesos en la NQS',color_discrete_sequence=["#1e97f3"])
        ),

        dcc.Graph(
            id='Tabla10',
            figure=px.scatter(car_a, x='Nombre_Estacion', y='Numero_Accesos_Estacion', size = 'Numero_Accesos_Estacion', title='Numero de accesos en Caracas',color_discrete_sequence=["#EF6C00"])
        ),


        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H2("Cuarto escenario:"),
        html.P("-En este escenario se hace una suma de la cantidad de estaciones con componente Wifi por cada troncal, con esto poder saber cual es la troncal que tiene mayor cantidad de estaciones con Wifi"),

        dcc.Graph(
           id='Tabla12',
            figure=px.line(tr_co, x='Troncal_Estacion', y='Numero_Estaciones_Con_Wifi', title='Cantidad de Wifi por Troncal', color_discrete_sequence=["#820000"])
        ),


        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela :"),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H2("Quinto escenario:"),
        html.P("-En este escenario se hace una suma de la cantidad de estaciones con biciestacion por cada troncal, con esto poder saber cual es la troncal que tiene mayor cantidad de biciestacion"),

        dcc.Graph(
            id='Tabla13',
            figure=px.line(tr_bi, x='Troncal_Estacion', y='Biciestacion', title='Cantidad de Biciestaciones por Troncal', color_discrete_sequence=["#f8da45"])
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