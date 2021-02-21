import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import colors

def cursos():
        card_content_1 = [
            dbc.CardImg(src="https://fotos.subefotos.com/ff1e2b90cc975981cb813073f8db0f23o.png", top=True),
            dbc.CardBody(
                [
                    html.H5("Python from Zero to Hero", className="card-title"),
                    html.P(
                        "Aprende desde cero el lenguaje con mayor crecimiento en los últimos años. Ideal para adentrarse al mundo de la programación por su sintáxis. Este curso te dará las herramientas necesarias para tomar los cursos de Ingeniería de datos, Introducción a Machine Learning con Python y Python from Hero to God.",
                        className="card-text",
                    ),
                    dbc.Button("Ver temario", color="danger", id = "tpyt"),
                ]
            ),
        ]

        card_content_2 = dbc.CardBody(
            [
                html.Blockquote(
                    [
                        html.P(
                            "A learning experience is one of those things that says, "
                            "'You know that thing you just did? Don't do that.'"
                        ),
                        html.Footer(
                            html.Small("Douglas Adams", className="text-muted")
                        ),
                    ],
                    className="blockquote",style = {'text-align':'justify'}
                )
            ]
        )

        card_content_3 = [
            dbc.CardImg(src="https://fotos.subefotos.com/ab267ce64ba84a0bc521bd8a98b212fao.png", top=True),
            dbc.CardBody(
                [
                    html.H5("Ingeniería de Datos", className="card-title"),
                    html.P(
                        "Aprende los procesos para obtener datos del mundo real. Conocerás a profundidad los procesos para la obtención de datos y su tratamiento, dejándolos listos para su análisis posterior (ETL). También automatizarás esos procesos.",
                        className="card-text",style = {'text-align':'justify'}
                    ),
                    dbc.Button("Ver temario", color="danger", id = "ting"),
                ]
            ),
        ]

        card_content_4 = [
            dbc.CardImg(src="https://fotos.subefotos.com/508d96fa6d25b4343eeab680eb074460o.png", top=True),
            dbc.CardBody(
                [
                    html.H5("MATLAB", className="card-title"),
                    html.P(
                        "Aprende análisis iterativo y logra expresar las matemáticas de matrices y arrays con las tecnologías que ofrece MATLAB.",
                        className="card-text",style = {'text-align':'justify'}
                    ),
                    dbc.Button("Ver temario", color="danger", id = "tmat"),
                ]
            ),
        ]
        card_content_5 = [
            dbc.CardImg(src="https://fotos.subefotos.com/982e203c664ec05e2dec2ed72ef83bc2o.png", top=True),
            dbc.CardBody(
                [
                    html.H5("Criptografía Aplicada en C++", className="card-title"),
                    html.P(
                        "Existen datos 'sensibles' como lo son: planes de operaciones comerciales o militares, movimientos financieros de empresas y personas, entre otras. En general nos referimos a 'información sensible' a cualquiera que en caso de caer en manos equivocadas mientras viaja por un medio inseguro (como el Internet) desencadene en un daño para la persona u organización dueño de ella; como: pérdidas de dinero, invasión de privacidad o anticipación de estrategias, etc. ",
                        className="card-text",style = {'text-align':'justify'}
                    ),
                    dbc.Button("Ver temario", color="danger", id = "tcrip"),
                ]
            ),
        ]
        card_content_6 = [
            dbc.CardImg(src="https://fotos.subefotos.com/9a5c12e822a32f434f4dc47d8ccd2bd9o.png", top=True),
            dbc.CardBody(
                [
                    html.H5("Python from Hero to God", className="card-title"),
                    html.P(
                        "Con este curso llegarás al siguiente nivel, en el que aprenderás cómo desarrollar todos los proyectos que tengas en mente. Podrás obtener datos de tus usuarios desde una interfaz de escritorio, una página web o hasta una aplicación móvil.",
                        className="card-text",style = {'text-align':'justify'}
                    ),
                    dbc.Button("Ver temario", color="danger", id = "tpya"),
                ]
            ),
        ]
        card_content_7 = [
            dbc.CardImg(src="https://fotos.subefotos.com/8f2f92bb9836c6e0c7ea5b1fdc9d35d2o.png", top=True),
            dbc.CardBody(
                [
                    html.H5("Introducción a Machine Learning con Python", className="card-title"),
                    html.P(
                        "Obtén los fundamentos para modelar con algoritmos de Machine Learning e Inteligencia Artificial el mundo real.  ",
                        className="card-text",style = {'text-align':'justify'}
                    ),
                    dbc.Button("Ver temario", color="danger"),
                ]
            ),
        ]
        card_content_8 = [
            dbc.CardImg(src="https://fotos.subefotos.com/667724ccdf09cd068f0263e231b4b6bdo.png", top=True),
            dbc.CardBody(
                [
                    html.H5("Wolfram Mathematica", className="card-title"),
                    html.P(
                        "Deja de utilizar Word y aprende a darle formato a tus ecuaciones y documentos científicos en Mathematica. En este curso conocerás su sintáxis y cómo programar.",
                        className="card-text", style = {'text-align':'justify'}
                    ),
                    dbc.Button("Ver temario", color="danger", id = "twol"),
                ]
            ),
        ]
        return  [
                html.Div([
                                        html.H1("Conoce todos nuestros cursos", className="display-3" , style ={"font-size":"3rem"} ),
                                        html.P(
                                            "No es necesario tener conocimientos sobre los cursos, pero algunos sí requieren conocimientos previos. ",
                                            className="lead",
                                        ),
                                        html.P(
                                            "En el CdP ESFM impartimos los siguientes cursos 100% gratuitos:",
                                        ),
                                        dbc.Row(
                                                [
                                                
                                                    dbc.Col([
                                                            html.Ul(
                                                                    [
                                                                        html.Li("Python from Zero to Hero"),
                                                                        html.Li("Criptografía Aplicada en C++"),
                                                                        #html.Li("Introducción a Machine Learning con Python"),
                                                                        html.Li("Ingeniería de Datos"), 
                                                                    ])

                                                            ]),

                                
                                                    dbc.Col([
                                                            html.Ul([
                                                                        html.Li("MATLAB"),
                                                                        html.Li("Wolfram Mathematica"),
                                                                        html.Li("Python from Hero to God"),
                                                                    ])

                                                            ]),
                                                
                                                ]
                                            ),
                                        
                                                
                                                
                                            
                                        
                                        
                                        #html.P(html.A(dbc.Button("Unéte a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
                                    ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5}),
                dbc.CardColumns(
            [
                dbc.Card(card_content_1, color="primary", inverse=True),
                #dbc.Card(card_content_2, body=True),
                
                dbc.Card(card_content_6, color="warning", inverse=True),
                dbc.Card(card_content_5, className= "cripto", inverse=True),
                dbc.Card(card_content_3, color="dark", inverse=True),
                dbc.Card(card_content_4, color="info", inverse=True),
                #dbc.Card(card_content_7, color="success", inverse=True),
                dbc.Card(card_content_8, color="success", inverse=True),
                # dbc.Card(card_content_1, color="dark", inverse=True),
                dbc.Modal(
                            [
                                dbc.ModalHeader("Python from Zero to Hero "),
                                dbc.ModalBody([
                                    html.P("Temario: "),
                                    html.Ul(
                                                                    [
                                                                        html.Li("Introducción a la terminal y consola"),
                                                                        html.Li("Jupyter Notebooks"),
                                                                        html.Li("Introducción a algoritmos"),
                                                                        html.Li("Tipos de datos"),
                                                                        html.Li("Operadores"),
                                                                        html.Li("Programación secuencial"),
                                                                        html.Li("Programación estructurada"),
                                                                        html.Li("Estructuras de datos"),
                                                                        html.Li("Programación modular"),
                                                                        html.Li("Programación defensiva"),
                                                                        html.Li("Pruebas y debugging"),
                                                                        html.Li("Complejidad algorítmica"),
                                                                        html.Li("Programación dinámica"),
                                                                        html.Li("Programación orientada a objetos"),           
                                                                    ])
                                ],
                            className = "tpyt"),
                                dbc.ModalFooter(
                                    dbc.Button("Cerrar", id="close-py", color = "danger")
                                ),
                            ],
                            id="modal-py",
                            size="lg",
                            centered = True
                        ),
                dbc.Modal(
                            [
                                dbc.ModalHeader("Ingeniería de Datos"),
                                dbc.ModalBody([
                                    html.P("Temario: "),
                                    html.Ul(
                                                                    [
                                                                        html.Li("Repaso de Python"),
                                                                        html.Li("Introdución a la ciencia de datos"),
                                                                        html.Li("Roles de la ciencia de datos"),
                                                                        html.Li("Jupyter Notebooks"),
                                                                        html.Li("Procesos ETL"),
                                                                        html.Li("Web Scraping"),
                                                                        html.Li("Introducción a Pandas"),
                                                                        html.Li("Implementación de Pipelines"),
                                                                        html.Li("Bases de datos"),
                                                                        html.Li("Cómputo en la nube"),
                                                                        html.Li("Creación de dashboards"),       
                                                                    ])
                                ],
                            className = "ting"),
                                dbc.ModalFooter(
                                    dbc.Button("Cerrar", id="close-ing", color = "danger")
                                ),
                            ],
                            id="modal-ing",
                            size="lg",
                            centered = True
                        ),
                dbc.Modal(
                            [
                                dbc.ModalHeader("MATLAB"),
                                dbc.ModalBody([
                                    html.P("Temario: "),
                                    html.Ul(
                                                                    [
                                                                        html.Li("Operaciones con datos y variables"),
                                                                        html.Li("Vectores y matrices"),
                                                                        html.Li("Estructura de programación en Matlab"),
                                                                        html.Li("Gráficos en 2D y 3D"),
                                                                        html.Li("Operaciones con polinomios y ecuaciones"),
                                                                            
                                                                    ])
                                ],
                            className = "tmat"),
                                dbc.ModalFooter(
                                    dbc.Button("Cerrar", id="close-mat", color = "danger")
                                ),
                            ],
                            id="modal-mat",
                            size="lg",
                            centered = True
                        ),
                dbc.Modal(
                            [
                                dbc.ModalHeader("Python from Hero to God"),
                                dbc.ModalBody([
                                    html.P("Temario en desarrollo. "),
                                    html.Ul(
                                                                    [
                                                                        #html.Li("Operaciones con datos y variables"),
                                                                        #html.Li("Vectores y matrices"),
                                                                        #html.Li("Estructura de programación en Matlab"),
                                                                        #html.Li("Gráficos en 2D y 3D"),
                                                                        #html.Li("Operaciones con polinomios y ecuaciones"),
                                                                            
                                                                    ])
                                ],
                            className = "tpya"),
                                dbc.ModalFooter(
                                    dbc.Button("Cerrar", id="close-pya", color = "danger")
                                ),
                            ],
                            id="modal-pya",
                            size="lg",
                            centered = True
                        ),
                dbc.Modal(
                            [
                                dbc.ModalHeader("Criptografía Aplicada en C++"),
                                dbc.ModalBody([
                                    html.P("Temario en desarrollo. "),
                                    html.Ul(
                                                                    [
                                                                        #html.Li("Operaciones con datos y variables"),
                                                                        #html.Li("Vectores y matrices"),
                                                                        #html.Li("Estructura de programación en Matlab"),
                                                                        #html.Li("Gráficos en 2D y 3D"),
                                                                        #html.Li("Operaciones con polinomios y ecuaciones"),
                                                                            
                                                                    ])
                                ],
                            className = "tcrip"),
                                dbc.ModalFooter(
                                    dbc.Button("Cerrar", id="close-crip", color = "danger")
                                ),
                            ],
                            id="modal-crip",
                            size="lg",
                            centered = True
                        ),
                dbc.Modal(
                            [
                                dbc.ModalHeader("Wolfram Mathematica"),
                                dbc.ModalBody([
                                    html.P("Temario en desarrollo. "),
                                    html.Ul(
                                                                    [
                                                                        #html.Li("Operaciones con datos y variables"),
                                                                        #html.Li("Vectores y matrices"),
                                                                        #html.Li("Estructura de programación en Matlab"),
                                                                        #html.Li("Gráficos en 2D y 3D"),
                                                                        #html.Li("Operaciones con polinomios y ecuaciones"),
                                                                            
                                                                    ])
                                ],
                            className = "twol"),
                                dbc.ModalFooter(
                                    dbc.Button("Cerrar", id="close-wol", color = "danger")
                                ),
                            ],
                            id="modal-wol",
                            size="lg",
                            centered = True
                        ),
            ], style = {"padding":"30px", "padding-top":20}#,'text-align':'justify'}
        )]