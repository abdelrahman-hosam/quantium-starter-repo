# Designing and architecting 100% human, coding 100% AI, testing and debugging 100% human


from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# -------------------------------------------------
# Load Data
# -------------------------------------------------

salesData = pd.read_csv("./data/PinkMorselSales.csv")

salesData["date"] = pd.to_datetime(salesData["date"])
salesData["year"] = salesData["date"].dt.year

pre_df = salesData[salesData["date"] <= "2021-01-15"]
post_df = salesData[salesData["date"] > "2021-01-15"]

# -------------------------------------------------
# Layout
# -------------------------------------------------

app.layout = html.Div(
    style={
        "width": "90%",
        "margin": "auto",
        "fontFamily": "Arial"
    },
    children=[

        html.H1("Quantium Sales Dashboard"),

        html.Hr(),

        html.Label("Mode"),

        dcc.RadioItems(
            id="mode",
            options=[
                {"label": "Compare", "value": "compare"},
                {"label": "View", "value": "view"},
            ],
            value="compare",
            inline=True
        ),

        html.Br(),

        html.Label("Region"),

        dcc.Dropdown(
            id="region",
            options=[
                {"label": "All", "value": "All"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="All",
            clearable=False
        ),

        html.Br(),

        html.Div(
            id="dataset-div",
            children=[

                html.Label("Dataset"),

                dcc.Dropdown(
                    id="dataset",
                    options=[
                        {"label": "Pre Raise", "value": "pre"},
                        {"label": "Post Raise", "value": "post"},
                    ],
                    value="pre",
                    clearable=False
                ),
            ]
        ),

        html.Br(),

        dcc.Graph(id="graph1"),

        dcc.Graph(id="graph2"),

        dcc.Graph(id="graph3")
    ]
)

# -------------------------------------------------
# Hide Dataset Dropdown
# -------------------------------------------------

@app.callback(
    Output("dataset-div", "style"),
    Input("mode", "value")
)
def hide_dataset(mode):

    if mode == "compare":
        return {"display": "none"}

    return {"display": "block"}


# -------------------------------------------------
# Update Graphs
# -------------------------------------------------

@app.callback(
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Output("graph3", "figure"),
    Input("mode", "value"),
    Input("region", "value"),
    Input("dataset", "value")
)
def update_graphs(mode, region, dataset):

    # ==================================================
    # COMPARE MODE
    # ==================================================

    if mode == "compare":

        pre = pre_df.copy()
        post = post_df.copy()

        if region != "All":
            pre = pre[pre["region"] == region]
            post = post[post["region"] == region]

        # -----------------------------
        # Graph 1 : Daily Sales
        # -----------------------------

        pre_daily = (
            pre.groupby("date")["sales"]
            .sum()
            .reset_index()
        )

        pre_daily["Period"] = "Pre Raise"

        post_daily = (
            post.groupby("date")["sales"]
            .sum()
            .reset_index()
        )

        post_daily["Period"] = "Post Raise"

        daily = pd.concat([pre_daily, post_daily])

        fig1 = px.line(
            daily,
            x="date",
            y="sales",
            color="Period",
            markers=True,
            title="Daily Sales Comparison",
            color_discrete_sequence=["#2563EB", "#DC2626"]
        )

        # -----------------------------
        # Graph 2 : Sales by Year
        # -----------------------------

        pre_year = (
            pre.groupby("year")["sales"]
            .sum()
            .reset_index()
        )

        pre_year["Period"] = "Pre Raise"

        post_year = (
            post.groupby("year")["sales"]
            .sum()
            .reset_index()
        )

        post_year["Period"] = "Post Raise"

        year_df = pd.concat([pre_year, post_year])

        fig2 = px.bar(
            year_df,
            x="year",
            y="sales",
            color="Period",
            barmode="group",
            title="Sales by Year",
            color_discrete_sequence=["#2563EB", "#DC2626"]
        )

        # -----------------------------
        # Graph 3 : Pie Chart
        # -----------------------------

        pie_df = year_df.copy()

        pie_df["Category"] = (
            pie_df["year"].astype(str)
            + " - "
            + pie_df["Period"]
        )

        fig3 = px.pie(
            pie_df,
            values="sales",
            names="Category",
            title="Sales Distribution by Year"
        )

        return fig1, fig2, fig3

    # ==================================================
    # VIEW MODE
    # ==================================================

    if dataset == "pre":
        df = pre_df.copy()
        title = "Pre Raise"

    else:
        df = post_df.copy()
        title = "Post Raise"

    if region != "All":
        df = df[df["region"] == region]

    # -----------------------------
    # Graph 1 : Daily Sales
    # -----------------------------

    daily = (
        df.groupby("date")["sales"]
        .sum()
        .reset_index()
    )

    fig1 = px.line(
        daily,
        x="date",
        y="sales",
        markers=True,
        title=f"{title} Daily Sales"
    )

    # -----------------------------
    # Graph 2 : Region Sales
    # -----------------------------

    region_sales = (
        df.groupby("region")["sales"]
        .sum()
        .reset_index()
    )

    fig2 = px.bar(
        region_sales,
        x="region",
        y="sales",
        color="region",
        title=f"{title} Sales by Region"
    )

    # -----------------------------
    # Graph 3 : Region Distribution
    # -----------------------------

    fig3 = px.pie(
        region_sales,
        names="region",
        values="sales",
        title=f"{title} Sales Distribution"
    )

    return fig1, fig2, fig3


# -------------------------------------------------
# Run
# -------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)