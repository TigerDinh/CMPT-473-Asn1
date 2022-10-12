import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from e1utils import construct_headless_chrome_driver, get_landing_page_url, wait_for_page_load


def test_nonsecret_scenario():
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
	driver.get(get_landing_page_url())

	# Scenario 1
	givenName = "Bobby"
	givenFood = "Pineapple"
	driver.find_element("id","preferredname").send_keys(givenName)
	driver.find_element("id","food").send_keys(givenFood)
	driver.find_element("id", "secret").send_keys("Open Sesame")
	driver.find_element("id", "submit").click()
 
 
	# Checking if redirected to response.html
	try:
		driver.find_element("id","thankname")
	except NoSuchElementException:
		print("Redirect to response.html failed\n")
  
	assert driver.find_element("id","thankname"), givenName
	assert driver.find_element("id","foodploy"), givenFood
 
	try:
		driver.find_element("id","secretButton")
	except NoSuchElementException:
		print("Working as intended!\n")
 
	wait_for_page_load(driver)
	driver.close()

def test_secret_scenario_magic():
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
	driver.get(get_landing_page_url())

 
	# Scenario 2
	givenName = "Bobby"
	givenFood = "Pineapple"
	givenSecret = "magic"
	driver.find_element("id","preferredname").send_keys(givenName)
	driver.find_element("id","food").send_keys(givenFood)
	driver.find_element("id", "secret").send_keys(givenSecret)
	driver.find_element("id", "submit").click()

	# Checking if redirected to response.html
	try:
		driver.find_element("id","thankname")
	except NoSuchElementException:
		print("Redirect to response.html failed\n")
		return
  
	assert driver.find_element("id","thankname"), givenName
	assert driver.find_element("id","foodploy"), givenFood
 
	try:
		driver.find_element("id","secretButton").click()
	except NoSuchElementException:
		print("Secret button failed to exist\n")
		return

	# Checking if redirected to secret.html
	assert driver.title, "SECRET Simple Web Page"
	assert driver.find_element("id","thankname"), givenName
 
	wait_for_page_load(driver)
	driver.close()

