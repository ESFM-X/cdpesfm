import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import time, random, string, datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import indexString, Header, Footer, index, Cursos, Proyectos, Soporte, send_email, Convocatoria, Enviar, Search

cred = credentials.Certificate("formularioesfm-firebase-adminsdk-f9csg-da5faa24f2.json")
firebase_admin.initialize_app(cred,{'projectId': 'formularioesfm'},'pagina')#,{'projectId': 'formularioesfm'},'pagina')
db = firestore.client()
intento = 0

external_stylesheets = ['https://eteekin.eus/wp-content/uploads/2018/11/normalize_reset.css','https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP],title='CdP ESFM', update_title= None, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],suppress_callback_exceptions=True)
server = app.server

app.title = 'CdP ESFM '
app.index_string = indexString.string
color_fondo = '#061d47'
margen = 25
color_letra = '#ffffff'#'#061d47'
color_footer = '#8f8f8f'

app.layout = html.Div([
                    dcc.Store(id='memory_test404'),dcc.Store(id='memory_test'),dcc.Store(id='session-stored2', data=[],storage_type='session'),
                    dcc.Location(id='url', refresh=False),
                    html.Div(id = 'layout-1')
                    ])
##Local
def sleep(num):
    time.sleep(num)
def load_key():
    return open("secret.key", "rb").read()
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_message)
def get_random_string(length):
    letters = string.ascii_lowercase + '123456789'
    return ''.join(random.choice(letters) for i in range(length))
def confirmar_id(ide):
        #print(ide,'confirmar')
    respuestas = db.collection(u'Respuestas')
    query_ref = respuestas.where(u'Id',u'==',ide)
    registros = query_ref.stream()
    for registro in registros:
        return registro.to_dict()['Id']#, registro.to_dict()['Boleta']
def confirmar_correo(correo, boleta):
        #print(ide,'confirmar')
    respuestas = db.collection(u'Id-correo')
    query_ref = respuestas.where(u'Correo',u'==',correo)
    query_ref2 = respuestas.where(u'Boleta',u'==',boleta)
    registros = query_ref.stream()
    registros2 = query_ref2.stream()
    for registro in registros:
        #print('\n\n REGISTRO:',registro.to_dict()['Curso'],registro2.to_dict()['Curso'],'\n\n DATOS:', correo, boleta,'\n\n\n')
        return registro.to_dict()['Curso']

    for registro in registros2:
        return registro.to_dict()['Curso']
#Callbacks
#@app.callback(Output('url','href'), [Input('url','pathname')], [State('url', 'href')])
#def change_url(url, href):
#    print(href)
#    if str(href)[0:4] == 'http':
#        print('*** https' + href[4:])
#        return 'https' + href[4:]
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
    elif pathname[0:7] == '/search':
        return [[Header.header()] + [Search.page] + Footer.footer()]
    else:#if pathname == '/proyectos':
        return [[Header.header()] + index.acerca() + Footer.footer()]

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
    #print('Entraste')
    #time.sleep(1.45)
    return "https://cdn.discordapp.com/attachments/798047392405913601/811435939284254740/CdP_ESFM.gif"

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
app.callback(
    Output("modal-pya", "is_open"),
    [Input("tpya", "n_clicks"), Input("close-pya", "n_clicks")],
    [State("modal-pya", "is_open")],
)(toggle_modal)
app.callback(
    Output("modal-crip", "is_open"),
    [Input("tcrip", "n_clicks"), Input("close-crip", "n_clicks")],
    [State("modal-crip", "is_open")],
)(toggle_modal)
app.callback(
    Output("modal-wol", "is_open"),
    [Input("twol", "n_clicks"), Input("close-wol", "n_clicks")],
    [State("modal-wol", "is_open")],
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
    [Output('nombre','value'),Output('interes','value'),Output('comentario','value')],
    [Input('mensaje-exito','children')]
)
def borrar_datos(mensaje):
    if mensaje == 'Enviado con éxito':
        return ['','','']
    else:
        raise dash.exceptions.PreventUpdate()
