import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import time, random, string, datetime
import indexString
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import indexString, ides2021, Header, Footer, index, Cursos, Proyectos, Soporte, send_email, Convocatoria, Enviar, Search, Datos, Ingresar, Certificados, Encuestas

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
        return registro.to_dict()['Cursos']

    for registro in registros2:
        return registro.to_dict()['Cursos']
#Callbacks
#@app.callback(Output('url','href'), [Input('url','pathname')], [State('url', 'href')])
#def change_url(url, href):
#    print(href)
#    if str(href)[0:4] == 'http':
#        print('*** https' + href[4:])
#        return 'https' + href[4:]
@app.callback([Output('layout-1','children')], [Input('url', 'pathname'), Input('url','href')])
def display_page(pathname, url):
    ides = ides2021.dicti()
    try:
        f = int(pathname[1:])
    except:
        f = None

    if f in ides:
        return [[Header.header()] + Certificados.cursos(ides[f]) + Footer.footer()]
    elif "/encuesta/2021-2" in pathname: 
        return [[Header.header()]+ Encuestas.encuesta_satis() + Footer.footer()]
    elif "/constancia" in pathname:
        #print(pathname[12:])
        return [ [Header.header()] + Certificados.certificado(pathname[12:])+ Footer.footer()]
    elif pathname == '/' or pathname == '/acerca':
        return [[Header.header()] + index.acerca()+ Footer.footer()]
    elif pathname == '/cursos':
        return [[Header.header()] + Cursos.cursos()+ Footer.footer()]
    elif pathname == '/proyectos':
        return [[Header.header()] +Proyectos.proyectos()+ Footer.footer()]
    elif pathname == '/soporte':
        return [[Header.header()] +Soporte.soporte()+ Footer.footer()]  
    elif pathname == '/convocatoria':
        return [[Header.header()] +Convocatoria.convocatoria2()+ Footer.footer()]
    elif pathname[0:7] == '/search':
        return [[Header.header()] + [Search.page] + Footer.footer()]
    elif pathname == '/ingresar':
        return [[Header.header()]  +Ingresar.ingresar() +Footer.footer()]
    elif pathname == '/perfil':
        return [[Header.header()]  + Footer.footer()]
    else:#if pathname == '/proyectos':
        return [[Header.header()] + index.acerca() + Footer.footer()]

@app.callback([Output('etiqueta_ingreso', 'children'),
               Output('mensaje-exito2', 'children'), 
               Output('mensaje-error2', 'children'),
               Output('mensaje-contrasena', 'children'),
               Output('input_ingreso', 'value'), 
               Output('input_ingreso', 'type'), 
               Output('input_ingreso', 'disabled')], 
               [Input('ingresar_boton', 'n_clicks')], 
               [State('input_ingreso', 'value')])
def check_id(n, ide):
    ides = ['asd', 'abd']
    
    if n:
        if ide not in ides:
            return ['ID:'], None, ['No se ha encontrado tu ID'], None, None, 'text', False
        else:
           
            return ['ID:'], ['Conectándose...'],None, None, None, 'password', False

    else: 
        raise PreventUpdate()

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

@app.callback(
    [Output('cursos','value'),Output('motivo','value'),Output('comentario_encuesta','value')],
    [Input('Confirmacion_encuesta','children')]
)
def borrar_datos(mensaje):
    if mensaje == 'Enviado con éxito, agradecemos tus comentarios':
        return ['','','']
    else:
        raise dash.exceptions.PreventUpdate()
######################################################################################### ENCUESTA
@app.callback([Output('Confirmacion_encuesta', 'children'), Output('Confirmacion_encuesta','style')],# Output('objetivo','value')],
              [Input('go_encuesta', 'n_clicks'), Input('session-stored2','data')],
                [State('cursos', 'value'),State('motivo', 'value'),State('comentario_encuesta', 'value')],
            )
def enviar(n_clicks,data, cursos, motivo, comentario):
    if n_clicks:
        if cursos and motivo and comentario:#varios cursos and args[8] !=[''] and args[8] != None: 
        
                    doc_ref = db.collection('Encuesta 2021-2').document(''.join([random.choice('qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMÑ1234567890') for _ in range(7)] ) )  
                    doc_ref.set({
                            u'cursos': cursos,
                            u'cursos': cursos,
                            u'motivo': motivo,
                            u'comentario': comentario
                    })
                    return ['Enviado con éxito, agradecemos tus comentarios',{'color':'green', 'padding':10}]#,args[6]]
        elif n_clicks >= 1:
            return ['Tienes que llenar todos los campos',{'color':'#7b1448', 'padding':10}]#,args[6]+' ']
        else:
            return ['',{'color':'#db0000', 'padding':10}]#,args[6]]
    else:
        raise dash.exceptions.PreventUpdate()


#########################################################################################
@app.callback([Output('Confirmacion', 'children'), Output('Confirmacion','style')],# Output('objetivo','value')],
              [Input('go', 'n_clicks'), Input('session-stored2','data')],
                [State('name', 'value'),State('boleta', 'value'),State('correo', 'value'),State('carrera', 'value'),State('semestre', 'value'),State('curso', 'value'),State('objetivo', 'value'),State('Accepted','value'),
                State('disponibilidad','value')],
            )
