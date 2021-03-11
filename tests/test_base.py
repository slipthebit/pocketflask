# tests/test_base.py
import pytest
from pocket import app as flask_app

def test_root_route():
    response = flask_app.test_client().get('/')
    assert response.status_code == 200
    assert b"hello" in response.data
