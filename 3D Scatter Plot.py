import plotly.express as px

df = px.data.tips()

fig = px.scatter_3d(df, x="total_bill", y="sex", z="tip", color='day', 
                    size='total_bill', symbol='time')

fig.show()