import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'},
            {'label': 'Krishna Deepak Reddy', 'value': 'KN'},
            {'label': 'Rens Ter Weijde', 'value':'RN'}
            ],
        value=['MTL', 'SF'],
        multi = True
        ),
    html.Label('Text Input'),
    dcc.Input(id='my-id', type='text'),
    html.Button('Submit', id='button'),

    html.Div(id='my-div')
    

    ], style={'columncount': 2})
@app.callback(
        Output(component_id='my-div', component_property='children'),
        [Input(component_id='my-id', component_property='value')]
        )
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)
