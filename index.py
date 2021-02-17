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
                        a continuación te proporcionamos la dirección al servidor de Discord, en donde podrás encontrar material de cursos pasados, hacer reseñas de profesores, ver peliculas 
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
                                html.Img(src="https://fotos.subefotos.com/4b27caae6fb7c29b8551f171d5195ecbo.png", style = {"width":"100%","margin-left":"auto" }) 
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
            ], style = {"padding-left":5, "text-justify": "inter-word"})
        ], style = {"padding":20, "background-color":"white", "color":"#3F3F3F"}
    ),
    
    ]