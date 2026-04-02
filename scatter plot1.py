import plotly.express as px

df = px.data.tips()

fig = px.scatter(df, x='total_bill', y="tip", color='time',
                 symbol='sex', size='size', facet_row='day',
                 facet_col='time')

fig.show()