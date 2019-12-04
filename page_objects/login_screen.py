from allure import step
from page_objects.base_screen import BaseScreen


class LoginScreen(BaseScreen):

    def __init__(self, driver, screens):
        self.driver = driver
        self.screens = screens
        BaseScreen.__init__(self, self.driver)

    def username_text_filed(self):
        return self.driver.find_element_by_id("username")

    def password_text_filed(self):
        return self.driver.find_element_by_id("password")

    def login_button(self):
        return self.driver.find_element_by_id("log-in")

    def all_icons(self):
        return self.driver.find_element_by_class_name("buttons-w").find_elements_by_tag_name("a")

    def checkbox(self):
        return self.driver.find_element_by_class_name("form-check-input")

    @step("Type in {1} in {0} field")
    def type_in(self, field, text):
        self.username_text_filed().clear()
        self.password_text_filed().clear()
        if field:
            fields = {
                "username": self.username_text_filed(),
                "password": self.password_text_filed(),
            }
            fields.get(field).click()
            fields.get(field).send_keys(text)
            return self
        return self

    @step("Type in username and password")
    def type_in_username_and_password(self, user, password):
        self.username_text_filed().clear()
        self.password_text_filed().clear()
        self.username_text_filed().send_keys(user)
        self.password_text_filed().send_keys(password)
        return self

    def tap_on_login_button(self):
        self.login_button().click()
        return self.screens

    @step("Verify Checkbox")
    def verify_checkbox(self):
        self.checkbox().click()
        self.verify_object("templates/login_screen/checked.png")
        self.checkbox().click()
        self.verify_object("templates/login_screen/unchecked.png")

    @step("Verify Error")
    def verify_error(self, error_type):
        errors = {
            "username": "templates/login_screen/error_on_email_only.png",
            "password": "templates/login_screen/error_on_password_only.png",
            "both": "templates/login_screen/error_on_both.png"
        }
        self.verify_object(errors.get(error_type))

    @step("Verify icons")
    def check_that_icons_are_enabled(self):
        for icon in self.all_icons():
            assert icon.is_enabled(), "Icon is not clickable"
            assert icon.get_attribute("href") == "https://demo.applitools.com/hackathon.html#", \
                "Link for icon is incorrect"
