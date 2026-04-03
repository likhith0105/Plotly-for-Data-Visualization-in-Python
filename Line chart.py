import plotly.express as px

df = px.data.iris()

fig = px.line(df, y="sepal_width",)

fig.show()


#Plotly for Data Visualization in Python