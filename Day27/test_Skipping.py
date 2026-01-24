import pytest
class TestClass :
    def test_LoginByEmail(self):
        print("test for Login by Email ")
        assert 1==1

    def test_LoginByFacebook(self):
        print(" this is login by Facedbook")
        assert True==True
    def test_LoginByTwitter(self):
        print(" this is login by Twitter")
        assert True==True
    @pytest.mark.skip
    def test_SignupByEmail(self):
        print(" this is signup by email")
        assert True==True
    @pytest.mark.skip
    def test_SignupByFacebook(self):
        print(" this is signup by Facedbook")
        assert True==True
    @pytest.mark.skip
    def test_SignupByTwitter(self):
        print(" this is signup by Twitter")
        assert True==True