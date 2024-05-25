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
        html.P("-Camila : Esta gráfica muestra que Autonorte, Américas, NQS (juntando NQS-G y NQS-E) y Caracas (Que al igual que NQS, se junta Caracas-T y Caracas-S) son las troncales con la mayor cantidad de estaciones, de igual forma, se puede evidenciar que Autonorte y Américas tienen la misma cantidad de estaciones, lo mismo pasa con Suba y Calle 26 y Eje Ambiental y Tunal."),
        html.P("-Juan Esteban : A partir de la gráfica de pie se puede observar que entre el autonorte, las ámericas, la calle 26, la NQS (que se conforma por la NQS-G y la NQS-E) y la Caracas (que se conforma por Caracas-T y Caracas-S) son de las troncales con mayor número de estaciones, abarcando 99 estaciones entre las cinco troncales, siendo este el aproximado de 66.42%, un poco más de la mitad de las estaciones que posee trasmilenio."),
        html.P("-Juan Diego: Analizando este escenario podemos ver cada una de las troncales y su cantidad de estaciones en cada una, con esta podemos evidenciar la longitud e importancia de cada una de ellas, como por ejemplo lo son la Autonorte y la Américas, las cuales son las que mayor cantidad de personas transportan diariamente, o el Eje ambiental, que aunque su tramo es muy corto permite la movilidad de una gran cantidad de personas como universitarios y comerciantes en el centro de la ciudad."),

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
        html.P("-Camila : Se puede notar que en todas las troncales siempre hay por lo menos una estación con 6 vagones, siendo Héroes- Gel'Hada en Autonorte, Marsella en Américas, AV.Rojas en Calle 26 y AV.Chile en la NQS, también hay que notar que Banderas y los portales no tienen vagones, esto se debe a que la infrastructura de estos es más amplia y no tiene vagones, ya que la mayoría necesitan un espacio en el centro para los paraderos de lo Alimentadores, Flotas y demás, esto facilita el flujo de buses a través de estos, pero a la vez puede hacer más confuso para los usuarios el trasladarse y encontrar los paraderos de los buses que se quiera encontrar."),
        html.P("-Juan Esteban : Viendo las gráficas presentadas de las cinco troncales, podemos decir que la Caracas es la que tiene mayor número de vagones en total, siendo 67, seguida por el Autonorte con 59, luego la NQS con 57, en cuarto lugar las Américas con 49 y, finalmente, la Calle 26 con 44. Adicionalmente, podemos observar con más detalle que el Autonorte, la NQS y las Américas cuentan con algunas de las estaciones con mayor número de vagones (6), siendo Héroes, del Autonorte, Marsella, de las Américas y la Av. Chile, de la NQS. Esto puede ser positivo para los usuarios ya que garantiza un buen manejo del orden y tránsito entre las estaciones."),
        html.P("Adicionalmente, no podemos omitir que, al parecer, entre los portales y Banderas no cuentan con un número de vagones, lo cual puede ser debido a que se manejan diferente a una estación tradicional, siendo administradas a partir de su gran estructura y no por divisiones en vagones. Esto puede ser positivo debido a que, en caso de cambios de rutas, sería más fácil la adaptación de estas estaciones. De igual forma, podría tener un aspecto negativo a la hora de manejar la cantidad de personas que podrían llegar a transitar, pudiendo generar dificultades de movilidad para los usuarios."),
        html.P("-Juan Diego : Más profundamente aquí podemos ver con las 5 principales troncales las estaciones en cada una de ellas y empezar el análisis . Cómo podemos ver, las estaciones con mayor afluencia son las que tienen más de tres vagones en ellas, esto se dió porque al tener mayor cantidad de vagones, las rutas que pueden parar en estas estaciones son mucha más que si tuviera un número más reducido. También otro factor es que debido a la estructura de los portales, estos no cuentan como tal con vagones, sino que es una misma construcción por la facilidad y la cantidad de personas que pueden llegar a haber en estos puntos."),
        html.P("Como podemos ver, al analizar cada una de las estaciones, se evidencia que en la troncal de las Américas y la Autonorte, el movimiento según lo antes dicho puede llegar a ser mucho mayor en comparación de las otras troncales."),
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
        html.P("-Camila : En esta gráfica podemos ver que Autonorte es la troncal en la que sus estaciones tienen menos accesos, con solo 2 estaciones teniendo 2 accesos, Calle 100-Marketmedios y Alcalá, y Caracas es la troncal la cual tiene la mayor cantidad de estaciones con mayor cantidad de entradas, teniendo 20 estaciones con 2 entradas, esto es algo positivo ya que mayor cantidad de entradas significa mejor movilidad al entrar y salir de las estaciones, evitando aglomeraciones de gente haciendo fila para entrar y reduciendo la inseguridad ya que esto evita que en medio de las aglomeraciones se presenten robos."),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: Para empezar, podemos ver en cada una de las estaciones de cada una de las troncales un número diferente de entradas a cada una de ellas, tener más entradas también significa una mejor movilidad y fácil acceso para cada uno de los usuarios, un factor importante también es la seguridad, al mirar estaciones con mayor número de entradas podemos ver también menor congestión, lo que se puede traducir es en una menor posibilidad de robos, los accesos múltiples son más importantes para las estaciones que tienen mayor número de vagones, debido a su afluencia, como lo habíamos evidenciado en la situación anterior. Analizando más a fondo cada una de las troncales, en la primera: Auto norte, se pudo evidenciar que al compararlo con la afluencia evidenciada en la Calle 100 y Alcalá, estas cuentan con dos entradas a diferencia de una entrada como el resto de estaciones de esta troncal, si no fuera así, estas estaciones muy probablemente colapsaría más de lo que ya están en la actualidad."),
        html.P("Viendo las troncales de la Calle 26 y la NQS, estas tienen un número similar de entradas, lo que significa que tienen una buena afluencia y pueden sostener mayor número de usuarios. Para la caracas y las américas, el número de entradas promedio aumenta, evidenciando que estas troncales son muy transitadas por los usuarios y necesitan mayor número de entradas y salidas en cada una de sus estaciones."),
        html.H2("Cuarto escenario:"),
        html.P("-En este escenario se hace una suma de la cantidad de estaciones con componente Wifi por cada troncal, con esto poder saber cual es la troncal que tiene mayor cantidad de estaciones con Wifi"),
        html.P(""),
        dcc.Graph(
           id='Tabla12',
            figure=px.line(tr_co, x='Troncal_Estacion', y='Numero_Estaciones_Con_Wifi', title='Cantidad de Wifi por Troncal', color_discrete_sequence=["#820000"])
        ),


        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela : Tener wifi en las estaciones es beneficioso, ya que proporciona una mejor experiencia en el uso del transporte público y permite acceder a información sobre horarios y rutas alternativas. En caso de emergencia, el usuario tendrá una forma más accesible de comunicarse con una autoridad. Al analizar la gráfica, podemos observar qué CR7-10, Suba, NQS y Caracas tienen un mayor número de estaciones con wifi, mientras que Autonorte y Calle 26 tienen un bajo número de estaciones con wifi en relación con su cantidad total. Por otro lado, Soacha, Tunal y Eje Ambiental son las troncales que tienen menos estaciones con wifi, pero hay que tener en cuenta que estas troncales tienen muy pocas estaciones en total."),
        html.P("-Camila : Como se puede apreciar, la troncal Caracas es la troncal que presenta una mayor cantidad de estaciones que ofrecen Wifi, esto es beneficioso y útil para el usuario, facilitando el acceso a información sobre rutas y horarios, facilitando la movilidad y la accesibilidad para los usuarios de Transmilenio, comparado con Soacha, Eje Ambiental y Tunal, pero de igual forma, hay que tener en cuenta que estas troncales son las que presentan la menor cantidad de estaciones."),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: Se puede evidenciar un número variado de puestos Wifi en cada una de las troncales, este análisis dice que entre mayor sea el número de estaciones y mayor sea la afluencia en ellas, es más probable que existan mayor cantidad de puestos de wifi en las troncales. Esta es una necesidad ajustada al contexto de hoy en día con la revolución de tecnologías, el contacto de emergencia puede surgir en cualquier momento, y que estaciones cuenten con estas tecnologías es muy necesario en caso de alguna situación de emergencia."),

        html.H2("Quinto escenario:"),
        html.P("-En este escenario se hace una suma de la cantidad de estaciones con biciestacion por cada troncal, con esto poder saber cual es la troncal que tiene mayor cantidad de biciestacion"),

        dcc.Graph(
            id='Tabla13',
            figure=px.line(tr_bi, x='Troncal_Estacion', y='Biciestacion', title='Cantidad de Biciestaciones por Troncal', color_discrete_sequence=["#f8da45"])
        ),

        html.H3("Analisis por integrante de grupo:"),
        html.P("-Gabriela : Tener biciestaciones en las estaciones es importante, ya que hace que sea más accesible llegar a ellas, permite viajes más flexibles y promueve el uso de la bicicleta, lo que ayuda a reducir la congestión. Observando la gráfica, podemos notar que son muy pocas las estaciones que cuentan con biciestaciones. La troncal Américas es la que tiene más estaciones con biciestaciones, con un total de 5 estaciones, pero considerando la cantidad total de estaciones que tiene esta troncal, es un número muy reducido. Es preocupante analizar la troncal Caracas, considerada una de las más importantes de la ciudad, y ver que no cuenta con ninguna estación con biciestaciones. Lo mismo sucede con la NQS, otra troncal muy relevante en la ciudad, que solo tiene un total de 3 biciestaciones en sus muchas estaciones. Definitivamente, es necesario mejorar este aspecto. Trabajar en la expansión y mejora de las biciestaciones en las troncales no solo beneficiaría a los usuarios del transporte público, sino que también tendría un impacto positivo en la movilidad urbana y en la calidad de vida de los ciudadanos."),
        html.P("-Camila : Las biciestaciones facilitan la llegada a las estaciones, ya que muchos usuarios llegan mediante bicicletas, y esto resuelve el problema de muchos usuarios sobre donde guardar las bicicletas al llegar, evitando la inseguridad de dejarlas en la calle y la incomodidad de otros usuarios ya que ya no tienen que llevar la bicicleta en los buses de transmilenio a otro lugar en el que lo puedan dejar. En esta gráfica se ve que Autonorte no tiene ninguna biciestación al igual que Calle 6, Autonorte, Eje Ambiental, Tunal y Caracas, y por el contrario, Americas es la troncal con mayor cantidad de biciestaciones, contando con 5 biciestaciones en total."),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego:  Las bicicletas son un medio de transporte por excelencia para cortas o medianas distancias, el sistema de Transmilenio cuenta en muchas partes con alimentadores que pasan desde las estaciones más concurridas hasta partes en donde el transmilenio muchas veces no llega, pero no es así en todos los casos, por ejemplo en la troncal de las américas, no existen en muchas partes estos llamados alimentadores, por lo que la necesidad de llegar a las estaciones principales se traslada a las bicicletas, y el guardarlas en estos lugares cómo son las biciestaciones se vuelve fundamental."),

        html.H2("Conclusiones por participante del grupo:"),
        html.P("-Gabriela : La selección de la base de datos resultó ser un proceso interesante. Necesitábamos encontrar una base de datos pública que fuera relevante para nuestro proyecto. Finalmente, optamos por utilizar la base de datos de TransMilenio, dado que es un sistema de transporte de uso cotidiano y consideramos que explorarla más a fondo sería beneficioso. Durante este proceso, aprendimos mucho sobre las estaciones troncales del TransMilenio y su funcionamiento. Cumplimos con los objetivos del proyecto, que incluían el diseño y la carga de la base de datos, así como el análisis de diferentes escenarios utilizando visualizaciones apropiadas. El diseño de la base de datos presentó ciertas complicaciones, ya que nos encontramos con una gran cantidad de datos dispersos. Fue necesario analizar minuciosamente cada uno de ellos para identificar las conexiones y discrepancias. Resultó sorprendente descubrir que una entidad tan importante como TransMilenio no contaba con una estructura de base de datos claramente definida. Durante el proceso de carga de datos, surgieron algunos contratiempos. Al realizar la carga masiva, nos percatamos de varios errores en la base de datos, como la mezcla de paradas de SITP con troncales de TransMilenio y la presencia de identificadores duplicados en algunas troncales. Fue necesario corregir estos problemas para garantizar una carga de datos exitosa. Una vez completada la carga de datos, procedimos a analizar los escenarios que podríamos evaluar con la base de datos. Esta tarea resultó ser desafiante debido a la gran cantidad de datos duplicados. Además, tuvimos que determinar qué tipos de gráficas serían útiles para cada escenario evaluado. Aprendimos a utilizar diferentes herramientas, como DAS, para crear visualizaciones que facilitaran un análisis más completo. En conclusión, este proyecto fue una experiencia enriquecedora. Aprendimos mucho sobre SQL y DAS, así como sobre las estaciones troncales del TransMilenio y su importancia en el contexto del transporte público en la ciudad. Estamos satisfechos de haber cumplido con los objetivos del proyecto y esperamos poder aplicar estos conocimientos en futuros proyectos."),
        html.P("-Camila : La selección de la base de datos fue algo largo de decidir, debido a que no encontrabamos una base de datos pública que nos pareciera relevante o coherente a lo que queríamos hacer. Pero al final se encontró múltiples base de datos oficiales de Transmilenio, al final decidimos por la base de datos que contenía la información sobre troncales y estaciones con sus respectivas características."),
        html.P("A pesar de que era una base de datos oficial, esta estaba muy desordenada, contando con datos repetidos, atributos que no eran claros y tablas que no eran necesarias, de igual forma estas tablas se ordenaron y se removieron los datos innecesarios, llegando a la carga de datos que fue algo larga debido a la cantidad de tablas y datos que contenían."),
        html.P("Finalmente, tuvimos que pensar en las gráficas que se podían hacer con estos datos, esto fue algo complicado ya que no sabíamos bien qué gráficas podrían ser útiles para el usuario o los administradores de este mismo y que conectaran los datos de las tablas, al final optamos por las gráficas que se vieron previamente."),
        html.P("En conclusión, este proyecto nos permitió conocer las diversas bases de datos que se pueden crear mediante información brindada ya sea por páginas o fuentes oficiales, esto es muy útil a futuro para creación de bases de datos aún más grandes ya sea para empresas o demás. Esta clase de proyectos, aunque pueden llegar a ser algo extensos y complejos, son interesantes y útiles y se espera volver a hacer un proyecto similar."),
        html.P("-Juan Esteban :"),
        html.P("-Juan Diego: En primer punto, el escoger una base de datos que cuente con cada uno de los requisitos del proyecto fue un poco complicado, que sea una base de datos disponible, actual y completa complicó la tarea a la hora de buscarla, pero al encontrar una base de datos como la de Transmilenio que es tan cotidiana para cada uno de nosotros, decidimos usarla. Diseñar la base de datos no fue un problema mayor con las herramientas con las que contábamos, como el primer paso que era normalizar, hacer el MER y ajustar cada uno de los parámetros,  la carga de datos después del diseño de la base de datos fue eficiente, aunque tuvimos algunos problemas con los datos que muchas veces no estaban con el orden o no estaban completos, por lo que muchas veces tuvimos que ver cada uno de los datos que faltaban para arreglarlos manualmente, nos tocó arreglar el tema de las troncales que a veces se cruzaban los datos o estaciones que no existían y que hacían parte del sistema de  SITP. Muchas veces surgen datos que se veían dos veces y no dejaban la funcionalidad de la base de datos adecuadamente. La visualización de los datos también fue un paso importante, ya que visualmente se puede ver de una mejor manera, el DASH nos ayudó con este trabajo en donde pudimos ver ya el avance que habíamos hecho en el proyecto utilizando diferentes métodos de visualización. Con cada uno de los escenarios estuvimos muy contentos ya que los datos se podían ver el análisis que nosotros como estudiantes que nos movilizamos en este medio de transporte vemos día a día. La verdad fue un reto interesante y divertido pese a los inconvenientes. "),

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
