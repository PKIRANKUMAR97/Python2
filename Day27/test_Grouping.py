import pytest
# GroupRegressionCheck
class TestClassGrouping:
    @pytest.mark.GroupSanityCheck
    def test_LoginByEmail(self):
        print(" this is login by email")
        assert True==True

    @pytest.mark.GroupSanityCheck
    def test_LoginByFacebook(self):
        print(" this is login by Facedbook")
        assert True==True

    @pytest.mark.GroupSanityCheck
    def test_LoginByTwitter(self):
        print(" this is login by Twitter")
        assert True==True

    @pytest.mark.GroupSanityCheck
    @pytest.mark.GroupRegressionCheck
    def test_SignupByEmail(self):
        print(" this is signup by email")
        assert True==True

    @pytest.mark.GroupRegressionCheck
    def test_SignupByFacebook(self):
        print(" this is signup by Facedbook")
        assert True==True

    @pytest.mark.GroupSanityCheck
    @pytest.mark.GroupRegressionCheck
    def test_SignupByTwitter(self):
        print(" this is signup by Twitter")
        assert True==True