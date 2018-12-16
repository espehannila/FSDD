# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
from layout import layout
import callback

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app         = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = layout.layout



callback.init(app)


if __name__ == '__main__':
    app.run_server(debug=True)