def enviar(n_clicks,data,*args,**kwargs):
    #print(args)
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
        if  len(list(args)[0]) != 0 and args[1] != '' and len(list(args)[2]) != 0  and len(list(args)[3]) != 0 and len(list(args)[5]) != 0 and len(list(args)[6]) != 0:#varios cursos and args[8] !=[''] and args[8] != None: 
            curso_tomado =  confirmar_correo(args[2], args[1])
            if curso_tomado:
                if len(curso_tomado) == 1:
                    return [f'Ya estás inscrito al curso de {curso_tomado[0]}',{'color':'#7b1448', 'padding':10}]#,args[6]]
                else:
                    cursof = ''
                    for ca in curso_tomado[:-2]:
                        cursof += ca + ', '
                    cursof+= curso_tomado[-2] + ' y '
                    cursof += curso_tomado[-1]
                    return [f'Ya estás inscrito a los cursos de {cursof}',{'color':'#7b1448', 'padding':10}]
            else:
                varios_cursos  = ''
                for curso in  args[5]:
                    varios_cursos += curso[0:2].lower()
                
                id_registro = varios_cursos + get_random_string(5)
                hora = datetime.datetime.now()
                hora = str(hora.day) + '-' + str(hora.month) + '-' + str(hora.year) + ' ' + str(hora.hour) + ':' + str(hora.minute) + ':' + str(hora.second)
                #print('ENVIADOS: ',list(args))
                if type(args[5])== str:
                    doc_ref = db.collection(args[5]).document(id_registro)
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
                else:
                    doc_ref = []
                    for curso in args[5]:
                        doc_ref = db.collection(curso).document(id_registro)
                        doc_ref.set({
                                    u'Nombre': args[0],
                                    u'Boleta': args[1],
                                    u'Correo': args[2],
                                    u'Carrera': args[3],
                                    u'Semestre': args[4],
                                    u'Curso': curso,
                                    u'Objetivo': args[6],
                                    u'Horario': args[8],
                                    u'Hora': hora,
                                    u'Id': id_registro
                                    })
                
                doc_ref = db.collection('Id-correo').document(id_registro)
                doc_ref.set({u'Correo':args[2], u'Id':id_registro,u'Cursos':args[5],u'Boleta':args[1]})
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

@app.callback([Output('name', 'value'),Output('boleta', 'value'),Output('correo', 'value'),Output('carrera', 'value'),Output('semestre', 'value'),Output('curso', 'value'), Output('objetivo','value'), Output('name', 'disabled'),Output('boleta', 'disabled'), Output('mensaje-id', 'children')],#,Output('objetivo', 'value')],
                [Input('Confirmacion', 'children'), Input('id_boton', 'n_clicks')], [State('id_anterior','value' )])
               # [State('Confirmacion', 'children')])
def borrar(mensaje, n, ide):
    #print(mensaje)
    if n:
        datos = obtener_datos(ide)
        if datos: 
            return datos[0], datos[1], datos[2],datos[3], datos[4]+1,'','', True, True,[html.P('Datos cargados con éxito.', style = {'color': '#39A051'})] 
        return '','','','',1,'','', False, False, [html.P('El ID no ha sido encontrado.', style = {'color': '#7b1448'})]
    mensaje = mensaje if type(mensaje) == str else ''
    if 'Ya estás inscrito a los cursos de' in mensaje or 'Ya estás inscrito al curso de' in mensaje or '¡Registro concluido con éxito!' in mensaje or 'Formulario enviado con éxito,' in mensaje: 
       # if n_clicks >= 1:
            return ['','','','',1,'','', False, False, []]#,'']
       # else:
        #    return ['','','','',1,'']#,'']
    else:
        raise dash.exceptions.PreventUpdate()

