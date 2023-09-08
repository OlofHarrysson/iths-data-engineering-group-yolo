import json
import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from utils import load_files

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1("News in the world of AI")), class_name="mt-3"),
        dbc.Row(
            [dbc.Col([html.Label("Search Title:"), dbc.Input(id="input", value="", type="text")])]
        ),
        dbc.Card(dbc.CardBody(html.H1("Articles")), class_name="mt-3"),
        dbc.Col(
            dcc.Tabs(
                id="blog-tabs",
                value="tab-1",
                children=[
                    dcc.Tab(
                        label="mit",
                        value="tab-1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        label="big_data",
                        value="tab-2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ),
        html.Div(id="summaries-container"),
    ]
)


@app.callback(
    Output("summaries-container", "children"),
    [Input("blog-tabs", "value"), Input("input", "value")],
)
def load_smmaries(tab, search_value):
    if tab == "tab-1":
        blog = "mit"
    elif tab == "tab-2":
        blog = "big_data"

    summeries_path = "data/data_warehouse/" + blog + "/summaries"
    summery_components = []

    articles = load_files(summeries_path)

    for article in articles:
        if search_value.lower() not in article["title"].lower():
            continue

        summery_component = dbc.Card(
            [
                dbc.CardHeader(html.H2(article["title"])),
                dbc.CardBody(
                    html.Div(
                        [
                            html.P(article["text"]),
                            html.P(article["simple"]),
                            html.A("Read full article", href=article["link"], target="blank"),
                            html.P(article["date"]),
                        ]
                    )
                ),
            ],
            class_name="mb-3",
        )

        summery_components.append(summery_component)

    # return summery_components

    row_components = []

    for i in range(0, len(summery_components), 2):
        row = dbc.Row(
            [dbc.Col(summery_components[i], width=6), dbc.Col(summery_components[i + 1], width=6)],
            class_name="mb-3",
        )

        row_components.append(row)

    return row_components


if __name__ == "__main__":
    app.run_server(debug=True)
