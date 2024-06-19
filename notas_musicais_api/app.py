"""
API para [Notas musicais](https://github.com/dunossauro/notas-musicais),
para ajudar na formação de escalas, acordes e campos harmônicos.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def get_root():
    message = """<html>
        <head>
            <title> Olá, Notas musicais!</title>
        </head>
        <body>
            <h1> Olá, Notas musicais! </h1>
        </body>
        </html>
    """

    return message
