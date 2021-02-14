import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import time

import indexString
import Header 
import Footer  
import index
import Cursos

external_stylesheets = ['https://eteekin.eus/wp-content/uploads/2018/11/normalize_reset.css','https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP],title='CdP ESFM', update_title= None, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],suppress_callback_exceptions=True)
server = app.server

app.title = 'CdP ESFM '
app.index_string = indexString.string

app.layout = html.Div([
                    dcc.Location(id='url', refresh=False),
                    html.Div(id = 'layout-1')
                    ])

@app.callback([Output('layout-1','children')], [Input('url', 'pathname'), Input('url','href')])
def display_page(pathname, url):
    
    if pathname == '/' or pathname == '/acerca':
        return [[Header.header()] + index.acerca()+ Footer.footer()]
    elif pathname == '/cursos':
        return [[Header.header()] + Cursos.cursos()+ Footer.footer()]
    else:#if pathname == '/proyectos':
        return [[Header.header()] + Footer.footer()]

@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
@app.callback(Output("logo","src"),[Input('url', 'pathname')])
def actualizar_logo(url):
    time.sleep(1.45)
    return "https://fotos.subefotos.com/1416b6c9b4064c3979cc500bc069885co.png"

def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

app.callback(
    Output("modal-py", "is_open"),
    [Input("tpyt", "n_clicks"), Input("close-py", "n_clicks")],
    [State("modal-py", "is_open")],
)(toggle_modal)

if __name__ == '__main__':
    #print(dbc.themes.BOOTSTRAP)
    app.run_server(debug = True, host = '192.168.137.1')

