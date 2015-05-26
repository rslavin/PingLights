import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
#driver.get("http://10.9.0.1/login")
driver.get("http://wlogin.userservices.net/wlogin.php")

def find_by_xpath(locator):
	element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, locator))
	)

	return element

class FormPage(object):
	def fill_form(self, data):
		#driver.find_element_by_xpath('//form[@name="login"]/input[@name = "username"]').send_keys(data['username'])
		#driver.find_element_by_xpath('//form[@name="login"]/input[@name = "password"]').send_keys(data['password'])
		find_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input').send_keys(data['username'])
		find_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/input').send_keys(data['password'])

		return self

	def submit(self):
		#find_by_xpath('//input[@value = "Submit"]').click()
		find_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/input').click()

data = {
		'username': 'slavin6142',
		'password': 'ZipLink13'
		}
try:
	FormPage().fill_form(data).submit()
except TimeoutException:
	driver.quit()
	sys.exit(0)
driver.quit()

