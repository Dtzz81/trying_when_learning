import pytest
from source.fixture import prepare_toy_box


# Create a fixture for the toy box
@pytest.fixture
def toy_box():
    return prepare_toy_box()  # Automatically call the function for the tests


def test_play_with_car(toy_box):

    assert "Car" in toy_box  # We check if the car is in the toy box


def test_play_with_doll(toy_box):
 #   toy_box = prepare_toy_box() removed cuz of fixture

    assert "Doll" in toy_box  # We check if the car is in the toy box
