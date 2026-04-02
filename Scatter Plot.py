import plotly.express as px

df = px.data.tips()

fig = px.scatter(df, x='total_bill', y="tip")

fig.show()