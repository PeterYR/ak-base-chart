import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"

df = pd.read_csv("test_scifi.csv")
df_points = df[df["category"] != "line"]
df_line = df[df["category"] == "line"]

fig = px.scatter(
    df_points,
    x="lmd",
    y="exp",
    text="setup",
    title="Proof of concept (Scifi calcs, low-end)",
    labels={"lmd": "LMD/day", "exp": "EXP/day"},
    hover_data={
        "lmd": True,
        "exp": True,
        "setup": True,
        "category": False,
    },
    color="category",
)

fig.add_scatter(
    x=df_line["lmd"],
    y=df_line["exp"],
    mode="lines",
    hoverinfo="skip",
    line={
        "color": "maroon",
        "width": 1,
    },
    showlegend=False,
)

fig.update_layout(
    title="Proof of concept (Scifi calcs, low-end)",
    xaxis_title="LMD/day",
    yaxis_title="EXP/day",
    legend_title="Base setup type",
)

fig.update_traces(textposition="top right")
fig.update_xaxes(
    rangemode="tozero",
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor="black",
)
fig.update_yaxes(
    rangemode="tozero",
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor="black",
)

fig.show()
fig.write_html("index.html")