def obtener_datos(ide):
    dic = Datos.dic
    for dicci in dic:
        if dicci['id'] == ide:
            return dicci['Nombre'], dicci['Boleta'], dicci['Correo'],dicci[ 'Carrera'], dicci['Semestre']
    return False


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
    if True:
        return [titulo+[html.P('No aplica',style = {"color": "#8f8f8f"}),dbc.Checklist(id = 'disponibilidad',
                #options=[{'label': '  Elige un curso', 'value': 'Lun'},],
                value=[''])]]

    # elif curso == 'Python-zh':
    #     return [titulo+[dbc.Checklist(id = 'disponibilidad',options=[
    #                         {'label': '  Lun 11:00 - 12:00', 'value': 'Lun'},
    #                         {'label': u'  Mié 14:00 - 15:00', 'value': 'Mie'},
    #                         #{'label': '  Los dos', 'value': 'All'},
    #                     ],value=[''])]]
    # elif curso == 'Ingenieria-datos':
    #     return [titulo+[dbc.Checklist(id = 'disponibilidad',options=[
    #                         {'label': '  Mar 10:00 - 11:00', 'value': 'Mar10'},
    #                         {'label': u'  Mar 13:00 - 14:00', 'value': 'Mar13'},
    #                         #{'label': '  Los dos', 'value': 'All'},
    #                     ],value=[''])]]
    # elif curso == 'Pandas-ciencia':
    #     return [titulo+[dbc.Checklist(id = 'disponibilidad',options=[
    #                         {'label': '  Jue 13:00 - 14:00', 'value': 'Jue'},
    #                         {'label': u'  Vie 11:00 - 12:00', 'value': 'Vie'},
    #                         #{'label': '  Los dos', 'value': 'All'},
    #                     ],value=[''])]]
    # elif curso == 'Matlab':
    #     return [titulo+[dbc.Checklist(id = 'disponibilidad',options=[
    #                         {'label': '  Jue 14:30 - 15:30', 'value': 'Jue'},
    #                         {'label': '  Mar 14:30 - 15:30', 'value': 'Mar'},
    #                     ],value=[''])]]
    

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
    [State('url','pathname')]
)
def search_title(n,text):
    
    if '/search&q=id:' in text.lower():
        #print(text[14:])
        datos = obtener_datos(text[14:])
        if datos:
            return Convocatoria.convocatoria(), ''
            #return Convocatoria.convocatoria2(ide = text[14:], nombre = datos[0], boleta = datos[1], correo = datos[2],carrera = datos[3],semestre = datos[4]+1), ''
        else:
            return [html.H1('Error'),'El ID no ha sido encontrado.'],''
    
    if '/search' in text:
        #print(text, "dsadssd")
        if text == '/search*':
            return [html.H1('Búsqueda'), html.Div(html.Img(src = 'https://raw.githubusercontent.com/gist/T-Jedsada/dbee22959762fa6c0ccad8153830b51a/raw/8957088c2e31dba6d72ce86c615cb3c7bb7f0b0c/nyan-cat.gif', style = {'width':'300px'}), style = {'width':'350px','margin-left':'auto','margin-right':'auto'}), html.Br(), '¡Has encontrado un Easter egg! En el CdP ESFM reconocemos a los curiosos, así que no dudes en hacernos saber que eres uno.'],''
        try:
            return [[html.H1('Búsqueda'),'No existe ningún resultado para ', html.P(text[10:].replace('+',' '), style = {"font-weight":"bold", "display":"inline"})],text[10:].replace('+',' ')]
        except:
            return [html.H1('Búsqueda'),'Introduce un término y luego realiza la búsqueda'],''
    else:
        raise dash.exceptions.PreventUpdate()

@app.callback([Output('curso', 'options')], [Input('curso', 'value')])
def desabilitar_cursos(cursos):
    if 'Python-zh' in cursos:
        return [[
                                                                {'label': 'Python from zero to hero', 'value': 'Python-zh'},
                                                                {'label': 'Ingeniería de datos con Python', 'value': 'Ingenieria-datos', 'disabled': True},
                                                                #{'label': 'Pandas para ciencia de datos', 'value': 'Pandas-ciencia'},
                                                                {'label': 'MATLAB', 'value': 'Matlab'},
                                                                {'label': 'Python from Hero to God', 'value': 'Python-hg', 'disabled': True},
                                                                {'label': 'Criptografía Aplicada en C++', 'value': 'Criptografia'},
                                                                {'label': 'Wolfram Mathematica', 'value': 'Wolfram'},
                                                                #{'label': 'Machine Learning', 'value': 'Mac', 'disabled': True}
                                                            ]]
    elif 'Python-hg' in cursos or 'Ingenieria-datos' in cursos: 
        return [[
                                                                {'label': 'Python from zero to hero', 'value': 'Python-zh', 'disabled': True},
                                                                {'label': 'Ingeniería de datos con Python', 'value': 'Ingenieria-datos'},
                                                                #{'label': 'Pandas para ciencia de datos', 'value': 'Pandas-ciencia'},
                                                                {'label': 'MATLAB', 'value': 'Matlab'},
                                                                {'label': 'Python from Hero to God', 'value': 'Python-hg'},
                                                                {'label': 'Criptografía Aplicada en C++', 'value': 'Criptografia'},
                                                                {'label': 'Wolfram Mathematica', 'value': 'Wolfram'},
                                                                #{'label': 'Machine Learning', 'value': 'Mac', 'disabled': True}
                                                            ]]
    else: 
        return [[
                                                                {'label': 'Python from zero to hero', 'value': 'Python-zh'},
                                                                {'label': 'Ingeniería de datos con Python', 'value': 'Ingenieria-datos'},
                                                                #{'label': 'Pandas para ciencia de datos', 'value': 'Pandas-ciencia'},
                                                                {'label': 'MATLAB', 'value': 'Matlab'},
                                                                {'label': 'Python from Hero to God', 'value': 'Python-hg'},
                                                                {'label': 'Criptografía Aplicada en C++', 'value': 'Criptografia'},
                                                                {'label': 'Wolfram Mathematica', 'value': 'Wolfram'},
                                                                #{'label': 'Machine Learning', 'value': 'Mac', 'disabled': True}
                                                            ]]
if __name__ == '__main__':
    
    app.run_server(debug = True)#, host = '192.168.0.7')

