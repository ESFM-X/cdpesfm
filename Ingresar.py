import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State




def ingresar():
    name_input = dbc.FormGroup(
    [
        dbc.Label("ID:", width=4, id="etiqueta_ingreso", style = {'text-align':'right'}),
        dbc.Col(
            dbc.Input(
                type="text", placeholder="", id = 'input_ingreso'
            ),
            width=5,
        ),
    ],
    row=True,
    )

    form = dbc.Form([name_input])
    return [html.Div([
                                        html.H1("Ingresa a tu perfil", className="display-3" , style ={"font-size":"3rem"} ),
                                        html.P(
                                            "Podrás acceder a la trayectoria de tus  cursos",
                                            className="lead",
                                        ),
                                        #html.P(html.A(dbc.Button("Unéte a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
                                    ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5}),
            html.Div([    
                dbc.Row([
                    dbc.Col(form)
                ]),
                html.P([''], id='mensaje-exito2',style = {'color':'green', 'text-align':'center'}),
                html.P([''], id='mensaje-error2',style = {'color':'red', 'text-align':'center'}),
                html.P([''], id='mensaje-contrasena',style = {'color':'black', 'text-align':'center'}),
                html.Div(
                    dbc.Button("Aceptar", color="danger", block=True, id = 'ingresar_boton'),
                    style = {"width":"30%", "margin-left":"auto", "margin-right":"auto"}
                )


            ], style = {'padding':'1em'})
            
            ]