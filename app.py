### Local imports
import time, random, string, datetime, requests, json

### Dash packages
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

### DB packages
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


### Local modules
from config import indexString
from dash_templates import Header, Footer, index, Cursos, Proyectos, Soporte, Search
from datos_alumnos import  Certificados
from formularios import send_email, Convocatoria, Enviar, Encuestas
from secret import apikeys
from config import periodo

cred = credentials.Certificate("secret/formularioesfm-firebase-adminsdk-f9csg-da5faa24f2.json")
firebase_admin.initialize_app(cred,{'projectId': 'formularioesfm'},'pagina')#,{'projectId': 'formularioesfm'},'pagina')
db = firestore.client()
# intento = 0

external_stylesheets = ['https://eteekin.eus/wp-content/uploads/2018/11/normalize_reset.css','https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP],title='CdP ESFM', update_title= None, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],suppress_callback_exceptions=True)
server = app.server
app.callback_modal = False
app.title = 'CdP ESFM '
app.index_string = indexString.string
color_fondo = '#061d47'
margen = 25
color_letra = '#ffffff'
color_footer = '#8f8f8f'

app.layout = html.Div([
                    dcc.Store(id='memory_test404'),dcc.Store(id='memory_test'),dcc.Store(id='session-stored2', data=[],storage_type='session'),
                    dcc.Location(id='url', refresh=False),
                    html.Div(id = 'layout-1')
                    ])


@app.callback([Output('layout-1','children')], [Input('url', 'pathname'), Input('url','href')])
def display_page(pathname, url):
    
    if "/constancias" in pathname:
        return [[Header.header()] + Certificados.cursos(pathname[13:]) + Footer.footer()]
    elif "/encuesta/2021-2" in pathname: 
        return [[Header.header()]+ Encuestas.encuesta_satis() + Footer.footer()]
    elif "/constancia" in pathname:
        return [ [Header.header()] + Certificados.certificado(pathname[12:])+ Footer.footer()]
    elif pathname == '/' or pathname == '/acerca':
        return [[Header.header()] + index.acerca()+ Footer.footer()]
    elif pathname == '/cursos':
        return [[Header.header()] + Cursos.cursos(app)+ Footer.footer()]
    elif pathname == '/proyectos':
        return [[Header.header()] +Proyectos.proyectos()+ Footer.footer()]
    elif pathname == '/soporte':
        return [[Header.header()] +Soporte.soporte()+ Footer.footer()]  
    elif pathname == '/convocatoria':
        return [[Header.header()] +Convocatoria.convocatoria_expired()+ Footer.footer()] #convocatoria_expired
    elif pathname[0:7] == '/search':
        return [[Header.header()] + [Search.page] + Footer.footer()]
    elif pathname == '/perfil':
        return [[Header.header()]  + Footer.footer()]
    else:
        return [[Header.header()] + index.acerca() + Footer.footer()]

######################################################################################### Funciones Bootstrap

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
    return "https://cdn.discordapp.com/attachments/798047392405913601/811435939284254740/CdP_ESFM.gif"

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

######################################################################################### Enviar correo de Soporte
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
    [Output('nombre','value'),Output('interes','value'),Output('comentario','value')],
    [Input('mensaje-exito','children')]
)
def borrar_datos(mensaje):
    if mensaje == 'Enviado con éxito':
        return ['','','']
    else:
        raise dash.exceptions.PreventUpdate()

######################################################################################### ENCUESTAS
@app.callback(
    [Output('cursos','value'),Output('motivo','value'),Output('comentario_encuesta','value')],
    [Input('Confirmacion_encuesta','children')]
)
def borrar_datos(mensaje):
    if mensaje == 'Enviado con éxito, agradecemos tus comentarios':
        return ['','','']
    else:
        raise dash.exceptions.PreventUpdate()

@app.callback([Output('Confirmacion_encuesta', 'children'), Output('Confirmacion_encuesta','style')],
              [Input('go_encuesta', 'n_clicks')],
                [State('cursos', 'value'),State('motivo', 'value'),State('comentario_encuesta', 'value')],
            )
