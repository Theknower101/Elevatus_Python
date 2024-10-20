# login_page.py

import random
from seleniumbase import BaseCase

class Login:
    def __init__(self, test_case: BaseCase):
        self.test_case = test_case  # Store the test case instance

    def navigate_to_login_testing(self):
        # Use the selector string directly instead of a WebElement
        log_in_button_selector = "//small[@class='text-gray font-weight-400']"
        self.test_case.click(log_in_button_selector)  # Click using the selector string

    def fill_login_email_testing(self):
        emails = ["betusoftware@gmail.com"]  # Define your emails here or pass it in some way
        passwords = ["Ahmad1234567890@", "Omar123456789@", "Ali123456789@"]

        login_successfully = False

        while not login_successfully:
            try:


                # Generate random indices for email and password
                random_index_email = random.randint(0, len(emails) - 1)
                random_index_password = random.randint(0, len(passwords) - 1)

                # Wait for the email input to be visible and interact with it
                self.test_case.wait_for_element_visible("input[placeholder='Email']")
                self.test_case.clear("input[placeholder='Email']")  # Clear the email field
                self.test_case.type("input[placeholder='Email']", emails[random_index_email])  # Type the email

                # Wait for the password input to be visible and interact with it
                self.test_case.wait_for_element_visible("input[placeholder='Password']")
                self.test_case.clear("input[placeholder='Password']")  # Clear the password field
                self.test_case.type("input[placeholder='Password']",
                                    passwords[random_index_password])  # Type the password

                # Optionally, if you need to click the submit button
                self.test_case.click("button[type='submit']")  # Click the submit button

                # Check for login error
                try:
                    self.test_case.wait_for_element_visible("//div[@class='react-toast-notifications__container css-q2061w']")
                except:
                    login_successfully = True

            except Exception as e:
                print(f"Exception encountered: {e}")







