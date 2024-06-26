"""
API para [Notas musicais](https://github.com/dunossauro/notas-musicais),
para ajudar na formação de escalas, acordes e campos harmônicos.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from notas_musicais import acordes, campo_harmonico, escalas

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


@app.get('/semitom/{note}/{interval}')
def get_semitone(note: str, interval: int) -> str:
    """
    Calcula a distância em semitons para uma outra nota usando intervalos.

    Args:
        note (str): Uma nota qualquer.
        interval (int): Um intervalo em semitons.

    Returns:
        str: Uma nota correspondente ao intervalo.
    """
    return acordes.semitom(note, intervalo=interval)


@app.get('/triade/{note}/{tonality}')
def get_triad(note: str, tonality: str) -> list[str]:
    """
    Gera triades a partir de uma tônica e uma tonalidade.

    Args:
        note (str): Uma nota da qual se deseja obter um acorde.
        tonality (str): Tonalidade na qual será formado o acorde.

    Returns:
        list[str]: A tríade do acorde referente a nota e a tonalidade.
    """
    return acordes.triade(note, tonality)


@app.get('/escala/{tonic}/{tonality}')
def get_scale(tonic: str, tonality: str) -> dict[str, list[str]]:
    """
    Gera uma escala apartir de uma tônica e uma tonalidade.

    Args:
        tonic (str): Nota que será a tônica da escala.
        tonality (str): Tonalidade da escala.

    Returns:
        dict[str, list[str]]: Um dicionário com as notas da escala e os graus.
    """
    return escalas.escala(tonic, tonality)


@app.get('/campo_harmonico/{tonic}/{tonality}')
def get_harmonic_field(tonic: str, tonality: str) -> dict[str, list[str]]:
    """
    Gera um campo harmônico com base em um tônica e uma tonalidade.

    Args:
        tonic (str): Primeiro grau do campo harmônico.
        tonality (str): Tonalidade para o campo. Ex: maior, menor, etc...

    Returns:
        dict[str, list[str]]: Um campo harmônico com
            as notas da escala e os graus.
    """
    return campo_harmonico.campo_harmonico(tonic, tonality)
