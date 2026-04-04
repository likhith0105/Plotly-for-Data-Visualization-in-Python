import plotly.express as px

df = px.data.tips()

fig = px.box(df, x="day", y="tip", color='sex',
             facet_row='time', boxmode='group',
             notched=True)

fig.show()