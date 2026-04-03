import plotly.express as px

df = px.data.tips()

fig = px.pie(df, values="total_bill", names="day",
             color_discrete_sequence=px.colors.sequential.RdBu,
             opacity=0.7, hole=0.5)
fig.show()