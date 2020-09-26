import pytest,allure

class Test_lll:
    
    @allure.step(title="first test.")
    # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_001(self):
        allure.attach("This is .txt file","contain")
        assert 1
    # @pytest.issue('http://www.163.com')
    # @pytest.allure.testcase('http://www.baidu.com/test_al001')

    def test_002(self):
        allure.attach("This is .txt file","contain")
        assert 0