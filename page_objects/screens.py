from .login_screen import LoginScreen
from .main_screen import MainScreen


class Screen:

    def __init__(self, driver):
        self.driver = driver
        self.login_screen = LoginScreen(self.driver, self)
        self.main_screen = MainScreen(self.driver, self)
