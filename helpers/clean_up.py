from os import remove, listdir, rmdir, path
from loguru import logger

class CleanUp:

    # Removing temp files from previous run
    @staticmethod
    def clean_dir(dir_name):
        for a in listdir(path=dir_name):
            if a == ".keep":
                pass
            else:
                remove(dir_name + "/" + a)

    def remove_allure_report_before_run(self):
        try:
            # self.clean_dir("allure-report/history")
            # rmdir("allure-report/history")
            self.clean_dir("allure-report")
            logger.info("Allure data removed")
        except Exception as e:
            logger.error(f"Error on delete allure report: {e}")

    # Clean needed dir, all_dir = []
    def clean_up(self, all_dirs):
        for directory in all_dirs:
            self.clean_dir(directory)

    # Clean everything in directory
    def clean_all(self, all_dirs):
        for directory in all_dirs:
            for undef in listdir(path=directory):
                if path.isdir(directory + "/" + undef):
                    self.clean_all([directory + "/" + undef])
                else:
                    remove(directory + "/" + undef)
            rmdir(directory)
