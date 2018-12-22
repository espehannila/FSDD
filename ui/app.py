# -*- coding: utf-8 -*-
from dash import Dash
from layout import layout

external_stylesheets        = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Create applicaton
app                         = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout                  = layout.layout


#if __name__ == '__main__':
 #   app.run_server(debug=True)