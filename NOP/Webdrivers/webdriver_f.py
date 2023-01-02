from selenium import webdriver


def all_webdrivers(Path):
    if Path == "Chrome":
        driver = webdriver.Chrome(
            executable_path="/Users/mac/apps/NOPEcommerce/NOP/Webdrivers/Drivers/chromedriver")
        return driver

    if Path == "Firefox":
        driver = webdriver.Chrome(
            executable_path="/Users/mac/apps/NOPEcommerce/NOP/Webdrivers/Drivers/geckodriver")
        return driver

    if Path == "Safari":
        driver = webdriver.Chrome(executable_path="")
        return driver
