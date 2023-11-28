# from dash import Dash, html, dcc, Input, Output  # pip install dash
# import plotly.express as px
# import dash_ag_grid as dag  # pip install dash-ag-grid
# import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
# import pandas as pd  # pip install pandas

# import matplotlib  # pip install matplotlib

# matplotlib.use("agg")
# import matplotlib.pyplot as plt
# import base64
# from io import BytesIO

# # df = pd.read_csv("1000_Sales_Records.csv")


# def create_app(df):
#     app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#     app.layout = dbc.Container(
#         [
#             html.H1(
#                 "Sales Data Insights - Demo",
#                 className="mb-2",
#                 style={"textAlign": "center"},
#             ),
#             dbc.Row(
#                 [
#                     dbc.Col(
#                         [
#                             dcc.Dropdown(
#                                 id="category",
#                                 value="Item Type",
#                                 clearable=False,
#                                 options=df.columns[1:],
#                             )
#                         ],
#                         width=4,
#                     )
#                 ]
#             ),
#             dbc.Row([dbc.Col([html.Img(id="bar-graph-matplotlib")], width="100%")]),
#             dbc.Row(
#                 [
#                     dbc.Col(
#                         [dcc.Graph(id="bar-graph-plotly", figure={})],
#                         width="100%",
#                         md=6,
#                     ),
#                 ],
#                 className="mt-4",
#             ),
#             dbc.Col(
#                 [
#                     dag.AgGrid(
#                         id="grid",
#                         rowData=df.to_dict("records"),
#                         columnDefs=[{"field": i} for i in df.columns],
#                         columnSize="sizeToFit",
#                     )
#                 ],
#                 width="100%",
#                 md=6,
#                 className="mt-4 w-full",
#             ),
#         ]
#     )

#     # Create interactivity between dropdown component and graph
#     @app.callback(
#         Output(component_id="bar-graph-matplotlib", component_property="src"),
#         Output("bar-graph-plotly", "figure"),
#         Output("grid", "defaultColDef"),
#         Input("category", "value"),
#     )
#     def plot_data(selected_yaxis):
#         # Build the matplotlib figure
#         fig = plt.figure(figsize=(20, 5))
#         plt.bar(df["Country"], df[selected_yaxis])
#         plt.ylabel(selected_yaxis)
#         plt.xticks(rotation=30)

#         # Save it to a temporary buffer.
#         buf = BytesIO()
#         fig.savefig(buf, format="png")
#         # Embed the result in the html output.
#         fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
#         fig_bar_matplotlib = f"data:image/png;base64,{fig_data}"

#         # Build the Plotly figure
#         fig_bar_plotly = px.bar(df, x="Country", y=selected_yaxis).update_xaxes(
#             tickangle=330
#         )

#         my_cellStyle = {
#             "styleConditions": [
#                 {
#                     "condition": f"params.colDef.field == '{selected_yaxis}'",
#                     "style": {"backgroundColor": "#d3d3d3"},
#                 },
#                 {
#                     "condition": f"params.colDef.field != '{selected_yaxis}'",
#                     "style": {"color": "black"},
#                 },
#             ]
#         }
#     return app
#     return fig_bar_matplotlib, fig_bar_plotly, {'cellStyle': my_cellStyle}


# if __name__ == "__main__":
#     df = pd.read_csv("1000_Sales_Records.csv")
#     app = create_app(df)
#     app.run_server(debug=False, port=8002, host="0.0.0.0")
from dash import Dash, html, dcc, Input, Output  # pip install dash
import plotly.express as px
import dash_ag_grid as dag  # pip install dash-ag-grid
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import pandas as pd  # pip install pandas

import matplotlib  # pip install matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def create_app(df):
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dbc.Container(
        [
            html.H1(
                "Sales Data Insights - Demo",
                className="mb-2",
                style={"textAlign": "center"},
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Dropdown(
                                id="category",
                                value=df.columns[1],  # Default value set to the second column name
                                clearable=False,
                                options=[{'label': col, 'value': col} for col in df.columns[1:]],  # Options need to be in {'label': , 'value': } format
                            )
                        ],
                        width=4,
                    )
                ]
            ),
            dbc.Row([dbc.Col([html.Img(id="bar-graph-matplotlib")], width="100%")]),
            dbc.Row(
                [
                    dbc.Col(
                        [dcc.Graph(id="bar-graph-plotly", figure={})],
                        width="100%",
                        md=6,
                    ),
                ],
                className="mt-4",
            ),
            dbc.Col(
                [
                    dag.AgGrid(
                        id="grid",
                        rowData=df.to_dict("records"),
                        columnDefs=[{"field": i} for i in df.columns],
                        columnSize="sizeToFit",
                    )
                ],
                width="100%",
                md=6,
                className="mt-4 w-full",
            ),
        ]
    )

    # Create interactivity between dropdown component and graph
    @app.callback(
        Output(component_id="bar-graph-matplotlib", component_property="src"),
        Output("bar-graph-plotly", "figure"),
        Output("grid", "defaultColDef"),
        Input("category", "value"),
    )
    def plot_data(selected_yaxis):
        # Build the matplotlib figure
        fig = plt.figure(figsize=(20, 5))
        plt.bar(df["Country"], df[selected_yaxis])
        plt.ylabel(selected_yaxis)
        plt.xticks(rotation=30)

        # Save it to a temporary buffer.
        buf = BytesIO()
        fig.savefig(buf, format="png")
        # Embed the result in the html output.
        fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
        fig_bar_matplotlib = f"data:image/png;base64,{fig_data}"

        # Build the Plotly figure
        fig_bar_plotly = px.bar(df, x="Country", y=selected_yaxis).update_xaxes(
            tickangle=330
        )

        my_cellStyle = {
            "styleConditions": [
                {
                    "condition": f"params.colDef.field == '{selected_yaxis}'",
                    "style": {"backgroundColor": "#d3d3d3"},
                },
                {
                    "condition": f"params.colDef.field != '{selected_yaxis}'",
                    "style": {"color": "black"},
                },
            ]
        }
        # Return statements should be inside the callback function
        return fig_bar_matplotlib, fig_bar_plotly, {'cellStyle': my_cellStyle}

    # The app is returned after defining the callback
    return app


if __name__ == "__main__":
    df = pd.read_csv("1000_Sales_Records.csv")
    app = create_app(df)
    app.run_server(debug=True, port=8002, host="0.0.0.0")
