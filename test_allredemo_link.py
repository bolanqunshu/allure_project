import allure


@allure.link("https://www.baidu.com",name="百度")
def test_with_link():
    print("这是一条加了测试链接的测试")
    pass

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_testcase_link():
    print("这是一跳测试用例的链接，链接到测试用还在里面")
    pass

# --allure-link-pattern=issue:https://www.mytesttracker.com/issue{}
@allure.issue('140', '这是一个issue')
def test_with_issue_link():
    pass