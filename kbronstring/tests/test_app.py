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

def test_square(client):
    answer = client.get("square_number?number=2")
    assert b"Square of 2.0 is 4.0" == answer.data

def test_hello_world(client):
    answer = client.get("/")
    assert re.match(b".* on host .*", answer.data)

def test_empty_input(client):
    answer = client.get("")
    assert 'Empty Input'== answer.data

def not_numeric(client):
    answer = client.get("square_number?number=a")
    assert b"Not a numerical value" == answer.data

def test_other_square(client):
    answer = client.get("square_number?number=3")
    assert b"Square of 3.0 is 9.0" == answer.data
