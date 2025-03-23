from selenium import webdriver

driver = webdriver.Chrome()  # または webdriver.Firefox(), webdriver.Edge() など
driver.get("https://www.google.com/")
driver.quit()