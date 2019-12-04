import pytest

from helpers.templates_dicoverer import TemplatesDiscoverer

login_templates = TemplatesDiscoverer("templates/login_screen")


class TestLoginPage:

    # @pytest.mark.parametrize("element_to_verify", login_templates.get_all_templates())
    # def test_verify_login_screen_ui(self, set_up, element_to_verify):
    #     set_up.screens.login_screen.verify_object(element_to_verify)

    # def test_icons(self, set_up):
    #     set_up.screens.login_screen.check_that_icons_are_enabled()
    #
    # def test_checkbox(self, set_up):
    #     set_up.screens.login_screen.verify_checkbox()

    # @pytest.mark.parametrize("field, text, error", [("username", "test", "username"),
    #                                                 ("password", "test", "password"),
    #                                                 ("", "", "both")])
    # def test_verify_error_on_login(self, set_up, field, text, error):
    #     set_up.screens.login_screen.type_in(field, text).tap_on_login_button().verify_error(error)

    def test_login_with_valid_data(self, set_up):
        set_up.screens.login_screen\
            .type_in_username_and_password("test", "test")\
            .tap_on_login_button()
        set_up.screens.main_screen\
            .verify_that_wew_are_on_main_screen()
