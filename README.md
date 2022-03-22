# aos

# Project info

## Purpose

To create automated test to test basic business critical functionality of an eCommerce web application Advantage Online Shopping.  
This project was given as capstone project and final phase of course for Software Quality and Test Automation during my studies at Canadian College of Technology and Business (CCTB).

**Video of all tests running**

https://user-images.githubusercontent.com/63124019/159391418-a2a527ca-f32e-4e1c-b1db-78bb0eb25edc.mp4



# Technology Stack

### Application Environment

(where tests are developed)
https://advantageonlineshopping.com/

- Localhost version can be installed and used as well
- Local host URL: http://localhost:8080/
- Local installation requires PosgreSQL database version 10 or up
- more details on local installation:
  https://advantageonlineshopping.com/#/version

### Automation Environment

(Tools, Technologies Used to develop automated tests)

- _IDE:_ PyCharm
- _Automation Framework:_ Selenium Webdriver
- _Language:_ Python 3.9
- _Browser:_ Chrome
- _Source Control:_ Git/GitHub
- _Data:_ Python Faker library, v 11.3

### Execution Environment

- Jenkins on AWS EC2 Linix instance with SSH-Key based secure connection to GitHub repository to pull and run the selenium scripts
- Local running the tests in PyCharm

### Project Structure

- `base_aos_test.py` base class that setup and teardown Selinium WebDriver that is used in aos_tests.py
- `aos_tests.py` all test cases
- `aos_methods.py` helper methods used in tests so we do not duplicate them, like _create_new_user_.
- `aos_locators.py` holds data used in tests

### Project Management

- Automated tests are developed based on Manual Test cases using Jira weekly Sprints
- Manual Test Cases are documented in Confluence and managed via Jira Tasks
