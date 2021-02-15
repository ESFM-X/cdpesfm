import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import time

import indexString, Header, Footer, index, Cursos, Proyectos, Soporte, send_email, Convocatoria

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
    elif pathname == '/proyectos':
        return [[Header.header()] +Proyectos.proyectos()+ Footer.footer()]
    elif pathname == '/soporte':
        return [[Header.header()] +Soporte.soporte()+ Footer.footer()]
    elif pathname == '/convocatoria':
        return [[Header.header()] +Convocatoria.convocatoria()+ Footer.footer()]
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

app.callback(
    Output("modal-ing", "is_open"),
    [Input("ting", "n_clicks"), Input("close-ing", "n_clicks")],
    [State("modal-ing", "is_open")],
)(toggle_modal)

app.callback(
    Output("modal-mat", "is_open"),
    [Input("tmat", "n_clicks"), Input("close-mat", "n_clicks")],
    [State("modal-mat", "is_open")],
)(toggle_modal)

@app.callback(
    [Output(f"collapse-{i}", "is_open") for i in range(1, 4)],
    [Input(f"group-{i}-toggle", "n_clicks") for i in range(1, 4)],
    [State(f"collapse-{i}", "is_open") for i in range(1, 4)],
)
def toggle_accordion(n1, n2, n3, is_open1, is_open2, is_open3):
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "group-1-toggle" and n1:
        return not is_open1, False, False
    elif button_id == "group-2-toggle" and n2:
        return False, not is_open2, False
    elif button_id == "group-3-toggle" and n3:
        return False, False, not is_open3
    return False, False, False

@app.callback(
    [Output('mensaje-exito','children'), Output('mensaje-error','children')],
    [Input('enviar','n_clicks')],
    [State('nombre','value'), State('correo','value'),State('interes','value'),State('comentario','value')]
)
def enviar_formulario(n, nombre, correo, interes, comentario):
    
    if n == None:
        return ['','']
    
    elif nombre == None or correo == None or interes == None or nombre == '' or correo == '' :
        return ['', 'Tienes que llenar todos los campos con *']
    else:
        print(send_email.enviar(nombre,correo,interes, comentario))
        return['Enviado con éxito','']

@app.callback(
    [Output('nombre','value'),Output('correo','value'),Output('interes','value'),Output('comentario','value')],
    [Input('mensaje-exito','children')]
)
def borrar_datos(mensaje):
    if mensaje == 'Enviado con éxito':
        return ['','','','']
    else:
        raise dash.exceptions.PreventUpdate()

if __name__ == '__main__':
    #print(dbc.themes.BOOTSTRAP)
    app.run_server(debug = True, host = '192.168.0.7')

