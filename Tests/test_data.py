import random
from seleniumbase import BaseCase


class TestData(BaseCase):
    passwords = ["Ahmad1234567890@", "Omar123456789@", "Ali123456789@"]
    url = "https://mcitcareerssd.elevatus.io"

    def setUp(self):
        self.open(self.url)
        self.maximize_window()
        self.rand = random.Random()





