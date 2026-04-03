import plotly.express as px

df = px.data.iris()

fig = px.line(df, y="sepal_width", line_group='species')

fig.show()