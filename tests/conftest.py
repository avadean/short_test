import pytest


@pytest.fixture
def participants():
    return [
        {"age": 25, "height": 180},
        {"age": 30, "height": 170},
        {"age": 35, "height": 160},
        {"age": 38, "height": 165},
        {"age": 40, "height": 190},
        {"age": 45, "height": 200},
    ]