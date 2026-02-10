from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Make sure the path is correct
pink_morsels_data = pd.read_csv("data/pink_morsels_data.csv")

# Convert date to datetime and sort
pink_morsels_data['date'] = pd.to_datetime(pink_morsels_data['date'])
pink_morsels_data = pink_morsels_data.sort_values('date')

# Aggregate sales per day per region (optional if multiple rows per day)
df_plot = pink_morsels_data.groupby(['date', 'region'])['Sales'].sum().reset_index()

# Create line chart
fig = px.line(df_plot, x="date", y="Sales", color="region", markers=True)

# Dash app
app = Dash()
app.layout = html.Div(children=[
    html.H1("Pink Morsels Sales Over Time"),
    dcc.Graph(id='sales-line-graph', figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
