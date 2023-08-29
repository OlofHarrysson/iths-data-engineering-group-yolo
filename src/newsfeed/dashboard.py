import json
import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1("Updated in the world of AI")), class_name="mt-3"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("search Title:"),
                        dbc.Input(id="input", value="", type="text"),
                        html.Div(id="output"),
                    ]
                )
            ]
        ),
        dbc.Card(dbc.CardBody(html.H1("Articles")), class_name="mt-3"),
        html.Button("Refresh", id="load-button"),
        html.Div(id="summaries-container"),
    ]
)


@app.callback(Output("output", "children"), [Input("input", "value")])
def updated_output(input_value):
    return f"You entered: {input_value}"


@app.callback(Output("summaries-container", "children"), [Input("load-button", "n_clicks")])
def load_smmaries(n_clicks):
    if n_clicks is None:
        return []

    summeries_path = "data/data_warehouse/mit/summaries"
    summeries = [file for file in os.listdir(summeries_path) if file.endswith(".json")]

    summery_components = []

    for summery in summeries:
        with open(summeries_path + "/" + summery, "r") as summery_file:
            json_data = json.load(summery_file)

        title = json_data.get("title", "missing title")
        text = json_data.get("text", "missing text")

        summery_component = dbc.Card(
            [
                dbc.CardHeader(html.H2(title)),
                dbc.CardBody(html.P(text)),
            ],
            class_name="mb-3",
        )

        summery_components.append(summery_component)

    return summery_components


if __name__ == "__main__":
    app.run_server(debug=True)
