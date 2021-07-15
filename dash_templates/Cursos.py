import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import requests
from secret import apikeys
from config import periodo
def cursos(app):
        def toggle_modal(n1, n2, is_open):
            if n1 or n2:
                return not is_open
            return is_open

        #################### API    
        dato = {'ruta':'cdp', 
                'args':{
                        'datos': 'cursos', 
                        'periodo': periodo.periodo_actual,
                        },
                'metodo':requests.get
                }
        
        cursos = dato['metodo'](apikeys.url + f'{dato["ruta"]}/{apikeys.key}', dato['args'] ).json()['datos']
        contenidos = []
        cursos_nombre = []
        for idx,curso in enumerate(cursos):
            cursos_nombre.append(curso['nombre'])
            contenidos.append(
                dbc.Card([dbc.CardImg(src=curso['img_lg'], top=True),
                            dbc.CardBody(
                                [html.H5(curso['nombre'], className="card-title"),
                                    html.P(
                                        curso['descripcion'],
                                        className="card-text", style = {'text-align':'justify'}
                                    ),
                                    dbc.Button("Ver temario", color="danger", id = f"t{curso['nombre'].lower()[0:3]}{idx}"),
                                ]
                            )
                        ], inverse=True, style = {'background-image':f'linear-gradient(0deg, {curso["color_primario"]}, {curso["color_secundario"]})', 
                                                    'color':curso['color_letra']}) 
            )
            
            contenidos.append(
                dbc.Modal([dbc.ModalHeader(curso['nombre']),
                                dbc.ModalBody([
                                    html.P("Temario:  "),
                                    html.Ul([
                                                html.Li(tema) for tema in curso['temario']                    
                                            ])
                                ], style = {'background-image':f'linear-gradient(0deg, {curso["color_primario"]}, {curso["color_secundario"]})', 
                                            'color':curso['color_letra']}),
                                dbc.ModalFooter(
                                    dbc.Button("Cerrar", id=f"close-{curso['nombre'].lower()[0:3]}{idx}", color = "danger")
                                ),
                            ],
                            id=f"modal-{curso['nombre'].lower()[0:3]}{idx}",
                            size="lg",
                            centered = True
                        ),
            )
            if not app.callback_modal:
                app.callback(
                            Output(f"modal-{curso['nombre'].lower()[0:3]}{idx}", "is_open"),
                            [Input(f"t{curso['nombre'].lower()[0:3]}{idx}", "n_clicks"),
                            Input(f"close-{curso['nombre'].lower()[0:3]}{idx}", "n_clicks")],
                            [State(f"modal-{curso['nombre'].lower()[0:3]}{idx}", "is_open")],
                )(toggle_modal)   
        #################### 
        app.callback_modal = True
        return  [html.Div([
                        html.H1("Conoce todos nuestros cursos", className="display-3" , style ={"font-size":"3rem"} ),
                        html.P(
                            "No es necesario tener conocimientos sobre los cursos, pero algunos sí requieren conocimientos previos. ",
                            className="lead",
                        ),
                        html.P(
                        "En el CdP ESFM impartimos los siguientes cursos 100% gratuitos:",
                        ),
                        dbc.Row([
                                dbc.Col(html.Li(curso),width="auto") for curso in cursos_nombre
                        ]),
                    ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5}),
                dbc.CardColumns(contenidos, style = {"padding":"30px", "padding-top":20})
                ]