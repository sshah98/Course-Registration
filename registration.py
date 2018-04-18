import time
import getpass

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


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
        actions = ActionChains(mydriver)

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

        print('Please click submit and wait 5 seconds while CRNS get populated...')

        time.sleep(5)

        mydriver.find_element_by_id("crn_id1").send_keys(crn1)

        mydriver.find_element_by_id("crn_id2").send_keys(crn2)

        mydriver.find_element_by_id("crn_id3").send_keys(crn3)

        mydriver.find_element_by_id("crn_id4").send_keys(crn4)

        mydriver.find_element_by_id("crn_id5").send_keys(crn5)


crn1 = '24415'
crn2 = '22962'
crn3 = '24414'
crn4 = '24744'
crn5 = '22516'

myuser = input('Enter GWID: ')
mypass = getpass.getpass('Enter password: ')
mypass2 = getpass.getpass('Enter Second Password: ')

myobj = Registration(myuser, mypass, mypass2)
myobj.loginToAccount()
