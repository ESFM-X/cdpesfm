import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import colors
 

def encuesta_satis():
    margen = 25
    color_letra = '#000'#'#061d47'
    color_footer = '#8f8f8f'
    color_fondo = '#ffffff'
    width_input = 300
    
    return [html.Div([
                                            html.H1("Encuesta 2021-2", className="display-3" , style ={"font-size":"3rem", "color":color_letra}, ),
                                            html.P(
                                                ["En el CdP ESFM estamos comprometidos en mejorar nuestros cursos y hacer que más personas sean parte de la comunidad satisfaciendo sus expectativas. Si te inscribiste en algún curso del semestre 2021-2 y",html.B(" no lo pudiste concluir"),", favor de llenar el siguiente formulario."],style = {"color":color_letra},
                                                className="lead",
                                            ),
                                        
                                            html.Div(
                                            children =[ 
                                                    
                                                        html.P('El formulario es totalmente anónimo', style = {'color':"#7b1448",'margin-top':10}),
                                                dbc.Row([
                                                    
                                                    dbc.Col([
                                                        
                                                        html.H6('Elige los cursos que inscribiste y no terminaste:', style = {'margin-top':margen,'color':color_letra}),
                                                        dcc.Dropdown(id = 'cursos',
                                                            options=[
                                                                {'label': 'Python from Zero to Hero', 'value': 'Python-zh'},
                                                                {'label': 'Ingeniería de Datos con Python', 'value': 'Ingenieria-datos'},
                                                                #{'label': 'Pandas para ciencia de datos', 'value': 'Pandas-ciencia'},
                                                                {'label': 'MATLAB', 'value': 'Matlab'},
                                                                {'label': 'Python from Hero to God', 'value': 'Python-hg'},
                                                                {'label': 'Criptografía Aplicada en C++', 'value': 'Criptografia'},
                                                                {'label': 'Wolfram Mathematica', 'value': 'Wolfram'},
                                                                #{'label': 'Machine Learning', 'value': 'Mac', 'disabled': True}
                                                            ],
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
                                                        html.H6('Elige el motivo que más te acomode:', style = {'margin-top':margen,'color':color_letra}),

                                                        dcc.Dropdown(id = 'motivo',
                                                            options=[
                                                                {'label': 'No pude organizar mi tiempo', 'value': 'Tiempo'},
                                                                {'label': 'No me agradó el temario', 'value': 'Temario'},
                                                                {'label': 'Tuve algún conflicto de aprendizaje', 'value': 'Conflicto de aprendizaje'},
                                                                {'label':'Otra', 'value':'Otro'}
                                                            
                                                            ],
                                                            value='',
                                                            multi = False, 
                                                            searchable = False,
                                                            clearable = False,
                                                            style = {
                                                                'width': width_input,
                                                                'margin-left':'auto',
                                                                'margin-right':'auto'
                                                            }, placeholder = 'Motivo'
                                                        ),
                                                        html.H6('(Opcional) Escribe algún comentario: ', style = {'margin-top':margen,'color':color_letra}),
                                                        #dcc.Input(id = 'objetivo',value='', type='text', style ={'width':'auto','width': 300, 'height':100}),
                                                        dbc.Textarea( id = 'comentario_encuesta',
                                                            placeholder='Escribenos comentarios, opiniones y recomendaciones para entregas futuras',
                                                            value='',
                                                            style ={'width':'auto','width': width_input, 'height':100, 'margin-left':'auto','margin-right':'auto'}
                                                        )
                                                    ], lg = 4,),
                                                    
                                                ], justify="center")
                                                ],
                                                style = {'width':'100%','margin-left':'auto','margin-right':'auto', 'text-align': 'center'}
                                            
                                            ),
                                            html.Div(children = [
                                                dcc.Loading(
                                                        id="loading-1",
                                                        type="default",
                                                        children=html.P(id='Confirmacion_encuesta'),#, style = {'color':'#db0000', 'padding':10}
                                                        color = '#7b1448'
                                                    )
                                            ],style = {'margin-left':'auto','margin-right':'auto', 'text-align': 'center', 'margin-top':20}),
                                            html.Div(children = [ 
                                                        dcc.Link( id = 'go_link', children = [
                                                            dbc.Button("Enviar", id='go_encuesta', n_clicks=0, color="danger", className="mr-1")
                                                        ], href = '')
                                                ],
                                                style = {'width':'auto','margin-left':'auto','margin-right':'auto', 'text-align': 'center', 'margin-top':margen, "margin-bottom":30}
                                                ),
                                            
                                           
                                        ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5, "background-color":color_fondo}),
                                        
                                        
            ]