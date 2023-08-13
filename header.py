"""This function file is for the header layout"""

from dash import html

def create_header():
    """ function to generate the layout of the header"""

    header_components = html.Div(
        [
            html.Div(
                [
                    html.Label(
                        "New Zealand International Visitors Tourism Dashboard",
                        className="header-title",
                    ),
                    html.Br(),
                    html.Label(
                        "Historical Analysis of Foreign Tourism",
                        className="header-subtitle",
                        style={"font-size": "1rem"},
                    ),
                ],
                className="header-content",
            )
        ],
        className="header-background",
    )

    return header_components
