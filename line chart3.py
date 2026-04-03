import plotly.express as px

df = px.data.iris()

fig = px.line(df, y="sepal_width", line_dash='species',
              color='species')

fig.show()