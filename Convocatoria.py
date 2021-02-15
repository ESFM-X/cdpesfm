import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import colors
 

def convocatoria():

    return [html.Div([
                                        html.H1("Convocatoria 2021-1", className="display-3" , style ={"font-size":"3rem"} ),
                                        html.P(
                                            "Falta muy poco para que puedas se parte de nuestra comunidad",
                                            className="lead",
                                        ),
                                        html.P(
                                            "La convocatoria se abrirá la primera semana de regreso a clases (febrero 22-27) ",
                                        ),
                                        html.P([
                                            "Requisitos indispensables: ",
                                            html.Ul([
                                                html.Li("Ser parte de la comunidad de estudiantes politécnica"),
                                                html.Li("Tener tu boleta y correo institucional activos"),
                                                html.Li("Si ya has tomado cursos en el CdP ESFM, tener tu ID de registro anterior")
                                            ])

                                        ])
                                        
                                        
                                                
                                                
                                            
                                        
                                        
                                        #html.P(html.A(dbc.Button("Unéte a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
                                    ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5}),
                                    
                                    
        ]