#########################################################################################
@app.callback([Output('Confirmacion', 'children'), Output('Confirmacion','style')],# Output('objetivo','value')],
              [Input('go', 'n_clicks'), Input('session-stored2','data')],
                [State('name', 'value'),State('boleta', 'value'),State('correo', 'value'),State('carrera', 'value'),State('semestre', 'value'),State('curso', 'value'),State('objetivo', 'value'),State('Accepted','value'),
                State('disponibilidad','value')],
            )
def enviar(n_clicks,data,*args,**kwargs):

    #print(data[-1], list(args[:-1]))
    ####global intento
    #print(args[8], type(args[8]), args)
    if n_clicks:
        for dat in data[:-1]:
            if dat == list(args[:-1]) and dat[0] != '':
                intento = 0
                return [f'Formulario ya enviado',{'color':'#db0000', 'padding':10}]#,args[6]]
        if args[5] == 'Ingenieria-datos' or args[5] == 'Pandas-ciencia':
            if args[7]!= ['Accepted']:
                intento = 0
                #print(args[7])
                return ['Es indispensable saber Python para inscribir ese curso. Te recomendamos tomar el curso de Python from zero to hero.',{'color':'#7b1448', 'padding':10}]#,args[6]+' ']
        if  len(list(args)[0]) != 0 and args[1] != '' and len(list(args)[2]) != 0  and len(list(args)[3]) != 0 and len(list(args)[5]) != 0 and len(list(args)[6]) != 0 and args[8] !=[''] and args[8] != None: 
            curso_tomado =  confirmar_correo(args[2], args[1])
            if curso_tomado:
                return [f'Ya estás inscrito al curso de {curso_tomado}',{'color':'#7b1448', 'padding':10}]#,args[6]]
            else:
                id_registro = args[5][0:2].lower() + get_random_string(5)
                #print('ENVIADOS: ',list(args))
                doc_ref = db.collection(args[5]).document(id_registro)
                hora = datetime.datetime.now()
                hora = str(hora.day) + '-' + str(hora.month) + '-' + str(hora.year) + ' ' + str(hora.hour) + ':' + str(hora.minute) + ':' + str(hora.second)
                doc_ref.set({
                    u'Nombre': args[0],
                    u'Boleta': args[1],
                    u'Correo': args[2],
                    u'Carrera': args[3],
                    u'Semestre': args[4],
                    u'Curso': args[5],
                    u'Objetivo': args[6],
                    u'Horario': args[8],
                    u'Hora': hora,
                    u'Id': id_registro
                })
                doc_ref = db.collection('Id-correo').document(id_registro)
                doc_ref.set({u'Correo':args[2], u'Id':id_registro,u'Curso':args[5],u'Boleta':args[1]})
                intento = Enviar.send_email(args[2],args[0],id_registro,args[5])
                if intento == 1:
                    return [f'¡Registro concluido con éxito!    ID: {id_registro}. \n Te hemos enviado un correo (revisa en Spam).',{'color':'#39A051', 'font-size':'1.2em', 'padding':10}]#,args[6]]
                elif intento == 0:
                    doc_ref = db.collection('Errors-email').document(id_registro)
                    doc_ref.set({u'Correo':args[2],u'Curso': args[5]})
                    return [f'Formulario enviado con éxito, pero no fue posible enviarte un correo. Ponte en contacto a soporte@cdpesfm.college con tu ID: {id_registro}.',{'color':'#db0000', 'padding':10}]#,args[6]]
        elif n_clicks >= 1:
            intento = 0
            return ['Tienes que llenar todos los campos',{'color':'#7b1448', 'padding':10}]#,args[6]+' ']
        else:
            intento = 0
            return ['',{'color':'#db0000', 'padding':10}]#,args[6]]
    else:
        raise dash.exceptions.PreventUpdate()

@app.callback([Output('name', 'value'),Output('boleta', 'value'),Output('correo', 'value'),Output('carrera', 'value'),Output('semestre', 'value'),Output('curso', 'value'), Output('objetivo','value')],#,Output('objetivo', 'value')],
                [Input('Confirmacion', 'children')])
               # [State('Confirmacion', 'children')])
