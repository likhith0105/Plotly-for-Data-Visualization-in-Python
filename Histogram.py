import plotly.express as px

df = px.data.tips()

fig = px.histogram(df, x="total_bill", color='sex',
                   nbins=50, histnorm='percent',
                   barmode='overlay')

fig.show()