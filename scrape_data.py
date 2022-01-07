from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import os

import requests
import time


class DartVersion:
    def __init__(self):
        
        self.response = ""
        self.delay = 1
        
        DART_URL = 'https://dart.dev/get-dart/archive'

        # Instantiate options
        opts = Options()

        # Set chrome.exe path
        opts.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        opts.add_argument('--headless')
        opts.add_argument('--disable-dev-shm-usage')
        opts.add_argument('--no-sandbox')
    
        

        # Set the location of the webdriver
        chrome_driver = os.environ.get("CHROMEDRIVER_PATH")

        # Instantiate a webdriver
        driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)

        # Load the HTML pages
        driver.get(DART_URL)

        # Wait for the page to load
        time.sleep(self.delay)

        # Parse processed webpage with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, features="html.parser")

        # Get the latest stable version of dart
        dart_versions_table = soup.find(id="stable")
        dart_versions_table_body = dart_versions_table.find("tbody")
        dart_body_rows = dart_versions_table_body.find_all("tr")
        dart_body_row_content = dart_body_rows[0].find_all("td")
        content_version_info = dart_body_row_content[0].text

        latest_stable_dart_version = dart_body_rows[0].text
        # print("Content version: " + content_version_info)
        # print("Latest stable Dart SDK version:" + latest_stable_dart_version)
        self.response += "Latest stable Dart SDK version: " + latest_stable_dart_version + "\n"
        for row in dart_body_rows:
            self.response += row.text + "\n"

        driver.quit()
        
    def get_response(self):
        return self.response

    def set_delay(self, delay):

        self.delay = delay


class FlutterVersion:

    def __init__(self):
        self.response = ""

        self.delay = 1

        FLUTTER_URL = 'https://docs.flutter.dev/development/tools/sdk/releases'

        # Instantiate options

        opts = Options()

        # Set chrome.exe path

        opts.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        opts.add_argument('--headless')
        opts.add_argument('--disable-dev-shm-usage')
        opts.add_argument('--no-sandbox')

        # Set the location of the webdriver

        chrome_driver = os.environ.get("CHROMEDRIVER_PATH")

        # Instantiate a webdriver

        driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)

        # Load the HTML pages

        driver.get(FLUTTER_URL)

        # Wait for the page to load

        time.sleep(self.delay)

        # Parse processed webpage with BeautifulSoup

        soup = BeautifulSoup(driver.page_source, features="html.parser")

        # Get the latest stable version of flutter

        flutter_versions_table = soup.find(id="downloads-windows-stable")

        flutter_versions_table_body = flutter_versions_table.find("tbody")

        flutter_body_rows = flutter_versions_table_body.find_all("tr")

        latest_versions = []

        for i in range(0, 10):

            latest_versions.append(flutter_body_rows[i].find_all("td")[0].text)

        #latest_stable_flutter_version = flutter_body_rows[0].find("td").text

        #print("Latest stable Flutter SDK version:" + latest_stable_flutter_version)

        self.response += "Recent 10 versions of Flutter SDK:\n"

        for version in latest_versions:

            self.response += version + "\n"

        self.response += "\nLatest version of Flutter SDK: " + latest_versions[0]

        driver.quit()

    def get_response(self):
        return self.response

    def set_delay(self, delay):
        self.delay = delay


