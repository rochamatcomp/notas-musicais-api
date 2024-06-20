"""
API para [Notas musicais](https://github.com/dunossauro/notas-musicais),
para ajudar na formação de escalas, acordes e campos harmônicos.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from notas_musicais import acordes

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


@app.get('/acorde/{cipher}')
def get_chord(cipher: str) -> dict[str, list[str]]:
    """
    Gera as notas de um acorde partindo de uma cifra.

    Args:
        cipher (str): Um acorde em forma de cifra.

    Returns:
        dict[str, list[str]]: Um dicionário com as notas e
            os graus correpondes a escala.
    """
    return acordes.acorde(cipher)
