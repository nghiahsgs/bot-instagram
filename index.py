from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import getpass
from time import sleep

class InstagramBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # prefs = {
        #     "profile.managed_default_content_settings.images": 2
        # }
        # chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            './chromedriver', chrome_options=chrome_options)

    def login_fb(self):
        self.driver.get('http://fb.com/login')
        email_ip = self.driver.find_element_by_css_selector('#email')
        email_ip.send_keys('nghiahsgs')
        
        password=getpass.getpass()
        pass_ip = self.driver.find_element_by_css_selector('#pass')
        pass_ip.send_keys(password)

        login_btn=self.driver.find_element_by_css_selector('#loginbutton')
        login_btn.click()

    def login_instagram(self):
        self.driver.get('https://www.instagram.com')
        btn_continue = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="button"]')))
        btn_continue.click()

        sleep(3)
        btn_not_now=self.driver.find_elements_by_css_selector('div[role="dialog"] button')[-1]
        btn_not_now.click()

        link_profile=self.driver.find_elements_by_css_selector('nav a')[3]
        link_profile.click()


    def get_list_followers(self):
        btn_list_followers = self.driver.find_elements_by_css_selector('ul li a')[
            0]
        btn_list_followers.click()

        sleep(10)

        len_list_row_elements=0
        while True:
            list_row_elements = self.driver.find_elements_by_css_selector(
                '.notranslate')
            if(len(list_row_elements) > len_list_row_elements):
                len_list_row_elements = len(list_row_elements)
            else:
                break
            print('len_list_row_elements', len_list_row_elements)
            sleep(3)
        
        
        
        self.list_followers=[e.text for e in list_row_elements]
        
    def get_list_following(self):
        #back to profile page
        link_profile = self.driver.find_elements_by_css_selector('nav a')[3]
        link_profile.click()
        sleep(10)

        btn_list_following = self.driver.find_elements_by_css_selector('ul li a')[
            1]
        btn_list_following.click()
        sleep(10)

        len_list_row_elements=0
        while(True):
            list_row_elements = self.driver.find_elements_by_css_selector('.notranslate')
            if(len(list_row_elements)>len_list_row_elements):
                len_list_row_elements=len(list_row_elements)
            else:
                break
            print('len_list_row_elements', len_list_row_elements)
            sleep(3)
                

        self.list_following = [e.text for e in list_row_elements]

    def un_follow(self,index):
        list_btn_following = self.driver.find_elements_by_css_selector('button[type="button"]')
        list_btn_following[index].click()
        sleep(5)

        input('kill')
        btn_unfollow = self.driver.find_element_by_css_selector('div[role="dialog"] button')
        btn_unfollow.click()
    
    def auto(self):
        self.login_fb()
        sleep(3)
        self.login_instagram()
        sleep(3)
        input('bam f12 de man hinh thu nho lai')
        self.get_list_followers()
        self.get_list_following()

        index=0
        for user in self.list_following:
            print('index', index)
            if user in self.list_followers:
                pass
            else:
                self.un_follow(index)
            index += 1
        
bot=InstagramBot()
bot.auto()


