import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import colors



def acerca():

    return [dbc.Jumbotron(
        [   
            html.Img(src = "https://fotos.subefotos.com/bd8cab011c4c316e1ea0e74f2aed492eo.png",#"https://fotos.subefotos.com/5a7f422ce2c2cc675934b38b137a547fo.png",
                    style = {"width":"100%"}),
            html.Div([
                html.H1("Únete a la comunidad", className="display-3", style ={"font-size":"3rem"} ),
                html.P(
                    "De ESFM para esfemitas ",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                
                html.P(
                    """
                        Una de nuestras intenciones es crear una comunidad en la que todos se sientan libres de compartir sus experiencias y hacer relaciones nuevas en tiempos de cuarentena,
                        a continuación te proporcionamos la dirección al servidor de Discord, en donde podrás encontrar material de cursos pasados, hacer reseñas de profesores, ver películas 
                        en llamada con la comunidad y hasta conocer jugadores de tu videojuego favorito. 

                    """, style = {"text-align":"justify"}
                ),
                html.P(html.A(dbc.Button("Únete a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
            ], style = {"padding-left":0})
        ], style = {"padding":20, "background-color":"#343a40", "color":"#CBCBCB"}
    ),
    dbc.Jumbotron(
        [   
            html.Div([
                html.H3("¿Qué es el CdP ESFM?", className="display-3"),#, style ={"font-size":"2rem"} ),
                html.P(
                    className="lead",
                ),
                html.Hr(className="my-2"),
                dbc.Row(
                    [
                        dbc.Col([
                                html.P(
                                        """El Club de Programación ESFM (CdP ESFM), ubicado en el Aula Siglo XXI del edificio 9, IPN Unidad Zacatenco, está formado por y para alumnos de la Escuela Superior de Física y Matemáticas que comparten un interés por la programación, el análisis de datos y el cómputo científico.""",
                                        
                                    ),
                                    html.P(
                                        """
                                            Nuestro objetivo principal es que desarrolles la habilidad de pasar de las mates a la programación, logrando aplicaciones relevantes dentro y fuera de la comunidad. La dinámica de nuestros cursos se basa en dar lecturas didácticas cada semana y dejando actividades, retos y misiones que ayudarán a reforzar los temas.

                                        """, style = {"text-align":"justify"}
                                    ),
                                    html.P(
                                        "¡Toda nuestra comunidad es bienvenida!",
                                        
                                    ),
                                    
                                ], md= 8#, xl = 9
                        ),
                        dbc.Col([
                                html.Img(src="https://fotos.subefotos.com/69f56b49685599ad2bc8377462bfeb6fo.jpg", style = {"width":"100%","margin-left":"auto" }) 
                        ], md = 4#, xl = 3

                        )
                    ], form = True
                )
                
                
                #html.P(html.A(dbc.Button("Unéte a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
            ], style = {"padding-left":5})
        ], style = {"padding":20, "background-color":"white", "color":"#3F3F3F", "margin-bottom":0}
    ),
    dbc.Jumbotron(
        [   
            html.Div([
                html.H3("Nuestros cursos", className="display-3", style ={"text-align":"right"} ),
                html.P(
                    "Cursos 100% en línea",
                    className="lead", style ={"text-align":"right"}
                ),
                html.Hr(className="my-2"),
                dbc.Row([
                            dbc.Col([
                                html.Img(src="https://fotos.subefotos.com/98e19371bee1fc70e3a4cef70db67df1o.jpg", style = {"width":"100%","margin-left":"auto", "padding-bottom":30 }),
                                
                            ],md=4 ),
                            dbc.Col([
                                html.P(
                                    """Todas las sesiones se imparten en Discord, aplicación que podrás utilizar desde tu navegador sin necesidad de descarga. En caso de que no puedas asistir a alguna clase, esta será transtimida permitiéndote revisarla después. 
                                        """, 
                                    style ={"text-align":"justify", "text-justify": "inter-word"}
                                ),
                                html.P(
                                    "Además, con esta plataforma podrás relacionarte con personas que puedan ayudarte a enriquecer tus conocimientos y que compartan el mismo interés en aprender. ",
                                    style ={"text-align":"justify", "text-justify": "inter-word"}
                                ),
                            ], md=8, style = {"text-align":"justify"}),
                            
                        ])
                #html.P(html.A(dbc.Button("Unéte a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
            ], style = {"padding-right":5})
        ], style = {"padding":20, "background-color":"#F6F6F6", "color":"#3F3F3F"}
    ),
    html.Div([
    dbc.Jumbotron(
        [   
            html.Div([
                html.H1("Alumnos destacados", className="display-3", style ={"margin-left":"auto"} ),
                html.P(
                    "Semestre 2021-1",
                    className="lead"
                ),
                html.Hr(className="my-2"),
                html.P(
                    "En cada curso tenemos estudiantes que muestran su compromiso y pasión desde la primera sesión, el CdP ESFM los reconoce presentándolos a continuación. " 
                ),
                #html.P(html.A(dbc.Button("Unéte a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
            dbc.Row([    
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://scontent-qro1-2.xx.fbcdn.net/v/t1.0-9/84334500_3354175324656855_3738219206634635264_o.jpg?_nc_cat=103&ccb=3&_nc_sid=174925&_nc_ohc=3eI6GvyuZ3IAX9W9SPa&_nc_ht=scontent-qro1-2.xx&oh=d31a2101d330f59baefa033d628c2c5a&oe=6050BD82", style = {'width':'100%',"padding-bottom":"20px"}),
                                    html.H4("Juan F. Martínez ", className="card-title"),
                                    html.H6("Python from Zero to Hero", className="card-subtitle"),
                                    html.P(
                                    #    "Su gran pasión por la programación lo impulso a terminar el curso de manera sobresaliente. ",
                                       # "Al chile si tiene buen gusto de rolitas.",
                                        className="card-text",
                                    ),
                                    dbc.CardLink("Github", href="https://github.com/juantonio-martinez",target='_blank'),
                                    dbc.CardLink("Discord", href="https://discordapp.com/users/490942535858913281",target='_blank'),
                                ]
                            ),
                            style={"width": "100%"},
                        ), lg = 3, md = 4, style = {"padding":"10px", "padding-top":0}
                ),
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://fotos.subefotos.com/793d2d132fcd7f15d7ab184c14135800o.jpg", style = {'width':'100%',"padding-bottom":"20px"}),
                                    html.H4("Sara I. López", className="card-title"),
                                    html.H6("Python from Zero to Hero", className="card-subtitle"),
                                    html.P(
                                    #    "Destacada por su asistencia, investigación, compromiso y hacer un proyecto final sobresaliente usando buenas prácticas. ",
                                        #Al chile si tiene buen gusto de rolitas.",
                                        className="card-text",
                                    ),
                                    #dbc.CardLink("Github", href="#"),
                                    dbc.CardLink("Discord", href="https://discordapp.com/users/762705945704136705",target='_blank'),
                                ]
                            ),
                            style={"width": "100%"},
                        ),lg = 3, md = 4, style = {"padding":"10px", "padding-top":0},
                    
                ),
                
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://fotos.subefotos.com/728dc97fe209707bc1a306ae593b79d9o.jpg", style = {'width':'100%',"padding-bottom":"20px"}),
                                    html.H4("Antonio E. Vargas", className="card-title"),
                                    html.H6("Ingeniería de Datos | Pandas para Ciencia de Datos", className="card-subtitle"),
                                    html.P(
                                    #    "Tuvo un gran desempeño entregando las actividades y retos logrando una asistencia perfecta. ",
                                        
                                        className="card-text",
                                    ),
                                    #dbc.CardLink("Github", href="#"),
                                    dbc.CardLink("Discord", href="https://discordapp.com/users/761436083392610335",target='_blank'),
                                ]
                            ),
                            style={"width": "100%"},
                        ),lg = 3, md = 4, style = {"padding":"10px", "padding-top":0}
                ),
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://fotos.subefotos.com/e7831a11c32c4b3d46d27e61098e0b31o.png", style = {'width':'100%',"padding-bottom":"20px"}),
                                    html.H4("Miriam R. Castelán", className="card-title"),
                                    html.H6("Python from Zero to Hero", className="card-subtitle"),
                                    html.P(
                                    #    "Asistió a todas las clases. ",
                                        
                                        className="card-text",
                                    ),
                                   # dbc.CardLink("Github", href="#"),
                                    dbc.CardLink("Discord", href="https://discordapp.com/users/754879239836401695",target='_blank'),
                                ]
                            ),
                            style={"width": "100%"},
                        ),lg = 3, md = 4, style = {"padding":"10px", "padding-top":0}
                ),
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://fotos.subefotos.com/8b856c930a58e2ad4d4c54d09b28c698o.jpg", style = {'width':'100%',"padding-bottom":"20px"}),
                                    html.H4("Rodrigo T. Castillo", className="card-title"),
                                    html.H6("Ingeniería de Datos", className="card-subtitle"),
                                    html.P(
                                     #   "Asistió a todas las clases. ",
                                        
                                        className="card-text",
                                    ),
                                    #dbc.CardLink("Github", href="#"),
                                    dbc.CardLink("Discord", href="https://discordapp.com/users/756607551897862255",target='_blank'),
                                ]
                            ),
                            style={"width": "100%"},
                        ),lg = 3, md = 4, style = {"padding":"10px", "padding-top":0}
                ),
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://fotos.subefotos.com/df21b0acdb6dd39c91c7f23f386c4467o.png", style = {'width':'100%',"padding-bottom":"20px"}),
                                    html.H4("Eduardo G. Cazares", className="card-title"),
                                    html.H6("Ingeniería de Datos", className="card-subtitle"),
                                    html.P(
                                    #    "Asistió a todas las clases. ",
                                        
                                        className="card-text",
                                    ),
                                    dbc.CardLink("Github", href="https://github.com/Cuadernin", target = '_blank'),
                                    dbc.CardLink("Discord", href="https://discordapp.com/users/533539803854274561",target='_blank'),
                                ]
                            ),
                            style={"width": "100%"},
                        ),lg = 3, md = 4, style = {"padding":"10px", "padding-top":0}
                ),
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://fotos.subefotos.com/a3afe547c4346dfd48e7377e50f02354o.jpg", style = {'width':'100%',"padding-bottom":"20px"}),
                                    html.H4("Eric O. Pardo", className="card-title"),
                                    html.H6("Pandas para Ciencia de Datos   ", className="card-subtitle"),
                                    html.P(
                                    #    "Asistió a todas las clases. ",
                                        
                                        className="card-text",
                                    ),
                                    #dbc.CardLink("Github", href="#"),
                                    dbc.CardLink("Discord", href="https://discordapp.com/users/756320972986122352",target='_blank'),
                                ]
                            ),
                            style={"width": "100%"},
                        ),lg = 3, md = 4, style = {"padding":"10px", "padding-top":0}
                ),
            ],justify="center",style = {'margin':30})
            ], style = {"padding-left":5, "text-justify": "inter-word"})
        ], style = {"padding":20, "background-color":"white", "color":"#3F3F3F"}
    ),
    ], style = {'margin':30})
    ]