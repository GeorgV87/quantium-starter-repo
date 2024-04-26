from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv("sales_pink_morsels.csv")
df_sorted_by_date = df.sort_values("date")


app = Dash(__name__)


app.layout = html.Div(
    [
        html.H1(children="Pink Morsel Sales", style={"textAlign": "center"}),
        dcc.Graph(
            figure=px.line(
                df_sorted_by_date,
                x="date",
                y="sales",
                color="region",
                title="Impact on sales after price increase on the\
                       15th of January, 2021",
            )
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
