import dash_bootstrap_components as dbc
import dash_html_components as html
import requests
from secret import apikeys
from config import periodo


def certificado(token):
    dato = {'ruta':'cdp', 
                'args':{
                        'datos': 'constancia', 
                        'periodo': periodo.periodo_actual,
                        'token': token,
                        },
                'metodo':requests.get
                }
        
    response_constancia = dato['metodo'](apikeys.url + f'{dato["ruta"]}/{apikeys.key}', dato['args'] )
    if response_constancia.status_code ==200:
        constancia = response_constancia.json()['datos']
    else:
        return [html.Div([html.H3("No se ha encontrado la constancia", className="display-4", style ={"text-align":"left"} ),
                html.P(
                                    "Ponte en contácto con nosotros si crees que es un error",
                                    className="lead", style ={"text-align":"left", "padding-bottom":100}
                                )], style = {"padding":20})]
    
    return [html.Div([
                    dbc.Row([
                            dbc.Col([
                                html.Img(src=constancia['archivo'], style = {"width":"100%","margin-left":"auto", "padding-bottom":30 }),
                                
                            ],md=6 ),
                            dbc.Col([
                                html.H3(constancia["curso"], className="display-4", style ={"text-align":"left"} ),
                                html.P(
                                    constancia['fecha'],
                                    className="lead", style ={"text-align":"left"}
                                ),
                                html.P(
                                    "Cursado por " + constancia["alumno"],
                                    className="lead", style ={"text-align":"left", "color":"black"}
                                ),
                                
                                html.P(
                                    constancia["alumno"].capitalize().split(' ')[0] + """ realizó las actividades y adquirió los conocimientos necesarios para poder concluir satisfactoriamente el curso de """ + constancia["curso"] + """, demostrando las habilidades mediante retos precisos que verifican su correcto aprendizaje.""", 
                                    style ={"text-align":"justify", "text-justify": "inter-word"}
                                )
                            ], md=6, style = {"text-align":"justify"}),
                            
                        ])
                     
                    ],
            style = {"padding":"20px", "padding-top":20, "padding-bottom":5})
            ]

def cursos(boleta):
    
    dato = {'ruta':'cdp', 
                'args':{
                        'datos': 'constancias', 
                        'periodo': periodo.periodo_actual,
                        'boleta': boleta,
                        },
                'metodo':requests.get
                }
        
    response_constancias = dato['metodo'](apikeys.url + f'{dato["ruta"]}/{apikeys.key}', dato['args'] )
    if response_constancias.status_code ==200:
        json_response = response_constancias.json()
        constancias = json_response['datos']
        nombre = json_response['nombre']
    else:
        return [html.Div([html.H3("No se ha encontrado datos con la boleta indicada", className="display-4", style ={"text-align":"left"} ),
                html.P(
                                    "Ponte en contácto con nosotros si crees que es un error",
                                    className="lead", style ={"text-align":"left", "padding-bottom":100}
                                )], style = {"padding":20})]

    card_contents = [dbc.CardBody(
            [
                html.Blockquote(
                    [
                        dbc.CardImg(src=constancia["archivo"], top=True, style = {"width":"100%"}),
                        html.P(
                            constancia['curso'], style = {"text-align":"center"}
                        ),
                        html.Footer(
                           [ html.Small(f"Periodo {constancia['periodo']}", style = {"padding-right":20}),
                            
                           ]
                        ),
                        html.Small("Enlaces para compartir: ", style = {"color":"white"}),
                        html.Br(),
                        html.A( "https://cdp.esfm-x.com/constancia/"+ constancia['token'], 
                                    href = "https://cdp.esfm-x.com/constancia/"+ constancia['token'], 
                                    style = { "font-size":"0.77em",  "color": "#f9aa3a", "word-wrap": "break-word"}
                        ),
                        html.Br(),
                        html.Div([
                            dbc.Button("LinkedIn", color="link", href = "https://www.linkedin.com/profile/add?startTask=CERTIFICATION_NAME&name="+ constancia['curso'].replace(" ", "%20") + "&organizationId=72339480&issueYear="+ str(constancia["periodo"])[:-2] + "&issueMonth="+ (constancia["periodo"][-1] if constancia["periodo"][-1] != "2" else "7") + "&certUrl=https://cdp.esfm-x.com/constancia/"+constancia['token'] + "&certId="+ constancia['token']    + "&credentialDoesNotExpire=1" , style = { "color": "#f9aa3a"}, target = "_blank" ),
                            dbc.Button("Facebook", color="link", href = "https://www.facebook.com/sharer/sharer.php?u=" +"https://cdp.esfm-x.com/constancia/"+ constancia['token'] , style = { "color": "#f9aa3a"}, target = "_blank"  ),
                            dbc.Button("Twitter", color="link", href = "https://twitter.com/intent/tweet/?hashtags=CdPESFM&text=" + "https://cdp.esfm-x.com/constancia/"+  constancia['token'] , style = { "color": "#f9aa3a"}, target = "_blank"  )
                        ],style = {"text-align":"center"}),
                    ],
                    className="blockquote"
                )
            ]
        )for constancia in constancias]

    return [html.Div([html.H1("Visualiza tus constancias", className="display-3" , style ={"font-size":"3rem"} ),
                                        html.P(
                                            nombre,
                                            className="lead",
                                        ),
                                        html.P(
                                            nombre.capitalize().split(' ')[0] + ", has participado en las actividades del club completando los siguientes cursos/talleres:",
                                        ),

                    dbc.CardColumns([ dbc.Card(card_content, color="danger", inverse=True) for card_content in card_contents]),

                    html.P("*Recuerda que no debes compartir el enlace de esta página")
                    
                    ],
            style = {"padding":"20px", "padding-top":20, "padding-bottom":5, "width":"100%"})
    ]   