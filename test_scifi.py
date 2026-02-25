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
    line={"color": "darkred"},
    hoverinfo="skip",
    name="Pareto front",
)

max_lmd = df_line["lmd"].max()
slope = 1111400 / (1334796 + 80000 + 100000 + 120000)

fig.add_scatter(
    x=[0, max_lmd],
    y=[0, max_lmd * slope],
    mode="lines",
    line={"color": "gray", "dash": "dot"},
    hoverinfo="skip",
    name="Max 6-star + 1x mod3",
)

# fig.add_shape(
#     type="line",
#     x0=0,
#     y0=0,
#     x1=max_lmd,
#     y1=max_lmd * slope_min,
#     line={
#         "color": "gray",
#         "dash": "dot",
#     },
# )

# fig.add_shape(
#     type="line",
#     x0=0,
#     y0=0,
#     x1=max_lmd,
#     y1=max_lmd * slope_max,
#     line={
#         "color": "gray",
#         "dash": "dot",
#     },
# )

fig.update_layout(
    title="Proof of concept (Scifi calcs, low-end)",
    xaxis_title="LMD/day",
    yaxis_title="EXP/day",
    legend_title=None,
)

fig.update_traces(
    textposition="top right",
    marker={"size": 10},
)
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
fig.write_html("docs/test_scifi.html")
