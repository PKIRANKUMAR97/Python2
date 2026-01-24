import pytest

@pytest.fixture()       ## decorator ## we will write all prerequisites
def setup():
    print("Launching browser....") # executes once before every test method
    print("opening browsers....")
    yield
    print("closing browsers....") # executes once after every test method