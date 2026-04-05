import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

df = px.data.tips()

plot = go.Figure(data=[go.Scatter(
    x=df['day'],
    y=df['tip'],
    mode='markers',)
])

plot.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="left",
            buttons=list([
                dict(
                    args=["type", "scatter"],
                    label="Scatter Plot",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Bar Chart",
                    method="restyle"
                )
            ]),
        ),
    ]
)

plot.show()