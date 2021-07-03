import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import colors

def proyectos():
    proyectos = ["Horarios de ESFM", "Automatización de limpieza de archivos locales", "Tracker de productos en tiendas online"]
    descripciones = [
                    html.P(["Creamos una tecnología que te permite visualizar y ordenar tu horario, la puedes encontrar dando click ", html.A("aquí", href = "https://horarioesfm.herokuapp.com",target='_blank',), "."]),
                    html.P(["El proyecto final de  Python from Zero to Hero fue un indexador de archivos mediante su extensión. Si tienes una carpeta con muchos archivos desordenados, corre nuestro código y este creará carpetas en las que organizará tus documentos segú su extensión. Puedes encontrarlo en nuestro ", html.A("Github", href = "https://github.com/JoulesCH",target='_blank'),"."]),
                    html.P(["Haciendo cómputo en la nube desde los servidores de Amazon Web Services pusimos en marcha un trackeador de precios de productos que deseemos comprar. Aún se sigue trabajando para volverlo plataforma, muy pronto podrás acceder y encontrar la mejor oferta. "])
                   
                   
                    ]
    def make_item(i):
        # we use this function to make the example items to avoid code duplication
        return dbc.Card(
            [
                dbc.CardHeader(
                    html.H2(
                        dbc.Button(
                            f"{proyectos[i-1]}",
                            color="link",
                            id=f"group-{i}-toggle",
                            style = {"color": "#7b1448", "font-weight": "bold"}
                        )
                    )
                ),
                dbc.Collapse(
                    dbc.CardBody([descripciones[i-1]]),
                    id=f"collapse-{i}",
                ),
            ]
        )

    
    return [

        html.Div([
                                        html.H1("Proyectos", className="display-3" , style ={"font-size":"3rem"} ),
                                        html.P(
                                            "En todos los cursos se designa un proyecto final que aporta algo a la comunidad.",
                                            className="lead",
                                        ),
                                        html.P(
                                            "El enfoque que tienen nuestros cursos te permiten poner en marcha tus proyectos de desarrollo. Si tienes alguna buena idea acércate a los integrantes del CdP ESFM y con gusto podremos ayudarte a volverla realidad. Conoce nuestras principales aportaciones: ",
                                        ),
                                        
                                        
                                                
                                                
                                            
                                        
                                        
                                        #html.P(html.A(dbc.Button("Unéte a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
                                    ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5}),
                                    html.Div(
                                            [make_item(1), make_item(2), make_item(3)], className="accordion", style = {"padding":50, "padding-top":5}
                                            )


    ]