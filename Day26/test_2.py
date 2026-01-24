import pytest

class TestClass:
    @pytest.fixture()       ## decorator
    def setup(self):
        print("Launching browser....")
        print("opening browsers....")

    def test_Login(self, setup):
        print("this is login test ")
    def test_Search(self, setup):
        print("this is search test ")
    def test_Advancedsearch(self, setup):
        print("this is advanced test ")