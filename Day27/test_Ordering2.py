import pytest
class TestClass :
    @pytest.mark.run(order=2)
    def test_LoginByEmail(self):
        print("test for Login by A ")
        assert 1==1

    @pytest.mark.run(order=1)
    def test_LoginByFacebook(self):
        print(" this is login by B")
        assert True==True

    @pytest.mark.run(order=6)
    def test_LoginByTwitter(self):
        print(" this is login by C")
        assert True==True

    @pytest.mark.run(order=4)
    def test_SignupByEmail(self):
        print(" this is signup by D")
        assert True==True

    @pytest.mark.run(order=3)
    def test_SignupByFacebook(self):
        print(" this is signup by E")
        assert True==True

    @pytest.mark.run(order=5)
    def test_SignupByTwitter(self):
        print(" this is signup by F")
        assert True==True