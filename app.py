# Importing packages
from dash import Dash, html, dash_table
import pandas as pd

# Adding data
df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My first App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])

# To run the app:
if __name__ == '__main__':
    app.run_server(debug=True)
