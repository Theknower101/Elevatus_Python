# ElevatusTestCases.py

import seleniumbase
from Tests.login_page import Login
from Tests.sign_up_page import SignUpPage

class TestCases(seleniumbase.BaseCase):
    def test_sign_up_process(self):
        sign = SignUpPage(self)  # Pass self to SignUpPage if it also needs to access BaseCase methods
        log = Login(self)  # Pass self to Login

        self.open("https://mcitcareerssd.elevatus.io")  # Navigate to the specified URL
        self.maximize_window()  # Maximize the browser window

        sign.close_cookies_testing()
        sign.registration_button_testing()
        sign.fill_first_name_testing()
        sign.fill_last_name_testing()
        sign.fill_email_testing()
        sign.fill_information_testing()
        log.navigate_to_login_testing()  # This should now work without errors
        log.fill_login_email_testing()  # This should also work now















