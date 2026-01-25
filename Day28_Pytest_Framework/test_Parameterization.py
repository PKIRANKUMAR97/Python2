import pytest
class TestClassParameterization:
    @pytest.mark.parametrize('num1,num2',[(1,1),(5,7),(6,6),(9,0)])
    def test_Calculation(self,num1,num2):
        assert num1 == num2