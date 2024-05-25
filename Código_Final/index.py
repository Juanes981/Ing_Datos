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
        html.P("-Gabriela : Al observar esta gráfica, podemos afirmar que las troncales con más estaciones son Autonorte, Américas, Calle 26, NQS y Caracas. Esto probablemente se deba a su mayor extensión geográfica. Por lo tanto, al evaluar estas cinco troncales, podremos obtener una visión representativa de las condiciones en una gran parte de las estaciones de Bogotá."),
        html.P("-Camila :"),
        html.P("-Juan Esteban: A partir de la gráfica de pie se puede observar que "),
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
        html.P("-Gabriela : Antes de analizar las gráficas de este primer escenario, es importante tener en cuenta que tener un número de vagones mayor a 3 es beneficioso. Esto permite que más rutas puedan parar en estas estaciones. Por el contrario, tener un número de vagones menor a 3 no es beneficioso, ya que menos rutas pueden detenerse en dichas estaciones, lo que empeora la experiencia de usar el transporte público. Al observar la primera gráfica, podemos ver que la troncal Autonorte tiene 9 estaciones con un número de vagones superior a 3 y 8 estaciones con un número de vagones menor a 3. En la segunda gráfica, se observa que la troncal Américas tiene 8 estaciones con un número de vagones mayor a 3 y 8 estaciones con un número de vagones menor a 3. En la tercera gráfica, podemos ver que la troncal Calle 26 tiene 8 estaciones con un número de vagones mayor a 3 y 6 estaciones con un número de vagones menor a 3. En la cuarta gráfica, se muestra que la troncal NQS tiene 4 estaciones con un número de vagones mayor a 3 y 20 estaciones con un número de vagones menor a 3. Finalmente, en la última gráfica, podemos ver que la troncal Caracas tiene una estación con un número de vagones mayor a 3 y 26 estaciones con un número de vagones menor a 3. Podemos concluir que la Calle 26 es la troncal con mayor número de estaciones con más de 3 vagones, mientras que la Caracas es la troncal con el menor número de estaciones con más de 3 vagones."),
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
        html.P("-Gabriela : Antes de analizar las gráficas de este escenario, es importante tener en cuenta que contar con un mayor número de accesos es beneficioso, ya que aumenta la capacidad de flujo de los pasajeros, reduciendo la congestión y facilitando el acceso rápido a los buses del TransMilenio. Por el contrario, tener un menor número de accesos no es favorable, ya que esto dificulta la accesibilidad en las estaciones, lo que puede ocasionar problemas de aglomeración, especialmente en horas pico. Al observar la primera gráfica, notamos que la troncal Autonorte cuenta solo con 2 estaciones con 2 accesos a la estación y 15 estaciones con un solo acceso. En la segunda gráfica, vemos que la troncal Américas tiene 9 estaciones con dos accesos y 8 estaciones con solo un acceso. En la tercera gráfica, la troncal Calle 26 presenta 3 estaciones con dos accesos y 11 estaciones con solo un acceso. La cuarta gráfica muestra que la troncal NQS tiene 6 estaciones con dos accesos y 18 estaciones con solo un acceso. Finalmente, en la última gráfica, la troncal Caracas cuenta con 20 estaciones con dos accesos y 7 estaciones con solo un acceso. Podemos concluir que Caracas es la troncal con el mayor número de estaciones con 2 accesos, mientras que Autonorte es la que tiene menos estaciones con 2 accesos. "),
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
        html.P("-Gabriela : Tener wifi en las estaciones es beneficioso, ya que proporciona una mejor experiencia en el uso del transporte público y permite acceder a información sobre horarios y rutas alternativas. En caso de emergencia, el usuario tendrá una forma más accesible de comunicarse con una autoridad. Al analizar la gráfica, podemos observar qué CR7-10, Suba, NQS y Caracas tienen un mayor número de estaciones con wifi, mientras que Autonorte y Calle 26 tienen un bajo número de estaciones con wifi en relación con su cantidad total. Por otro lado, Soacha, Tunal y Eje Ambiental son las troncales que tienen menos estaciones con wifi, pero hay que tener en cuenta que estas troncales tienen muy pocas estaciones en total."),
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
        html.P("-Gabriela : Tener biciestaciones en las estaciones es importante, ya que hace que sea más accesible llegar a ellas, permite viajes más flexibles y promueve el uso de la bicicleta, lo que ayuda a reducir la congestión. Observando la gráfica, podemos notar que son muy pocas las estaciones que cuentan con biciestaciones. La troncal Américas es la que tiene más estaciones con biciestaciones, con un total de 5 estaciones, pero considerando la cantidad total de estaciones que tiene esta troncal, es un número muy reducido. Es preocupante analizar la troncal Caracas, considerada una de las más importantes de la ciudad, y ver que no cuenta con ninguna estación con biciestaciones. Lo mismo sucede con la NQS, otra troncal muy relevante en la ciudad, que solo tiene un total de 3 biciestaciones en sus muchas estaciones. Definitivamente, es necesario mejorar este aspecto. Trabajar en la expansión y mejora de las biciestaciones en las troncales no solo beneficiaría a los usuarios del transporte público, sino que también tendría un impacto positivo en la movilidad urbana y en la calidad de vida de los ciudadanos."),
        html.P("-Camila :"),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: "),

        html.H2("Conclusiones por participante del grupo:"),
        html.P("-Gabriela : La selección de la base de datos resultó ser un proceso interesante. Necesitábamos encontrar una base de datos pública que fuera relevante para nuestro proyecto. Finalmente, optamos por utilizar la base de datos de TransMilenio, dado que es un sistema de transporte de uso cotidiano y consideramos que explorarla más a fondo sería beneficioso. Durante este proceso, aprendimos mucho sobre las estaciones troncales del TransMilenio y su funcionamiento. Cumplimos con los objetivos del proyecto, que incluían el diseño y la carga de la base de datos, así como el análisis de diferentes escenarios utilizando visualizaciones apropiadas. El diseño de la base de datos presentó ciertas complicaciones, ya que nos encontramos con una gran cantidad de datos dispersos. Fue necesario analizar minuciosamente cada uno de ellos para identificar las conexiones y discrepancias. Resultó sorprendente descubrir que una entidad tan importante como TransMilenio no contaba con una estructura de base de datos claramente definida. Durante el proceso de carga de datos, surgieron algunos contratiempos. Al realizar la carga masiva, nos percatamos de varios errores en la base de datos, como la mezcla de paradas de SITP con troncales de TransMilenio y la presencia de identificadores duplicados en algunas troncales. Fue necesario corregir estos problemas para garantizar una carga de datos exitosa. Una vez completada la carga de datos, procedimos a analizar los escenarios que podríamos evaluar con la base de datos. Esta tarea resultó ser desafiante debido a la gran cantidad de datos duplicados. Además, tuvimos que determinar qué tipos de gráficas serían útiles para cada escenario evaluado. Aprendimos a utilizar diferentes herramientas, como DAS, para crear visualizaciones que facilitaran un análisis más completo. En conclusión, este proyecto fue una experiencia enriquecedora. Aprendimos mucho sobre SQL y DAS, así como sobre las estaciones troncales del TransMilenio y su importancia en el contexto del transporte público en la ciudad. Estamos satisfechos de haber cumplido con los objetivos del proyecto y esperamos poder aplicar estos conocimientos en futuros proyectos."),
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
