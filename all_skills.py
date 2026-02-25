import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"

df = pd.read_csv("all_skills.csv")
df_points = df[df["category"] != "line"]
df_line = df[df["category"] == "line"]

fig = px.scatter(
    df_points,
    x="lmd",
    y="exp",
    text="setup",
    title="All base skills (up to Ato)",
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


fig.update_layout(
    title="All base skills (up to Ato)",
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
fig.write_html("docs/all_skills.html")
