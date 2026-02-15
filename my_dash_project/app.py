from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from plotly.express import line
import pandas as pd

# Load and sort data
data = pd.read_csv("data/pink_morsels_data.csv")
data = data.sort_values(by="date")

# Initialize Dash
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    # Header
    html.H1(
        "Pink Morsel Visualizer",
        id="header",
        style={
            'textAlign': 'center',
            'color': '#E91E63',
            'font-family': 'Arial, sans-serif',
            'padding': '20px',
            'backgroundColor': '#f7f7f7',
            'borderRadius': '10px'
        }
    ),
    
    # Radio buttons to filter region
    html.Div([
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-picker',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True,
            style={'margin': '10px 0'}
        )
    ], style={'textAlign': 'center'}),
    
    # Graph
    dcc.Graph(
        id="visualization"
    )
])

# Callback to update graph based on region selection
@app.callback(
    Output('visualization', 'figure'),
    Input('region-picker', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_data = data
    else:
        filtered_data = data[data['region'].str.lower() == selected_region]
    
    fig = line(
        filtered_data,
        x="date",
        y="Sales",
        color='region',
        title=f"Pink Morsel Sales - {selected_region.capitalize()}"
    )
    fig.update_layout(template='plotly_white', title_x=0.5)
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
