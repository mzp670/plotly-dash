"""This function file is for the layout of the card metrics"""

from dash import html
import dash_bootstrap_components as dbc

def create_metrics():
    """ function to generate the layout of the card metrics row"""
    
    metrics_components = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.I(className="bi bi-coin me-0", style={"font-size": "2rem"}),
                                ],
                            ),
                            html.H3(id="international-value", children="Value here", style={"margin-top": ".3rem", "font-size": "100%"}),
                            html.H6("International Visitors", style={"margin-top": "0rem", "font-size": "70%", "margin": "0"}),
                            html.H6("Travel Expenditure", style={"font-size": "70%", "margin": "0", "margin-bottom": ".3rem"}),
                        ],
                        width=2,
                        className="text-center m-2",
                        style={"background-color": "white", "border": "1px solid lightgray", "box-shadow": "1px 1px 1px rgba(0, 0, 0, 0.1)"},
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.I(className="bi bi-coin me-0", style={"font-size": "2rem"}),
                                ],
                            ),
                            html.H3(id="domestic-value", children="Value here", style={"margin-top": ".3rem", "font-size": "100%"}),
                            html.H6("Domestic Visitors", style={"margin-top": "0rem", "font-size": "70%", "margin": "0"}),
                            html.H6("Travel Expenditure", style={"font-size": "70%", "margin": "0", "margin-bottom": ".3rem"}),
                        ],
                        width=2,
                        className="text-center m-2",
                        style={"background-color": "white", "border": "1px solid lightgray", "box-shadow": "1px 1px 1px rgba(0, 0, 0, 0.1)"},
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.I(className="bi bi-people-fill me-0", style={"font-size": "2rem"}),
                                ],
                            ),
                            html.H3(id="pax-value", children="Value here", style={"margin-top": ".3rem", "font-size": "100%"}),
                            html.H6("International Visitors", style={"margin-top": "0rem", "font-size": "70%", "margin": "0"}),
                            html.H6("Number of Persons", style={"font-size": "70%", "margin": "0", "margin-bottom": ".3rem"}),
                        ],
                        width=2,
                        className="text-center m-2",
                        style={"background-color": "white", "border": "1px solid lightgray", "box-shadow": "1px 1px 1px rgba(0, 0, 0, 0.1)"},
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.I(className="bi bi-credit-card-2-back-fill me-0", style={"font-size": "2rem"}),
                                ],
                            ),
                            html.H3(id="spend-value", children="Value here", style={"margin-top": ".3rem", "font-size": "100%"}),
                            html.H6("International Visitors", style={"margin-top": "0rem", "font-size": "70%", "margin": "0"}),
                            html.H6("Mean Travel Spending", style={"font-size": "70%", "margin": "0", "margin-bottom": ".3rem"}),
                        ],
                        width=2,
                        className="text-center m-2",
                        style={"background-color": "white", "border": "1px solid lightgray", "box-shadow": "1px 1px 1px rgba(0, 0, 0, 0.1)"},
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.I(className="bi bi-cart4 me-0", style={"font-size": "2rem"}),
                                ],
                            ),
                            html.H3(id="night-value", children="Value here", style={"margin-top": ".3rem", "font-size": "100%"}),
                            html.H6("International Visitors", style={"margin-top": "0rem", "font-size": "70%", "margin": "0"}),
                            html.H6("Average Spend per Night", style={"font-size": "70%", "margin": "0", "margin-bottom": ".3rem"}),
                        ],
                        width=2,
                        className="text-center m-2",
                        style={"background-color": "white", "border": "1px solid lightgray", "box-shadow": "1px 1px 1px rgba(0, 0, 0, 0.1)"},
                    ),
                ],
                className="row-column-1 p-0 mb-0 gap-3",
            ),
        ],
        fluid=True,
    )
    return metrics_components