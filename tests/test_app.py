"""
Tests for app.
"""

from http import HTTPStatus


def test_root_must_response_hello_message_as_html(client):
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
