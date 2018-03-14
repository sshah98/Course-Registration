import time
import getpass

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class Registration(object):

    def __init__(self, login, password, secondpass):
        self.login = login
        self.password = password
        self.secondpass = secondpass

    def loginToAccount(self):
		
		baseurl = 'https://banweb.gwu.edu/PRODCartridge/twbkwbis.P_WWWLogin'
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-extensions")
        options.add_experimental_option("detach", True)
        mydriver = webdriver.Chrome(
            executable_path='chromedriver', chrome_options=options)
        mydriver.get(baseurl)

        mydriver.find_element_by_id("UserID").send_keys(self.login)
        mydriver.find_element_by_xpath(
            '//*[@id="PIN"]/input').send_keys(self.password)
        mydriver.find_element_by_xpath("//p//input[@type='submit']").click()

        mydriver.find_element_by_id('answer').send_keys(self.secondpass)

        mydriver.find_element_by_xpath("//p//input[@type='submit']").click()

        mydriver.get(
            'https://banweb.gwu.edu/PRODCartridge/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu')

        time.sleep(1)

        mydriver.get(
            'https://banweb.gwu.edu/PRODCartridge/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu')

        time.sleep(1)

        mydriver.find_element_by_link_text(
            'Register, Drop and/or Add Classes').click()

        time.sleep(4)

        print('Please click submit and wait while CRNS get populated')

        mydriver.find_element_by_id("crn_id1").send_keys(crn1)
        mydriver.send_keys(Keys.TAB)

        mydriver.find_element_by_id("crn_id2").send_keys(crn2)
        mydriver.send_keys(Keys.TAB)

        mydriver.find_element_by_id("crn_id3").send_keys(crn3)
        mydriver.send_keys(Keys.TAB)

        mydriver.find_element_by_id("crn_id4").send_keys(crn4)
        mydriver.send_keys(Keys.TAB)

        mydriver.find_element_by_id("crn_id5").send_keys(crn5)
        mydriver.send_keys(Keys.TAB)


crn1 = '111111'
crn2 = '222222'
crn3 = '333333'
crn4 = '444444'
crn5 = '555555'

myuser = input('Enter GWID: ')
mypass = getpass.getpass('Enter password: ')
mypass2 = getpass.getpass('Enter Second Password: ')

myobj = Registration(myuser, mypass, mypass2)
myobj.loginToAccount()
