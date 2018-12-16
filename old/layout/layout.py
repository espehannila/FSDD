# -*- coding: utf-8 -*-
import dash_html_components as html

from .header import header
from .footer import footer
from .content import content


layout  = html.Div(children=[
   header,
   content,
   footer
])