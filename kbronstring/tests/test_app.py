import re

import pytest

from app.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_squareroot(client):
    answer = client.get("squareroot_number?number=4")
    assert b"Square Root of 4.0 is 2.0" == answer.data


def test_hello_world(client):
    answer = client.get("/")
    assert re.match(b".* on host .*", answer.data)
