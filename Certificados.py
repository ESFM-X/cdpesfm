import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import ides2021
imagenes = ides2021.images() 
# {"in1ui2w0":{"url":"https://fotos.subefotos.com/a5dad493c6f317756745afd664e5bff1o.png",
#                         "curso":"Taller de Ingeniería de Datos",
#                         "Fecha": "20 de marzo del 2021",
#                         "Nombre": "Rodolfo Carlos Lagunas  Jardines"
#                         },
#             "ineids20":{"url":"https://fotos.subefotos.com/3a9322d21dd18c53a1b76747925cf4e2o.png",
#                         "curso":"Taller de Ingeniería de Datos",
#                         "Fecha": "Enero del 2021",
#                         "Nombre": "Antonio Elias Vargas",
#                         },
#             "ineids21":{"url":"https://fotos.subefotos.com/27736987a9028e2b57ed5281f339e449o.png",
#                         "curso":"Taller de Pandas para Ciencia de Datos",
#                         "Fecha": "20 de marzo del 2021",
#                         "Nombre": "Antonio Elias Vargas"
#                         }}

def certificado(datos):
    if datos not in imagenes:
        return [html.Div([html.H3("No se ha encontrado la constancia", className="display-4", style ={"text-align":"left"} ),
                html.P(
                                    "Ponte en contácto con nosotros si crees que es un error",
                                    className="lead", style ={"text-align":"left", "padding-bottom":100}
                                )], style = {"padding":20})]
    return [html.Div([
                    dbc.Row([
                            dbc.Col([
                                html.Img(src=imagenes[datos]["url"], style = {"width":"100%","margin-left":"auto", "padding-bottom":30 }),
                                
                            ],md=6 ),
                            dbc.Col([
                                html.H3(imagenes[datos]["curso"], className="display-4", style ={"text-align":"left"} ),
                                html.P(
                                    imagenes[datos]["Fecha"],
                                    className="lead", style ={"text-align":"left"}
                                ),
                                html.P(
                                    "Cursado por " + imagenes[datos]["Nombre"],
                                    className="lead", style ={"text-align":"left", "color":"black"}
                                ),
                                
                                html.P(
                                    imagenes[datos]["Nombre"].capitalize().split(' ')[0] + """ realizó las actividades y adquirió los conocimientos necesarios para poder concluir satisfactoriamente del """ + imagenes[datos]["curso"] + """, demostrando las habilidades mediante retos precisos que verifican su correcto aprendizaje.""", 
                                    style ={"text-align":"justify", "text-justify": "inter-word"}
                                )
                            ], md=6, style = {"text-align":"justify"}),
                            
                        ])
                     
                    ],
            style = {"padding":"20px", "padding-top":20, "padding-bottom":5})
            ]
def cursos(datos):
    url = "https://www.linkedin.com/profile/add?startTask=CERTIFICATION_NAME&name=Experta%en%Patita&organizationId=72339480&issueYear=2020&issueMonth=8&certUrl=http://www.cdpesfm.college/&certId=123dsad&credentialDoesNotExpire=1"
    card_contents = [dbc.CardBody(
            [
                html.Blockquote(
                    [
                        dbc.CardImg(src=imagenes[datos["Id"] + str(indice)]["url"], top=True, style = {"width":"100%"}),
                        html.P(
                            curso[:], style = {"text-align":"center"}
                        ),
                        html.Footer(
                           [ html.Small("Período " + "2021-1", style = {"padding-right":20}),# className="text-muted")
                            #dbc.Button("Ver", color="danger", href = "/constancia/" + datos["Id"] + str(indice)  ),
                           ]
                        ),
                        html.Small("Enlaces para compartir: ", style = {"color":"white"}),
                        html.Br(),
                        dbc.Button( "http://www.cdpesfm.college/constancia/"+ datos["Id"] + str(indice), href = "http://www.cdpesfm.college/constancia/"+ datos["Id"] + str(indice),  color="link", style = { "font-size":"0.77em",  "color": "#f9aa3a"}),
                        html.Br(),
                        html.Div([
                            dbc.Button("LinkedIn", color="link", href = "https://www.linkedin.com/profile/add?startTask=CERTIFICATION_NAME&name="+ curso.replace(" ", "%20") + "&organizationId=72339480&issueYear="+ str(datos["Periodo"])[:-1] + "&issueMonth="+ (str(datos["Periodo"])[-1] if str(datos["Periodo"])[-1] != "2" else "7") + "&certUrl=http://www.cdpesfm.college/constancia/"+ datos["Id"] + str(indice)  + "&certId="+ datos["Id"] + str(indice)   + "&credentialDoesNotExpire=1" , style = { "color": "#f9aa3a"}, target = "_blank" ),
                            dbc.Button("Facebook", color="link", href = "https://www.facebook.com/sharer/sharer.php?u=" +"http://www.cdpesfm.college/constancia/"+ datos["Id"] + str(indice) , style = { "color": "#f9aa3a"}, target = "_blank"  ),
                            dbc.Button("Twitter", color="link", href = "https://twitter.com/intent/tweet/?hashtags=CdPESFM&text=" + "http://www.cdpesfm.college/constancia/"+ datos["Id"] + str(indice)  , style = { "color": "#f9aa3a"}, target = "_blank"  )
                        ],style = {"text-align":"center"}),
                    ],
                    className="blockquote"#,style = {'text-align':'justify'}
                )
            ]
        )for indice, curso in enumerate(datos["Curso"])]
    return [html.Div([html.H1("Visualiza tus constancias", className="display-3" , style ={"font-size":"3rem"} ),
                                        html.P(
                                            datos["Nombre"],
                                            className="lead",
                                        ),
                                        html.P(
                                            datos["Nombre"].capitalize().split(' ')[0] + ", has participado en las actividades del club complentando los siguientes cursos/talleres:",
                                        ),
                    #dbc.Row([
                    dbc.CardColumns([ dbc.Card(card_content, color="danger", inverse=True) for card_content in card_contents]),
                   # ], justify="center", style = {"padding":"10px", "width":"100%"}),
                    html.P("*Recuerda que no debes compartir el enlace de esta página")
                    
                    ],
            style = {"padding":"20px", "padding-top":20, "padding-bottom":5, "width":"100%"})
    ]   