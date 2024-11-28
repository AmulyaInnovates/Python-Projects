from selenium import webdriver
from bs4 import BeautifulSoup

# set up the web driver
driver = webdriver.Chrome()

# navigate to Amazon's website
driver.get("https://www.wikipedia.org/")

# get the page source
page_source = driver.page_source

# parse the page source using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# print the page title
print(soup.title)

 