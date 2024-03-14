
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(8)

# navigate back to All section
all_link = driver.find_element("id", "nav-hamburger-menu")
all_link.click()
time.sleep(5)

# Selecting the "Best Sellers" option under the "All" category
best_sellers_option = driver.find_element("xpath", "/html/body/div[3]/div[2]/div/ul[1]/li[2]/a")
best_sellers_option.click()
time.sleep(7)

# Find and click on the first item under the Best Sellers section
first_item = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/ol/li[1]/div/div[2]/div/a[1]/div")
first_item.click()
time.sleep(5)

# Navigate to the "Frequently Bought Together" section
frequently_bought_together_link = driver.find_element("xpath", "/html/body/div[2]/div/div[5]/div[11]/div/div/div/div/div/div")
frequently_bought_together_link.click()
time.sleep(3)

# Adding the items to the cart
add_to_cart_button = driver.find_element("id", "AddToCartLibrary-AddToCartButton-Personalization")
add_to_cart_button.click()
time.sleep(5)

# Navigate to Go To Cart
go_to_cart_button = driver.find_element("xpath", "/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/span/span/a")
go_to_cart_button.click()
time.sleep(5)

# Navigate to Home Page
homepage_button = driver.find_element("id", "nav-logo-sprites")
homepage_button.click()
time.sleep(5)

# Clicking on the language selector dropdown
language_selector = driver.find_element("id", "icp-nav-flyout")
language_selector.click()
time.sleep(3)

# Navigating to Prime Video
prime_video = driver.find_element("id", "nav-link-amazonprime")
prime_video.click()
time.sleep(3)
free_trail = driver.find_element("xpath", "/html/body/div[1]/div/div/div[3]/div/div/div[2]/div[1]/div/form/span/span/input")
free_trail.click()
time.sleep(3)

driver.close()


