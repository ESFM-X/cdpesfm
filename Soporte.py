 
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import colors
 
 
def soporte():
    name_input = dbc.FormGroup(
    [
        dbc.Label("Nombre*", width=4, style = {'text-align':'right'}),
        dbc.Col(
            dbc.Input(
                type="text", placeholder="Nombre y Apellido", id = 'nombre'
            ),
            width=7,
        ),
    ],
    row=True,
    )

    email_input = dbc.FormGroup(
        [
            dbc.Label("Correo*", html_for="example-email-row", width=4, style = {'text-align':'right'}),
            dbc.Col(
                dbc.Input(
                    type="email", placeholder="Ingresa tu e-mail",id = 'correo'
                ),
                width=7,
            ),
        ],
        row=True,
    )

    number_input = dbc.FormGroup(
        [
            dbc.Label("Número", html_for="example-password-row", width=4, style = {'text-align':'right'}),
            dbc.Col(
                dbc.Input(
                    type="number",
                    #id="example-password-row",
                    placeholder="Ingresa si quieres que te llamemos", id = 'numero'
                ),
                width=7,
            ),
        ],
        row=True,
    )

    radios_input = dbc.FormGroup(
        [
            dbc.Label("Motivo*", html_for="example-radios-row", width=4, style = {'text-align':'right'}),
            dbc.Col(
                dbc.RadioItems(
                    id="interes",
                    options=[
                        {"label": "Ayuda con mi registro", "value": "Ayuda"},
                        {"label": "Duda", "value": "Duda"},
                        {"label": "Contactar", "value": "Contacto",
                            #"disabled": True,
                        },
                    ],
                ),
                width=7,
            ),
        ],
        row=True,
    )

    input_large = dbc.FormGroup(
        [
            dbc.Label("Comentario", html_for="example-password-row", width=4, style = {'text-align':'right'}),
            dbc.Col(
                dbc.Textarea(className="mb-3", placeholder="Agrega más detalle a tu solicitud de contacto", id = 'comentario'),

                width=7,
            ),
        ],
        row=True,
    )
    form = dbc.Form([name_input,email_input, radios_input,input_large])
    return [html.Div([
                                        html.H1("Soporte", className="display-3" , style ={"font-size":"3rem"} ),
                                        html.P(
                                            "¿Tienes algún problema con tu registro o quieres ponerte en contacto con nosotros? ",
                                            className="lead",
                                        ),
                                        html.P(
                                            "Llena este formulario y nos contactaremos contigo lo más pronto posible: ",
                                        ),
                                        
                                        
                                                
                                                
                                            
                                        
                                        
                                        #html.P(html.A(dbc.Button("Unéte a Discord", color="primary"), href = "https://discord.gg/JxS59BFBu3",target="_blank" ), className="lead"),
                                    ], style = {"padding":"20px", "padding-top":20, "padding-bottom":5}),
            html.Div([ 
                #html.Img(src = 'https://fotos.subefotos.com/a19bbf1ed6808b6b56f250d7aed97c5ao.png', width = "100%"),
                #html.H1("Ingresa tus datos y nos pondremos en contácto lo antes posible", className="display-4", style = {'padding-top':30,'font-size':'2.3em','padding-bottom':30}),
                    
                dbc.Row([
                    dbc.Col(form)
                ]),
                html.P([''], id='mensaje-exito',style = {'color':'green', 'text-align':'center'}),
                html.P([''], id='mensaje-error',style = {'color':'red', 'text-align':'center'}),
                html.Div(
                    dbc.Button("Enviar", color="danger", block=True, id = 'enviar'),
                    style = {"width":"30%", "margin-left":"auto", "margin-right":"auto"}
                )


            ], style = {'padding':'1em'})
            
            ]
                                    