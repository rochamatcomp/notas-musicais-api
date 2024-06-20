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


def test_semitone_must_respond_matching_note(client):
    response = client.get('/semitom/c/-1')

    semitone = 'B'

    assert response.json() == semitone


def test_triad_must_respond_matching_notes_tone(client):
    response = client.get('/triade/c/menor')

    triad = ['C', 'D#', 'G']

    assert response.json() == triad


def test_scale_must_respond_notes_degrees_as_json(client):
    response = client.get('/escala/a/menor')

    scale = {
        'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }

    assert response.json() == scale
