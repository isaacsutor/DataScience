import datetime
import pandas_datareader.data as web
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
ticker = "TSLA"
df = web.DataReader(ticker, 'yahoo', start, end)
df.reset_index(inplace=True)

df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

print(df.head())

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Stock Graph!
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': ticker},
            ],
            'layout': {
                'title': ticker
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)




