# UI Automaton
Automation testing framework (UI) - an example. Based on Python, Selenium, Pytest

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/Stan575/uidemotest/blob/master/LICENSE)
[![Tests](https://github.com/Stan575/uidemotest/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Stan575/uidemotest/actions/workflows/ci.yml)
[![Code Quality](https://img.shields.io/badge/code%20quality-A-brightgreen)]()

## Requirements
Python 3.10.\*/3.11.\*, Pytest 7.1.2, <br>
Selenium 4.1.5 <br>
WebDriverManager 3.7.0 <br>

## Project structure
```text
-- uidemotest
   |-- .gitattributes
   |-- .gitignore
   |-- LICENSE
   |-- README.md
   |-- requirements.txt
   |-- .github
       `-- workflows
           `-- ci.yml
   |-- uidemotest
       |-- src
       `-- test
```

## How to prepare environment
1) Install [Python](https://www.python.org/downloads/) 3.10.* /3.11.*
2) Create [virtual environment](https://docs.python.org/3/library/venv.html)
3) Clone or copy (download) the repository into your virtual environment
4) Activate virtual environment, move to `uidemotest` root folder, and execute command `pip install -r requirements.txt`

## How to run tests
1) Open terminal window
2) Move to virtual environment folder
3) Activate virtual environment
4) Move to `uidemotest` root folder
5) Execute 
    - all tests: `pytest -v -s`
    - smoke test suite: `pytest -m smoke -v -s`
    - smoke and regression test suites: `pytest -m "smoke or regression" -v -s`
    - all tests except slow tests: `pytest -m "not slow" -v -s`

## Technology stack and helpful info
- [x] [Python](https://docs.python.org/3.10/)
- [x] [Selenium](https://www.selenium.dev/documentation/)
- [x] [Pytest](https://docs.pytest.org/en/7.1.x/contents.html)
- [x] [Chrome](https://www.google.com/chrome/downloads/)
- [x] [ChromeDriver](https://chromedriver.chromium.org/downloads)
- [x] [Webdriver Manager for Python](https://pypi.org/project/webdriver-manager/) <br>