def enviar(n_clicks, cursos, motivo, comentario):
    if n_clicks:
        if cursos and motivo: 
        
            doc_ref = db.collection('Encuesta 2021-2').document(''.join([random.choice('qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMÑ1234567890') for _ in range(7)] ) )  
            doc_ref.set({
                    u'cursos': cursos,
                    u'cursos': cursos,
                    u'motivo': motivo,
                    u'comentario': comentario
            })
            return ['Enviado con éxito, agradecemos tus comentarios',{'color':'green', 'padding':10}]
        elif n_clicks >= 1:
            return ['Tienes que llenar todos los campos',{'color':'#7b1448', 'padding':10}]
        else:
            return ['',{'color':'#db0000', 'padding':10}]
    else:
        raise dash.exceptions.PreventUpdate()


######################################################################################### Convocatoria
@app.callback([Output('curso', 'options')], [Input('curso', 'value')], [State('curso','options')])
def deshabilitar_cursos(cursos, options):
        return [options]

@app.callback([Output('Confirmacion', 'children'), Output('Confirmacion','style')],
            [Input('go', 'n_clicks'), Input('session-stored2','data')],
            [State('name', 'value'),State('boleta', 'value'),State('correo', 'value'),
                State('carrera', 'value'),State('semestre', 'value'),State('curso', 'value'),
                State('objetivo', 'value')],
            )
def enviar(n_clicks,data,*args):
    if n_clicks:
        if  len(list(args)[0]) != 0 and args[1] != '' and len(list(args)[2]) != 0  and len(list(args)[3]) != 0 and len(list(args)[5]) != 0 and len(list(args)[6]) != 0:#varios cursos and args[8] !=[''] and args[8] != None: 
            dato = {'ruta':'cdp', 
                    'args':{
                            'nombre': args[0], 
                            'boleta': args[1], 
                            'email': args[2], 
                            'carrera': args[3], 
                            'semestres_ini': args[4], 
                            'cursos': ([[args[5]]] if type(args[5])!= list else [args[5]]),
                            'periodo': periodo.periodo_actual,
                            'objetivo': args[6], 
                            },
                    'metodo':requests.post
                    }  
            print(dato['args']['cursos'])
            response = dato['metodo'](apikeys.url + f'{dato["ruta"]}/{apikeys.key}', json=dato['args'] )
            if str(response.status_code)[0] == '2':
                token_response = response.json()['token']
                #intento = Enviar.send_email(args[2],args[0],token_response,args[5])
                return [f'¡Registro concluido con éxito! ID: {token_response}. \n Te hemos enviado un correo (revisa en Spam).',{'color':'#39A051', 'font-size':'1.2em', 'padding':10}]#,args[6]]
                
            elif str(response.status_code)[0] == '4' :
                if 'error' in response.json(): 
                    print(response.json()['error'])
                return [f'Datos ya registrados, si se trata de un error pone en contácto: contact@esfm-x.com',{'color':'#db0000', 'padding':10}]
            else: 
                print(response.json()['error'])
                return [f'Lo sentimos, nuestros servidores están fallando. Inténtalo en unos minutos.',{'color':'#db0000', 'padding':10}]
        
        elif n_clicks >= 1:
            return ['Tienes que llenar todos los campos',{'color':'#7b1448', 'padding':10}]
        else:
            return ['',{'color':'#db0000', 'padding':10}]
    else:
        raise dash.exceptions.PreventUpdate()

@app.callback([Output('go','children'), Output('go_link','href'), Output('go_link','target')], [Input('curso','value')])
def ac_buttom(curso):
    if (curso == 'Ingenieria-datos' or curso == 'Pandas-ciencia'):

        return ['Enviar','javascript:void(0);','_self']
    else:
        return ['Enviar','javascript:void(0);','_self']

############################################# Datos en la base de datos
@app.callback([Output('name', 'value'),Output('boleta', 'value'),Output('correo', 'value'),Output('carrera', 'value'),Output('semestre', 'value'),Output('curso', 'value'), Output('objetivo','value'), Output('name', 'disabled'),Output('boleta', 'disabled'), Output('mensaje-id', 'children')],#,Output('objetivo', 'value')],
                [Input('Confirmacion', 'children'), Input('id_boton', 'n_clicks')], [State('id_anterior','value' )])
