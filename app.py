# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, dash_table
import plotly.express as px
import pandas as pd
from python.documents import Corpus

# Load in all txt files from a folder containing your writing
path_to_writing_folder = "/Users/mbarry/Documents/03_hobbies/writing/prose/essays"
corpus = Corpus(path_to_writing_folder)

app = Dash(__name__)

colors = {
    "background": "#fae9bd",
    "text": "#7DBFF"
    
}

def generate_summary_table(corpus):
    
    return html.Table([
        html.Thead(
            html.Tr([html.Th('Total Documents'),
                     html.Th( "Word Count")
                ]
            )
        ),
        html.Tbody([
            html.Tr([
                html.Td(corpus.document_count),
               html.Td(corpus.word_count)
            ])
        ])
    ])

app.layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
    html.H1(children='Writing Analysis Dashboard',
            style={"textAlign": "center"}
    ),
    html.Div(children='''
        A dashboard to help writers better understand the patterns of their language.''', 
        style={"textAlign": "center"}
    ),
    generate_summary_table(corpus)
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)