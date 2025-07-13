from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup")
class BaseTest:

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "taj" + time_stamp + "@gmail.com"

    # def pytest_runtest_makereport(item, call):
    #     # Execute all other hooks to get the report object
    #     outcome = yield
    #     rep = outcome.get_result()
    #
    #     # Only take screenshot for failed tests
    #     if rep.when == "call" and rep.failed:
    #         # Get the class instance (where 'self.driver' is stored)
    #         driver = getattr(item.instance, "driver", None)
    #         if driver is not None:
    #             file_name = f"screenshots/{item.name}.png"
    #             driver.save_screenshot(file_name)
