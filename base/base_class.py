from datetime import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver


    '''Method get current url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url ' + get_url)

    '''Method assert word'''

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Correct value word')

    '''Method Screenshot'''

    def save_screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('/Users/wowkeans/PycharmProjects/PythonStrunkiru/screenshots/' + name_screenshot)

    '''Method assert url'''

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Correct value url')
