import getpass
import selenium
from selenium import webdriver

# Open Facebook login page
browser = webdriver.Firefox()
browser.get("https://www.facebook.com/login/identify/?ctx=recover&unrecognized_tn=H1gY1WXZvZYQyGnJ")

# Enter email or phone number associated with the hacked account
email_or_phone = input("Enter the email or phone number associated with the hacked account: ")
browser.find_element_by_name("identify_email").send_keys(email_or_phone)

# Click the Continue button
browser.find_element_by_id("did_submit").click()

# Enter the new password
new_password = getpass.getpass("Enter a new password for the account: ")
browser.find_element_by_name("password_new").send_keys(new_password)

# Confirm the new password
confirm_new_password = getpass.getpass("Confirm the new password: ")
browser.find_element_by_name("password_new_confirm").send_keys(confirm_new_password)

# Click the Continue button
browser.find_element_by_id("did_submit").click()

# Recovery process completed, log out
browser.get("https://www.facebook.com/logout/")
browser.quit()
