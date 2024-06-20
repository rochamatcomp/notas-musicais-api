"""
Tests for app.
"""

from http import HTTPStatus


def test_root_must_respond_hello_message_as_html(client):
    response = client.get('/')

    message = """<html>
        <head>
            <title> Olá, Notas musicais!</title>
        </head>
        <body>
            <h1> Olá, Notas musicais! </h1>
        </body>
        </html>
    """

    assert response.status_code == HTTPStatus.OK
    assert response.text == message


def test_chord_must_respond_notes_degrees_as_json(client):
    response = client.get('/acorde/cm')

    chord = {'notas': ['C', 'D#', 'G'], 'graus': ['I', 'III-', 'V']}

    assert response.json() == chord
