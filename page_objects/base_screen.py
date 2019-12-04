from helpers.python_eye import PythonEye
from allure import step


class BaseScreen:

    def __init__(self, driver):
        self.driver = driver
        self.python_eye = PythonEye(self.driver)

    @step("Verify {0} element")
    def verify_object(self, element):
        self.python_eye.verify_objects([element])

    @step("Verify {0} elements")
    def verify_objects(self, elements):
        self.python_eye.verify_objects(elements)
