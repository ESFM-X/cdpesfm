import dash_bootstrap_components as dbc
import dash_html_components as html
from config import periodo

def acerca():

    return [dbc.Jumbotron(
        [   
            html.Img(src = "https://i.ibb.co/QmGbkxq/Logo-Ancho-Final-Negro.png",#"https://fotos.subefotos.com/5a7f422ce2c2cc675934b38b137a547fo.png",
                    style = {"width":"100%"}),
            html.Div([
                html.H1("Únete a la comunidad", className="display-3", style ={"font-size":"3rem"} ),
                html.P(
                    "De esfemitas para esfemitas ",
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
                                html.Img(src="https://i.ibb.co/1m6xSTn/9-ESFM-2.jpg", style = {"width":"100%","margin-left":"auto" }) 
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
                                html.Img(src="https://i.ibb.co/ngp0mLV/151263335-431011394788665-3824541555941416493-n-2.jpg", style = {"width":"100%","margin-left":"auto", "padding-bottom":30 }),
                                
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
                    f"Semestre {periodo.periodo_actual[0:-1]}{ '1' if periodo.periodo_actual[-1] == '2' else  '2'}",
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
                                    html.Img(src= "https://i.ibb.co/yddmYV1/imagen-2021-05-30-165715.png", style = {'width':'100%',"padding-bottom":"20px"}),
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
                        ), lg = 3, md = 4, sm=6, style = {"padding":"10px", "padding-top":0}
                ),
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://i.ibb.co/mqxpCbT/photo4996863693920774385-2.jpg", style = {'width':'100%',"padding-bottom":"20px"}),
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
                        ),lg = 3, md = 4, sm=6,style = {"padding":"10px", "padding-top":0},
                    
                ),
                
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://i.ibb.co/kh8B8DT/66398624-2261797620703860-4737014727492763648-o.jpg", style = {'width':'100%',"padding-bottom":"20px"}),
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
                        ),lg = 3, md = 4,sm=6, style = {"padding":"10px", "padding-top":0}
                ),
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://i.ibb.co/wYNjzSV/imagen-2021-05-30-165635.png", style = {'width':'100%',"padding-bottom":"20px"}),
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
                        ),lg = 3, md = 4, sm=6,style = {"padding":"10px", "padding-top":0}
                ),
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://i.ibb.co/MngVmyV/61613845-2457168924570134-8565666540718915584-o.jpg", style = {'width':'100%',"padding-bottom":"20px"}),
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
                        ),lg = 3, md = 4,sm=6, style = {"padding":"10px", "padding-top":0}
                ),
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://fotos.subefotos.com/df21b0acdb6dd39c91c7f23f386c4467o.png", alt="Avatar de Eduardo G.",  style = {'width':'100%',"padding-bottom":"20px"}),
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
                        ),lg = 3, md = 4, sm=6,style = {"padding":"10px", "padding-top":0}
                ),
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://i.ibb.co/5WmqFZS/IMG-20210211-161255-2.jpg", style = {'width':'100%',"padding-bottom":"20px"}),
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
                        ),lg = 3, md = 4, sm=6,style = {"padding":"10px", "padding-top":0}
                ),
                dbc.Col(
                    dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src= "https://i.ibb.co/4TBxKpY/imagen-2021-05-30-170435.png", style = {'width':'100%',"padding-bottom":"20px"}),
                                    html.H4("Jaaziel A. Bautista", className="card-title"),
                                    html.H6("Python from Zero to Hero   ", className="card-subtitle"),
                                    html.P(
                                    #    "Asistió a todas las clases. ",
                                        
                                        className="card-text",
                                    ),
                                    #dbc.CardLink("Github", href="#"),
                                    dbc.CardLink("Discord", href="https://discordapp.com/users/769361188025794570",target='_blank'),
                                ]
                            ),
                            style={"width": "100%"},
                        ),lg = 3, md = 4,sm=6, style = {"padding":"10px", "padding-top":0}
                ),
            ],justify="center", style = {"padding":30, "width":"100%"})
            ], style = {"padding-left":15, "text-justify": "inter-word"})
        ], style = {"padding":0, "background-color":"white", "color":"#3F3F3F"}
    ),
    ])
    ]