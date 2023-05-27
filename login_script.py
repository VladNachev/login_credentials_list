from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

def is_logged_in(driver):
    # Check if the user is logged in by examining the current URL
    # Return True if logged in, False otherwise
    return driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"

def save_to_file(content, file_path):
    with open(file_path, "a") as file:
        file.write(content + "\n")

chrome_options = Options()
chrome_options.add_argument("--remote-allow-origins=*")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Path to the CSV file
csv_file_path = "resources/credentials.csv"
output_file_path = "resources/output.txt"

# Clear the output file if it exists
if os.path.exists(output_file_path):
    with open(output_file_path, "w") as file:
        file.write("")

try:
    # Read the CSV file
    with open(csv_file_path, "r") as csv_file:
        lines = csv_file.readlines()
        for line in lines:
            credentials = line.strip().split(",")
            username = credentials[0]
            password = credentials[1]

            # Open the login page
            driver.get("https://practicetestautomation.com/practice-test-login/")

            # Find the username and password input fields
            username_input = driver.find_element(By.ID, "username")
            password_input = driver.find_element(By.ID, "password")

            # Enter the username and password
            username_input.send_keys(username)
            password_input.send_keys(password)

            # Find and submit the login button
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()

            # Check if login is successful
            if is_logged_in(driver):
                message = f"!!! ### !!! Login successful for username: {username} and password: {password}"
                print(message)
                save_to_file(message, output_file_path)
            else:
                message = f"Login failed for username: {username} and password: {password}"
                print(message)
                save_to_file(message, output_file_path)

except IOError as e:
    print(e)

# Close the browser
driver.quit()
