import pytest
class TestClass :
    @pytest.mark.sixth
    def test_LoginByEmail(self):
        print("test for Login by A ")
        assert 1==1
    @pytest.mark.second

    def test_LoginByFacebook(self):
        print(" this is login by B")
        assert True==True

    @pytest.mark.fourth
    def test_LoginByTwitter(self):
        print(" this is login by C")
        assert True==True

    @pytest.mark.third
    def test_SignupByEmail(self):
        print(" this is signup by D")
        assert True==True
    @pytest.mark.first
    def test_SignupByFacebook(self):
        print(" this is signup by E")
        assert True==True

    @pytest.mark.fifth
    def test_SignupByTwitter(self):
        print(" this is signup by F")
        assert True==True