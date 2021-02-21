import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

def footer():
    return [html.Div([html.Div([dbc.Jumbotron(
                                [
                                    html.Div(
                                        [
                                            html.Img(src="https://fotos.subefotos.com/8d86f83446ffc85b28747e51e666f4b5o.png", height = 50, style = {"margin":5}),
                                            html.Img(src="https://fotos.subefotos.com/076df224d0bb0b75749aa140d0c955afo.png", height = 50, style = {"margin":5}),
                                            html.Img(src="https://fotos.subefotos.com/d832491f73b5c1db1fa9d6d704177fcao.png", height = 40, style = {"margin":5}),
                                            html.Div([
                                                html.A('Facebook   ', href = '#', style = {'color':'#3b5998', 'text-align':'center'}),    #,target='_blank'
                                                #html.A('   Instagram', href = '#', style = {'padding-left':10,'color':'#C13584', 'text-align':'center'}),    #,target='_blank'
                                                html.A('   Discord', href = 'https://discord.com/users/396799146977132544',target='_blank', style = {'padding-left':10,'color':'#7289da', 'text-align':'center'})    
                                            ], style = {"padding-left":65})
                                        ],
                                        style = {"margin-left":"auto","margin-right":"auto", "width":282, "padding-bottom":10}
                                    ),
                                    dbc.Row(
                                        [
                                        
                                            dbc.Col([
                                                
                                            html.H5("Dirección"),#, className="display-6"),
                                            html.Hr(className="my-2"),
                                        # html.P(
                                            #"Visita nuestras redes sociales",
                                                #"featured content or information.",
                                            #    className="lead",
                                            #),
                                            
                                            html.P('Av. Instituto Politécnico Nacional s/n Edificio 9 Unidad Profesional “Adolfo López Mateos” Col. San Pedro Zacatenco, Del. Gustavo A. Madero, Ciudad de México C.P. 07738, Ciudad de México; México 2009-2013. Conmutador 01 (55) 5729 6000, ext. 55343',
                                                    style = {"text-align":"justify"}),
                                            
                                            ], style = {'color':'black'}),

                                            #dbc.Col(html.Img(src = 'https://fotos.subefotos.com/a451cf35b3875a515c3ec89042922cebo.png', style = {'width':'100%', 'padding-bottom':10,'margin-left':'auto','margin-right':'auto'})),
                                            
                                            dbc.Col([
                                                
                                                html.H5("Responsables"),#, className="display-6"),
                                                html.Hr(className="my-2"),
                                                html.P('Julio Hernández - joules.hdz@gmail.com'),
                                                html.P('Alejandro Cardona - acardmx@gmail.com '),
                                                html.P('Rodolfo Lagunas - rodolfolj97@gmail.com '),
                                                #html.P('club.de.programacion.esfm@gmail.com')
                                            ], style = {'color':'black'}),
                                        
                                        ]
                                    ),
                                    html.H6("Página hecha con ❤ por el CdP ESFM", style = {"text-align":'center', "padding-top":30}),
                                    #html.Div(dbc.Button('El canal de YouTube de Aurus Tek', color="link", style = {'width':'100%','margin-left':'auto','margin-right':'auto','color':'#8797b4'}), className="lead", style = {'width':'70%','margin-left':'auto','margin-right':'auto', 'padding-top':0})
                                    
                                ],
                                style = {'padding-top':15, 'background':'#EAEAEA','margin-bottom':0, 'padding-bottom':20}
                            )], style ={'background': '#EAEAEA', 'width':'100%'} ),


                            #html.Div([ dbc.ListGroup(
                            #    [
                            #        dbc.ListGroupItem(
                            #            [
                            #                dbc.ListGroupItemHeading("Más información"),
                            #                dbc.ListGroupItemText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut neque nisi, pretium et mauris eget, interdum consectetur elit. Donec euismod egestas elit, eget egestas ligula convallis id. Integer quis arcu quis arcu porta bibendum. Vivamus venenatis leo neque, id placerat libero euismod ut. Vivamus feugiat id eros nec ultricies. "),
                            #            ], style = {'background':'#7b7c7e', 'color':'white'}
                            #        )
                            #    ], 
                            #)], style = {'background':'#7b7c7e'}),

                            # html.Div([
                            #                     dbc.Row([
                            #                             #dbc.Col([html.P('Aurus Tek', style = {'margin-bottom':0})], style = {'text-align':'center'}),
                            #                             dbc.Col([html.A('Políticas de Garantía', style = {'margin-bottom':0}, href = 'https://drive.google.com/file/d/1rFQZGNWG6uHGzuif00A4WqzmfYCSXWNf/view?usp=sharing')], style = {'text-align':'center'}),
                            #                             #dbc.Col([html.A('Contácto', style = {'margin-bottom':0})], style = {'text-align':'center'}),
                            #                         ], style = {'width':'100%'})
                            #                 ],style = {'width':'100%', 'padding-top':5, 'background':'#7b7c7e','margin-bottom':0, 'padding-bottom':5,'color':'white', 'font-size':'0.8em'})
                            ]
                            )]

