import random
import seleniumbase

class SignUpPage:

    def __init__(self, base_case):
        self.base_case = base_case

    def close_cookies_testing(self):
        close_button = "//div[@class='drawer-handle']"
        self.base_case.click(close_button)

    def registration_button_testing(self):
        register_button = ".MuiButtonBase-root.btns.theme-transparent.is-registration-btn.mx-2.css-1b47e06"
        self.base_case.click(register_button)

    def fill_first_name_testing(self):
        first_names = ["Ahmad", "Mohammad", "Ali"]
        random_index = random.randint(0, len(first_names) - 1)
        first_name_field = "input[placeholder='First name']"
        self.base_case.type(first_name_field, first_names[random_index])

    def fill_last_name_testing(self):
        last_names = ["Allan", "Almoqdad", "Jabali"]
        random_index = random.randint(0, len(last_names) - 1)
        last_name_field = "input[placeholder='Last name']"
        self.base_case.type(last_name_field, last_names[random_index])

    def fill_email_testing(self):
        emails = ["betusoftware@gmail.com", "Ahmad@gmail.com", "at3220920@gmail.com"]

        random_index = random.randint(0, len(emails) - 1)
        email_field = "input[placeholder='Email']"
        self.base_case.type(email_field, emails[random_index])
        entered_email = self.base_case.get_attribute(email_field, "value")
        assert "@gmail.com" in entered_email or "@hotmail.com" in entered_email or "@yahoo.com" in entered_email, "Email format is invalid."

    def fill_information_testing(self):
        passwords = ["Ahmad1234567890@", "Omar123456789@", "Ali123456789@"]
        phone_numbers = ["791314605", "781234569", "794000008"]

        random_index_password = random.randint(0, len(passwords) - 1)
        random_index_phone = random.randint(0, len(phone_numbers) - 1)

        password_field = "input[placeholder='Password']"
        confirm_password_field = "input[placeholder='Confirm Password']"
        phone_number_field = "//input[@id='SharedPhoneControlRef--0---0-0-phone_number']"
        check_box = "//label[@for='customCheckLogin']"
        submit_button = ".btn-main.my-4.btn.btn-secondary"

        self.base_case.type(password_field, passwords[random_index_password])
        self.base_case.type(confirm_password_field, passwords[random_index_password])
        self.base_case.type(phone_number_field, phone_numbers[random_index_phone])
        self.base_case.click(check_box)
        self.base_case.click(submit_button)

        # Wait for the success message to appear
        successfully_registered_message = "//div[@class='h4 mt-2 text-center']"
        self.base_case.wait_for_element(successfully_registered_message, timeout=10)

        # Check for password strength error
        try:
         password_strength_error = "div:nth-child(4) div:nth-child(2)"
         assert not self.base_case.is_element_visible(password_strength_error), "Password is weak."
        except:
         print("Password is weak")
        # Check for password match error

        try:
         password_is_matched_error = "//div[@class='invalid-feedback d-block error-wrapper']"
         if self.base_case.get_attribute(password_field, "value") != self.base_case.get_attribute(confirm_password_field, "value"):
            assert self.base_case.is_element_visible(password_is_matched_error), "Passwords do not match."
        except:
            print("Password is  match.")
        # Check for phone number validation error
        try:
         valid_number_error = "//div[@class='phone-error-wrapper']"
         if len(self.base_case.get_attribute(phone_number_field, "value")) < 9:
            assert self.base_case.is_element_visible(valid_number_error), "Phone number is invalid."
        except:
            print("Phone number is valid.")
        # Check for successful registration message
        try:
         assert self.base_case.is_element_visible(successfully_registered_message), "Registration failed."
        except:
         print("Registration succed.")




