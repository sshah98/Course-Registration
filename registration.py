from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ChromeOptions, Chrome



baseurl = 'https://banweb.gwu.edu/PRODCartridge/twbkwbis.P_WWWLogin'

class Registration(object):

	def __init__(self, login, password, secondpass):
		self.login = login
		self.password = password
		self.secondpass = secondpass

	def loginToAccount(self):
		options = Options()
		options.add_argument('--disable-gpu')
		options.add_argument("--disable-extensions")
		options.add_experimental_option("detach", True)
		mydriver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options)
		# mydriver = webdriver.Firefox()
		mydriver.get(baseurl)

		# print("Logging in...")
		mydriver.find_element_by_id("UserID").send_keys(self.login)
		mydriver.find_element_by_xpath('//*[@id="PIN"]/input').send_keys(self.password)
		mydriver.find_element_by_xpath("//p//input[@type='submit']").click()



		mydriver.find_element_by_id('answer').send_keys(self.secondpass)

		mydriver.find_element_by_xpath("//p//input[@type='submit']").click()

		mydriver.get('https://banweb.gwu.edu/PRODCartridge/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu')

		# time.sleep(2)

		mydriver.get('https://banweb.gwu.edu/PRODCartridge/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu')

		mydriver.get('https://banweb.gwu.edu/PRODCartridge/bwskfreg.P_AddDropCrse')
		
		mydriver.find_element_by_xpath("//form//input[@type='submit']").click()

		


myuser = input('Enter GWID: ')
mypass = getpass.getpass('Enter password: ')
mypass2 = getpass.getpass('Enter Mothers Maiden Name: ')

myobj = Registration(myuser, mypass, mypass2)
myobj.loginToAccount()




# crn1 = driver.find_element_by_id("crn_id1")
# crn1.send_keys('351231')
# crn1.send_keys(Keys.TAB)

# crn2 = driver.find_element_by_id("crn_id2")
# crn2.send_keys('351231')
# crn2.send_keys(Keys.TAB)


# crn3 = driver.find_element_by_id("crn_id3")
# crn3.send_keys('351231')
# crn3.send_keys(Keys.TAB)

# crn4 = driver.find_element_by_id("crn_id4")
# crn4.send_keys('351231')
# crn4.send_keys(Keys.TAB)


# crn5 = driver.find_element_by_id("crn_id5")
# crn5.send_keys('351231')
# crn5.send_keys(Keys.TAB)
