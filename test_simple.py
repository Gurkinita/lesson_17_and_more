

@allure.step('Test first')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Test assert')
@allure.description('my description')
def test_1():
    print('My first test')
    assert 1==1
