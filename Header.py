import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import colors

def header():
    #link = "https://lh3.googleusercontent.com/fife/ABSRlIqbkENPI3fzn5DDnCh_E-WqK1Ba_VKkQ5KqhZYQw37yVYUBLvdWwqOWJBiwXbV-4bIbe3Y7rMqCP9alD2O0RThDo9kMFqSv5rXAKmJslda6coHoR172B27aW17oMcQrag02fpjSYbtrXJEpyoM0_UqcbxrG7AkjdDLTGzmJtMYNF1_ZSkl_oRKPZcY6fDkxVaVC3vT336nLuO5_WTCaWNwSOxOvJdU8WJVFGuAcJrF_mudrpxSkO22m4gsNs3pHNb1WAk07ccO7ICARV_afGdYoPV1YCtkHLJBgs-lmTpvjpUvz_sxWgBNT4b_8Cc2yCX-HTBcKJ6A1HZqbi0aa06wMFOLuivV3dsfkJZfqJT39AIFPeexfT46fj_sCM1rSjU1JhpBZsuzJkOIXT9nCWXDD162xIKulyvm7z9DA7N9wetm1R1Tv0mBFh8w7V_-czZobE8s0Df5MxLAVdV0YRpWlFn0z7JopU2uFBCx5WoDvK7eVgl14sU5itBiOCgRceQhDzMh6fidpdEOY9aceou1vi07jVnHOXqT0l0WItkTFjrYEa-1g5WAZ5RZhYFYPuB3v57Hv5tuDdpxafVRROOJl4d5XiNk54FnrhWmSazirrMAFlZnPDABG1VlgcKXb3pXhfQO02QNLJZrz9l7h0qizPTJbiKRkuHEESJJvH5MALuVbZQTek2t9F4CzMRRZXJkgtVfr8wfuGV4VOYU2TEZ0R5Jjg57MgGA=w1326-h668-ft"
    link = "https://cdn.discordapp.com/attachments/798047392405913601/811435939284254740/CdP_ESFM.gif"
    search_bar = dbc.Row(
                    [
                        dbc.Col(dbc.Input(type="search", placeholder="Buscar", id="search_input")),
                        dbc.Col(
                            dbc.Button("🔎", color="danger", className="ml-2", id = "search"),
                            width="auto",
                        ),
                    ],
                    no_gutters=True,
                    className="ml-auto flex-nowrap mt-3 mt-md-0",
                    align="center",
                )
    return dbc.Navbar(
                        [
                            html.A(
                                # Use row and col to control vertical alignment of logo / brand
                                dbc.Row(
                                    [
                                        dbc.Col(html.Img(id = "logo",src= link,#src="https://fotos.subefotos.com/921ce26e26dacaae534d68a2f0f13392o.png",#"https://lh3.googleusercontent.com/fife/ABSRlIqbkENPI3fzn5DDnCh_E-WqK1Ba_VKkQ5KqhZYQw37yVYUBLvdWwqOWJBiwXbV-4bIbe3Y7rMqCP9alD2O0RThDo9kMFqSv5rXAKmJslda6coHoR172B27aW17oMcQrag02fpjSYbtrXJEpyoM0_UqcbxrG7AkjdDLTGzmJtMYNF1_ZSkl_oRKPZcY6fDkxVaVC3vT336nLuO5_WTCaWNwSOxOvJdU8WJVFGuAcJrF_mudrpxSkO22m4gsNs3pHNb1WAk07ccO7ICARV_afGdYoPV1YCtkHLJBgs-lmTpvjpUvz_sxWgBNT4b_8Cc2yCX-HTBcKJ6A1HZqbi0aa06wMFOLuivV3dsfkJZfqJT39AIFPeexfT46fj_sCM1rSjU1JhpBZsuzJkOIXT9nCWXDD162xIKulyvm7z9DA7N9wetm1R1Tv0mBFh8w7V_-czZobE8s0Df5MxLAVdV0YRpWlFn0z7JopU2uFBCx5WoDvK7eVgl14sU5itBiOCgRceQhDzMh6fidpdEOY9aceou1vi07jVnHOXqT0l0WItkTFjrYEa-1g5WAZ5RZhYFYPuB3v57Hv5tuDdpxafVRROOJl4d5XiNk54FnrhWmSazirrMAFlZnPDABG1VlgcKXb3pXhfQO02QNLJZrz9l7h0qizPTJbiKRkuHEESJJvH5MALuVbZQTek2t9F4CzMRRZXJkgtVfr8wfuGV4VOYU2TEZ0R5Jjg57MgGA=w1326-h668-ft", 
                                                        height="70px",
                                                        style = {'padding-right':'40px'})),
                                        #dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
                                    ],
                                    align="center",
                                    no_gutters=True,
                                ),
                                href="/",
                            ),
                            dbc.NavbarToggler(id="navbar-toggler"),
                            dbc.Collapse(#search_bar
                                        [
                                            dbc.NavItem(dbc.NavLink("💬 Conócenos", href="/acerca"), style ={'list-style-type': 'none', "font-weight": "bold"}),
                                            dbc.NavItem(dbc.NavLink("🎯 Cursos", href="/cursos"), style ={'list-style-type': 'none', "font-weight": "bold"}),
                                            #dbc.NavItem(dbc.NavLink("Alumnos destacados", href="/destacados"), style ={'list-style-type': 'none'}),
                                            dbc.NavItem(dbc.NavLink("👨‍💻 Proyectos", href="/proyectos"), style ={'list-style-type': 'none', "font-weight": "bold"}),
                                            dbc.NavItem(dbc.NavLink("📑 Convocatoria", href="/convocatoria"), style ={'list-style-type': 'none', "font-weight": "bold"}),
                                            #dbc.NavItem(dbc.NavLink("🧦 Artículos", href="/articulos"), style ={'list-style-type': 'none', "font-weight": "bold"}),
                                            dbc.NavItem(dbc.NavLink("☎ Soporte", href="/soporte"), style ={'list-style-type': 'none', "font-weight": "bold"}),
                                           # dbc.NavItem(dbc.NavLink("🏚 Ingresar", href="/ingresar"), style ={'list-style-type': 'none', "font-weight": "bold"}),
                                            search_bar,
                                            
                                        ],
                             id="navbar-collapse", 
                             navbar=True),
                             
                        ],
                        color="light",
                        dark=False,
                        style = {},
                        sticky = "top"
                    )