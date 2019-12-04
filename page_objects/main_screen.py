from allure import step
from page_objects.base_screen import BaseScreen


class MainScreen(BaseScreen):

    def __init__(self, driver, screens):
        self.driver = driver
        self.screens = screens
        BaseScreen.__init__(self, self.driver)

    @step("Verify Checkbox")
    def verify_that_wew_are_on_main_screen(self):
        self.verify_object("templates/main_screen/nav_bar_main.png")