def borrar(mensaje):
    #print(mensaje)
    mensaje = mensaje if type(mensaje) == str else ''
    if 'Ya estás inscrito al curso de' in mensaje or '¡Registro concluido con éxito!' in mensaje or 'Formulario enviado con éxito,' in mensaje: 
       # if n_clicks >= 1:
            return ['','','','',1,'','']#,'']
       # else:
        #    return ['','','','',1,'']#,'']
    else:
        raise dash.exceptions.PreventUpdate()





@app.callback([Output('Python_accept','children')],[Input('curso','value')])
def gen_accept(curso):
    if curso == 'Ingenieria-datos' or curso == 'Pandas-ciencia': 
        return [dbc.Checklist( id = 'Accepted', options=[{'label': ' Confirmo que sé Python', 'value': 'Accepted'}],style = {'margin-top':8, 'color': '#000'})]
    else:
        return [dcc.Checklist(id = 'Accepted')]
@app.callback([Output('go','children'), Output('go_link','href'), Output('go_link','target')], [Input('curso','value')])
def ac_buttom(curso):
    global intento
    #print(intento)
    if (curso == 'Ingenieria-datos' or curso == 'Pandas-ciencia'):

        return ['Enviar','javascript:void(0);','_self']
    else:
        return ['Enviar','javascript:void(0);','_self']
@app.callback([Output('elegir_horario','children')],[Input('curso','value')])
def elegir_horario(curso):
    titulo = [html.H6('Elige tu disponibilidad de horario:')]
    if curso == '':
        return [titulo+[html.P('Elige un curso',style = {"color": "#8f8f8f"}),dbc.Checklist(id = 'disponibilidad',
                #options=[{'label': '  Elige un curso', 'value': 'Lun'},],
                value=[''])]]

    elif curso == 'Python-zh':
        return [titulo+[dbc.Checklist(id = 'disponibilidad',options=[
                            {'label': '  Lun 11:00 - 12:00', 'value': 'Lun'},
                            {'label': u'  Mié 14:00 - 15:00', 'value': 'Mie'},
                            #{'label': '  Los dos', 'value': 'All'},
                        ],value=[''])]]
    elif curso == 'Ingenieria-datos':
        return [titulo+[dbc.Checklist(id = 'disponibilidad',options=[
                            {'label': '  Mar 10:00 - 11:00', 'value': 'Mar10'},
                            {'label': u'  Mar 13:00 - 14:00', 'value': 'Mar13'},
                            #{'label': '  Los dos', 'value': 'All'},
                        ],value=[''])]]
    elif curso == 'Pandas-ciencia':
        return [titulo+[dbc.Checklist(id = 'disponibilidad',options=[
                            {'label': '  Jue 13:00 - 14:00', 'value': 'Jue'},
                            {'label': u'  Vie 11:00 - 12:00', 'value': 'Vie'},
                            #{'label': '  Los dos', 'value': 'All'},
                        ],value=[''])]]
    elif curso == 'Matlab':
        return [titulo+[dbc.Checklist(id = 'disponibilidad',options=[
                            {'label': '  Jue 14:30 - 15:30', 'value': 'Jue'},
                            {'label': '  Mar 14:30 - 15:30', 'value': 'Mar'},
                        ],value=[''])]]
    

@app.callback(
    [ Output('url','pathname')],
    [Input('search','n_clicks')],
    [State('search_input','value')]
)
def searching(n,text):
    
    if n != None:
        return ['/search&q='+text.replace(' ','+')]
        
    else:
        raise dash.exceptions.PreventUpdate()

@app.callback(
    [Output('busqueda_p','children'), Output('search_input','value')],
    [Input('search','n_clicks')],
    [State('url','pathname')]
)
def search_title(n,text):
    
    if '/search' in text:
        #print(text, "dsadssd")
        try:
            return [['Resultados de la búsqueda para ', html.P(text[10:].replace('+',' '), style = {"font-weight":"bold", "display":"inline"})],text[10:].replace('+',' ')]
        except:
            return ['Introduce un término y luego realiza la búsqueda'],''
    else:
        raise dash.exceptions.PreventUpdate()

if __name__ == '__main__':
    #print(dbc.themes.BOOTSTRAP)
    app.run_server(debug = True, host = '192.168.0.7')

