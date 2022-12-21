import dash
from dash.html.Button import Button
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State
import plotly.express as px
from pages import lesson1, lesson2, startpage, text1, text2, test1, test2 

app= dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.title='Deutsch'
server=app.server


                          
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
    ]
                      )




@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'))

def display_page(pathname):
    if pathname == '/':
        return startpage.layout
    elif pathname == '/pages/lesson1':
        return lesson1.layout
    elif pathname == '/pages/lesson2':
        return lesson2.layout
    elif pathname == '/pages/text1':
        return text1.layout
    elif pathname == '/pages/text2':
        return text2.layout
    elif pathname == '/pages/test1':
        return test1.layout
    elif pathname == '/pages/test2':
        return test2.layout
    else:
        return '404'



if __name__ == "__main__":
    app.run_server()