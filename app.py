import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Load the sales data
data_path = r'data\daily_sales_data.csv'  
sales_data = pd.read_csv(data_path)

# Initialize the Dash app
app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Sales, Price, and Quantity Data Over Time',
            style={'textAlign': 'center', 'color': '#FFFFFF', 'fontFamily': 'Arial', 'marginTop': '20px', 'marginBottom': '20px'}),

    html.Div(children=[
        html.Label('Select a Region:', style={'color': '#FFFFFF', 'marginBottom': '10px', 'fontFamily': 'Arial'}),
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': 'All Regions', 'value': 'All'}] +
                    [{'label': i, 'value': i} for i in sales_data['region'].unique()],
            value='All',
            style={'color': '#000', 'marginBottom': '20px'}
        )
    ], style={'padding': '20px', 'border': '1px solid #FFFFFF', 'borderRadius': '5px', 'marginBottom': '20px', 'backgroundColor': '#333333'}),

    dcc.Graph(id='sales-price-graph'),
    dcc.Graph(id='sales-quantity-graph'),
], style={'fontFamily': 'Arial', 'padding': '20px', 'backgroundColor': '#121212', 'color': '#FFFFFF'})

@app.callback(
    [Output('sales-price-graph', 'figure'),
     Output('sales-quantity-graph', 'figure')],
    [Input('region-dropdown', 'value')]
)

def update_graph(selected_region):
    if selected_region == 'All':
        filtered_data = sales_data
    else:
        filtered_data = sales_data[sales_data['region'] == selected_region]
    

    aggregated_data = filtered_data.groupby('date').agg({'sales': 'sum', 'price': 'mean', 'quantity': 'sum'}).reset_index()

    # Sales and Price Graph
    sales_price_fig = go.Figure()


    sales_price_fig.add_trace(go.Scatter(x=aggregated_data['date'], y=aggregated_data['sales'],
                                         name='Sales', mode='lines+markers',
                                         line=dict(width=3, color='lightblue'), 
                                         marker=dict(color='lightblue', size=8)))

 
    sales_price_fig.add_trace(go.Scatter(x=aggregated_data['date'], y=aggregated_data['price'],
                                         name='Price', mode='lines+markers',
                                         line=dict(width=3, color='lightgreen', dash='dash'), 
                                         yaxis='y2', marker=dict(color='lightgreen', size=8)))

    sales_price_fig.update_layout(
        title=f'Sales and Price Over Time {"Across All Regions" if selected_region == "All" else "in " + selected_region}',
        xaxis_title='Date',
        yaxis_title='Sales',
        yaxis2=dict(
            title='Price',
            overlaying='y',
            side='right',
            showgrid=False,
        ),
        plot_bgcolor='#121212',
        paper_bgcolor='#121212',
        font=dict(color='white'),
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(0,0,0,0)')
    )

    # Sales and Quantity Graph
    sales_quantity_fig = go.Figure()

    sales_quantity_fig.add_trace(go.Scatter(x=aggregated_data['date'], y=aggregated_data['price'],
                                        name='Price', mode='lines+markers',
                                        line=dict(width=3, color='lightgreen', dash='dash'), 
                                        marker=dict(color='lightgreen', size=8)))


    # Refined quantity line
    sales_quantity_fig.add_trace(go.Scatter(x=aggregated_data['date'], y=aggregated_data['quantity'],
                                            name='Quantity', mode='lines+markers',
                                            line=dict(width=3, color='red', dash='solid'), 
                                            yaxis='y2', marker=dict(color='red', size=8)))

    sales_quantity_fig.update_layout(
        title=f'Sales and Quantity Over Time {"Across All Regions" if selected_region == "All" else "in " + selected_region}',
        xaxis_title='Date',
        yaxis_title='Sales',
        yaxis2=dict(
            title='Quantity',
            overlaying='y',
            side='right',
            showgrid=False,
        ),
        plot_bgcolor='#121212',
        paper_bgcolor='#121212',
        font=dict(color='white'),
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(0,0,0,0)')
    )

    return sales_price_fig, sales_quantity_fig

if __name__ == '__main__':
    app.run_server(debug=True)
