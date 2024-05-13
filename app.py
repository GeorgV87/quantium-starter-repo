from dash import Dash, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_csv("sales_pink_morsels.csv")
df_sorted_by_date = df.sort_values("date")


app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

title = dcc.Markdown(children="# Pink Morsel Sales")
graph = dcc.Graph(figure={})
radio = dcc.RadioItems(
    [
        {
            "label": "all",
            "value": "all",
        },
        {
            "label": "north",
            "value": "north",
        },
        {
            "label": "east",
            "value": "east",
        },
        {
            "label": "south",
            "value": "south",
        },
        {
            "label": "west",
            "value": "west",
        },
    ],
    "all",
    inline=True,
    labelStyle={
        "display": "inline",
        "font-weight": "bold",
        "font-size": 20,
        "padding-right": 15,
    },
    inputStyle={"margin-right": 5},
)

app.layout = dbc.Container([title, graph, radio])


@callback(
    Output(graph, component_property="figure"), Input(radio, component_property="value")
)
def update_graph(user_input):
    if user_input == "all":
        fig = px.line(df_sorted_by_date, x="date", y="sales", title="Overall Sales")

    else:
        fig = px.line(
            df_sorted_by_date.loc[df_sorted_by_date["region"].str.contains(user_input)],
            x="date",
            y="sales",
            title=f"Sales Region {user_input}",
        )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
