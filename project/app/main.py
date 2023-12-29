import asyncio
from configuration import ConfigurationManager
from login import LoginPage
from home import HomePage
from setup import Setup

async def main():
    config_manager = ConfigurationManager()
    driver = config_manager.get_driver_and_open_web()

    login_page = LoginPage(driver)
    login_page.login_to_account()

    home_page = HomePage(driver)
    home_page.navigate_home()

    setup = Setup(driver)
    setup.data_set()
    await setup.announcement_iteration()

if __name__ == "__main__":
    asyncio.run(main())
