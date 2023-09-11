import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from newsfeed.utils import load_files

# themes DARKLY, CYBORG, QUARTZ, MORPH, SKETCHY, SLATE, SOLAR
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])

app.layout = dbc.Container(
    [
        dbc.Card(dbc.CardBody(html.H1("News in the world of AI")), class_name="mt-3"),
        dbc.Col(
            dcc.Tabs(
                id="blog-tabs",
                value="tab-1",
                children=[
                    dcc.Tab(
                        label="Technical",
                        value="tab-1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        label="Non-Technical",
                        value="tab-2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ),
        # dbc.Card(dbc.CardBody(html.H1("Articles")), class_name="mt-3"),
        dbc.Row(
            [dbc.Col([html.H5("Search Title:"), dbc.Input(id="input", value="", type="text")])]
        ),
        dbc.Col(html.H5("Blog:")),
        dbc.Col(
            dcc.Dropdown(
                id="blog-picker",
                options=[
                    {"label": option[0], "value": option[1]}
                    for option in (("MIT", "mit"), ("Big data", "big_data"))
                ],
                value="mit",
            ),
            class_name="mb-3",
        ),
        html.Div(id="summaries-container"),
    ]
)


@app.callback(
    Output("summaries-container", "children"),
    [Input("blog-tabs", "value"), Input("input", "value"), Input("blog-picker", "value")],
)
def load_smmaries(tab, search_value, blog):
    if tab == "tab-1":
        content = "text"
    elif tab == "tab-2":
        content = "simple"

    summeries_path = "data/data_warehouse/" + blog + "/summaries"
    summery_components = []

    articles = load_files(summeries_path)[:16]

    for article in articles:
        if search_value.lower() not in article["title"].lower():
            continue

        summery_component = dbc.Card(
            [
                dbc.CardHeader(html.H2(article["title"])),
                dbc.CardBody(
                    html.Div(
                        [
                            html.P(article[content]),
                            html.A("Read full article", href=article["link"], target="blank"),
                            html.P(article["date"]),
                        ]
                    )
                ),
            ],
            class_name="mb-3",
        )

        summery_components.append(summery_component)

    row_components = []

    for i in range(0, len(summery_components), 2):
        if i + 1 < len(summery_components):
            row = dbc.Row(
                [
                    dbc.Col(summery_components[i], width=6),
                    dbc.Col(summery_components[i + 1], width=6),
                ],
                class_name="mb-3",
            )
        else:
            row = dbc.Row(
                [dbc.Col(summery_components[i], width=6), dbc.Col(width=6)],
                class_name="mb-3",
            )

        row_components.append(row)

    return row_components


if __name__ == "__main__":
    app.run_server(debug=True)
