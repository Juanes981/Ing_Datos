import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Datos de ejemplo
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Crear una figura usando Plotly Express
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Diseño de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Mi Dashboard con Dash'),

    html.Div(children='''
        Ejemplo sencillo de un dashboard usando Dash y Plotly.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=False)
