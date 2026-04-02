import plotly.express as px

df = px.data.tips()

fig = px.violin(df, x="day", y="tip")

fig.show()