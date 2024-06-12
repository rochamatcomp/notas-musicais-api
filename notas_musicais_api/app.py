"""
API para [Notas musicais](https://github.com/dunossauro/notas-musicais),
para ajudar na formação de escalas, acordes e campos harmônicos.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_root():
    return {'message': 'Olá, Notas musicais!'}
