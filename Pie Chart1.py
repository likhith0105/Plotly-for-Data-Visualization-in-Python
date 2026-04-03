import plotly.express as px

df = px.data.tips()

fig = px.pie(df, values="total_bill", names="day")
fig.show()