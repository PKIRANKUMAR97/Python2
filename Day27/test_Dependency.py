import pytest

class TestClassApp:

    @pytest.mark.dependency()
    def test_OpenApp(self):
        assert True==True

    @pytest.mark.dependency(depends=['TestClassApp::test_OpenApp'])
    def test_Login(self):
        assert True==True

    @pytest.mark.dependency(depends=['TestClassApp::test_Login'])
    def test_search(self):
        assert True==False

    @pytest.mark.dependency(depends=['TestClassApp::test_Login', 'TestClassApp::test_search'])
    def test_advancedSearch(self):
        assert True==True

    @pytest.mark.dependency(depends=['TestClassApp::test_Login'])
    def test_logout(self):
        assert True==True
