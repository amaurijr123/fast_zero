from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert (
        response.text
        == """<html>
        <head>
            <title> Olá Mundo </title>
        </head>
        <body>
            <h1> Olá Mundo! </h1>
        </body>
    </html>"""
    )  # Assert
