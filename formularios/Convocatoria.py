import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from secret import apikeys
from config import periodo
import requests

def convocatoria_expired():
    return [html.Div([
                html.H1(f"Convocatoria {periodo.periodo_actual}", className="display-3" , style ={"font-size":"3rem"} ),
                html.P("El tiempo de registro ha terminado",className="lead"),
                html.P("Iniciamos los cursos a partir del 1 de marzo en el día indicado. "),
                                       
            ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5}),
                                       
        ]
def convocatoria(ide = None):
    margen = 25
    color_letra = '#000'
    color_footer = '#8f8f8f'
    color_fondo = '#ffffff'
    width_input = 300
    #################### API
    imagenes_cursos = []
    dropdown_values_cursos = []
    dato = {'ruta':'cdp', 
                'args':{
                        'datos': 'cursos', 
                        'periodo': periodo.periodo_actual,
                        },
                'metodo':requests.get
                }
        
    cursos = dato['metodo'](apikeys.url + f'{dato["ruta"]}/{apikeys.key}', dato['args'] ).json()['datos']
    for curso in cursos:
        imagenes_cursos.append( 
            dbc.Col(html.Img (src= curso['img_md'] , 
                                style = {'width':'100%'}), lg = 3, md = 4, sm = 5, xs = 6)
        )
        dropdown_values_cursos.append(
            {'label': curso['nombre'], 'value': str(curso['id']), 'disabled':False if curso['cupo'] else True}
        )
    ####################
    if not ide:
        return [
            html.Div([
                html.H1(f"Convocatoria {periodo.periodo_actual}", className="display-3" , style ={"font-size":"3rem", "color":color_letra}, ),
                html.P(
                    "Llena el siguiente formulario y espera una confirmación por e-mail. Iniciamos el 1 de marzo.",
                    style = {"color":color_letra}, className="lead",
                ),
                dbc.Row(imagenes_cursos, justify = 'center'),
                html.Div([ 
                    html.H6('Si has tomado cursos con nosotros ingresa tu boleta', style = {'margin-top':margen,'color':color_letra}),
                    html.Div([
                            dbc.Row([
                            dbc.Col([
                                dbc.Input(id = 'id_anterior',value='', type='number', style ={'width':'100%', 'margin-left':'auto','margin-right':'auto'},
                                         placeholder = 'Boleta'),
                            ], width = 10),
                            dbc.Col([
                                dbc.Button('Ir', id = "id_boton")
                            ], width = 2)
                        ], no_gutters=True,),
                    ], style = {'width':300, 'margin-left':'auto','margin-right':'auto'}),

                    html.Div(id = 'mensaje-id'),

                   
                    dbc.Row([
                        dbc.Col([
                            
                            html.H6('Ingresa tu nombre completo: ', style = {'margin-top':margen,'color':color_letra}),
                            dbc.Input(id = 'name',value='', type='text', style ={'width':width_input, 'margin-left':'auto','margin-right':'auto'}, placeholder = 'Empieza por tus nombres'),
                            
                            html.H6('Ingresa tu número de boleta: ', style = {'margin-top':margen,'color':color_letra}),
                            dbc.Input(id = 'boleta',value='', type='number', style ={'width': width_input, 'margin-left':'auto','margin-right':'auto'}),

                            html.H6('Ingresa tu correo institucional: ', style = {'margin-top':margen,'color':color_letra}),
                            dbc.Input(id = 'correo',value='', type='email', style ={'width': width_input, 'margin-left':'auto','margin-right':'auto'}, placeholder = 'nombre@alumno.ipn.mx'),
                            html.P('Si aún no tienes correo institucional ingresa otro correo.', style = {'color':color_footer,'margin-top':10}),
                        ], lg = 4),
                        dbc.Col([
                            html.H6('Elige tu carrera:', style = {'margin-top':margen,'color':color_letra}),

                            dcc.Dropdown(id = 'carrera',
                                options=[
                                    {'label': 'Lic. en Matemática Algorítmica', 'value': 'Mat'},
                                    {'label': 'Lic. en Física y Matemáticas', 'value': 'Lic'},
                                    {'label': 'Ingeniería Matemática', 'value': 'Ing'},
                                    {'label':'Otra', 'value':'Otr'}
                                
                                ],
                                value='',
                                multi = False, 
                                searchable = False,
                                clearable = False,
                                style = {
                                    'width': width_input,
                                    'margin-left':'auto',
                                    'margin-right':'auto'
                                }, placeholder = 'Carreras'
                            ),
                            html.H6('Elige tu semestre:', style = {'margin-top':margen,'color':color_letra}),
                            html.Div( children = [
                                                    dcc.Slider(id = 'semestre',
                                                        min=0,
                                                        max=9,
                                                        marks={i: '{}+'.format(i) if i == 9 else str(i) for i in range(0, 9)},
                                                        value=0
                                                        
                                                    )],
                                    style = {'width':width_input, 'margin-left':'auto', 'margin-right':'auto'}
                            ),
                            html.P('Selecciona el número de semestres que has cursado.', style = {'color':color_footer,'margin-top':10}),
                            
                            html.H6('Elige los cursos a inscribir:', style = {'margin-top':margen,'color':color_letra}),
                            dcc.Dropdown(id = 'curso',
                                options=dropdown_values_cursos,
                                value='',
                                multi = True, 
                                searchable = False,
                                clearable = False,
                                style = {
                                    'width': width_input,
                                    'margin-left':'auto',
                                    'margin-right':'auto'
                                }, placeholder = 'Cursos'
                            ),
                        
                            html.Div(id = 'elegir_horario'),
                            
                            html.Div(id = 'Python_accept', children = [dbc.Checklist(id = 'Accepted')]),
                        ], lg = 4),
                        dbc.Col([
                            html.Div(id = 'elegir_horario', style = {'margin-top':margen,'color':color_letra}),
                            html.H6('Escribe tus objetivos en el curso: ', style = {'margin-top':margen,'color':color_letra}),
                            dbc.Textarea( id = 'objetivo',
                                placeholder='Se considerará si se excede el límite de cupo',
                                value='',
                                style ={'width':'auto','width': width_input, 'height':100, 'margin-left':'auto','margin-right':'auto'}
                            ),
                        ], lg = 4)  
                    ])
                ], style = {'width':'100%','margin-left':'auto','margin-right':'auto', 'text-align': 'center'}),

                html.Div(children = [
                    dcc.Loading(
                            id="loading-1",
                            type="default",
                            children=html.P(id='Confirmacion'),
                            color = '#7b1448'
                        )
                ],style = {'margin-left':'auto','margin-right':'auto', 'text-align': 'center', 'margin-top':20}),
                html.Div(children = [ 
                            dcc.Link( id = 'go_link', children = [
                                dbc.Button("Enviar", id='go', n_clicks=0, color="danger", className="mr-1")
                            ], href = '')
                    ],
                    style = {'width':'auto','margin-left':'auto','margin-right':'auto', 'text-align': 'center', 'margin-top':margen}
                    ),
                
                html.Div(children = [
                    html.Footer(children = [ 
                        '*Al enviar tus datos aceptas su uso para confirmar su veracidad.',
                    ],style = {'margin-left':'auto','margin-right':'auto', 'text-align': 'center','padding-bottom':20,'color':color_footer} ),
                            
                ], style = {'margin-top': 25})
                    
            ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5, "background-color":color_fondo}),                        
        ]