def borrar(mensaje, n, ide):
    if n:
        datos = obtener_datos(ide)
        if datos: 
            return datos[0], datos[1], datos[2],datos[3], datos[4],'','', True, True,[html.P('Datos cargados con éxito.', style = {'color': '#39A051'})] 
        return '','','','',1,'','', False, False, [html.P('El ID no ha sido encontrado.', style = {'color': '#7b1448'})]
    mensaje = mensaje if type(mensaje) == str else ''
    if 'Lo sentimos, nuestros servidores' in mensaje or '¡Registro concluido con éxito!' in mensaje or 'Formulario enviado con éxito,' in mensaje: 
            return ['','','','',1,'','', False, False, []]
    else:
        raise dash.exceptions.PreventUpdate()

def obtener_datos(ide):
    dato = {'ruta':'cdp', 
                    'args':{
                            'datos':'alumnos_anteriores',
                            'boleta': ide, 
                            'periodo': periodo.periodo_actual,
                            },
                    'metodo':requests.get
                    }  
    response = dato['metodo'](apikeys.url + f'{dato["ruta"]}/{apikeys.key}', dato['args'] )

    if response.status_code == 200:
        datos = response.json()['datos']
        
        return datos['nombre'], datos['boleta'], datos['email'], datos['carrera'], obtener_semestre_actual(datos['periodo'] ,int(datos['semestres_ini']) )

    else:
        print(response.json())
        return False    
def obtener_semestre_actual(periodo_inicial, semestre_inicial ):
    año_inicial = int(periodo_inicial[0:4])
    año_actual = int(periodo.periodo_actual[0:4])
    semestres = 2*(año_actual-año_inicial) + semestre_inicial
    if periodo_inicial == periodo.periodo_actual:
        return semestre_inicial
    if año_inicial == año_actual:
        return semestres + 1 
    if periodo_inicial[-1] != periodo.periodo_actual[-1]:
        return semestres+1
    return semestres

######################################################################################### Búsqueda
@app.callback(
    [ Output('url','pathname')],
    [Input('search','n_clicks')],
    [State('search_input','value')]
)
def searching(n,text):
    if n != None:
        try:
            return ['/search&q='+text.replace(' ','+')]
        except:
            return ['/search*']
    else:
        raise dash.exceptions.PreventUpdate()

@app.callback(
    [Output('busqueda_p','children'), Output('search_input','value')],
    [Input('search','n_clicks')],
    [State('url','pathname'), State('busqueda_p','children')]
)
def search_title(n,text, busqueda):
    
    if '/search&q=id:' in text.lower():
        datos = obtener_datos(text[14:])
        if datos:
            return Convocatoria.convocatoria(), ''
        else:
            return [html.H1('Error'),'El ID no ha sido encontrado.'],''
    
    if '/search' in text:
        if text == '/search*':
            return [html.H1('Búsqueda'), html.Div(html.Img(src = 'https://raw.githubusercontent.com/gist/T-Jedsada/dbee22959762fa6c0ccad8153830b51a/raw/8957088c2e31dba6d72ce86c615cb3c7bb7f0b0c/nyan-cat.gif', style = {'width':'300px'}), style = {'width':'350px','margin-left':'auto','margin-right':'auto'}), html.Br(), '¡Has encontrado un Easter egg! En el CdP ESFM reconocemos a los curiosos, así que no dudes en hacernos saber que eres uno.'],''
        try:
            return [[html.H1('Búsqueda'),'No existe ningún resultado para ', html.P(text[10:].replace('+',' '), style = {"font-weight":"bold", "display":"inline"})],text[10:].replace('+',' ')]
        except:
            return [html.H1('Búsqueda'),'Introduce un término y luego realiza la búsqueda'],''
    else:
        raise dash.exceptions.PreventUpdate()
                                                            
if __name__ == '__main__':
    
    app.run_server(debug = True)

