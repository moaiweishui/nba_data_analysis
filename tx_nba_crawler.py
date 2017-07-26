# coding=utf-8
import sys
import time

import requests
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf-8')

def sele2req_cookies(cookies):
    cookie_dict = dict()
    for cookie in cookies:
        cookie_dict[cookie['name']] = cookie['value']
    return cookie_dict

headers = {
        'user_agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
browser = webdriver.Chrome(chrome_options=options)
#browser = webdriver.PhantomJS()
#browser.set_window_size(800, 600)
browser.get('http://nba.stats.qq.com/stats/')
#print browser.page_source
print browser.title
browser.implicitly_wait(5)
# team
elem = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul/li[5]/a')
print browser.title
elem.click()
browser.implicitly_wait(5)
# warriors
elem = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/a/img')
elem.click()
print browser.title
print browser.current_url

print type(browser.current_window_handle)
window_list = browser.window_handles
window_set = set(window_list)
window_set.remove(browser.current_window_handle)
for window in window_set:
    browser.switch_to_window(window)
    time.sleep(2)

print browser.title
print browser.current_url

elem = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[4]/div[2]/ul/li[1]/a')
#elem.location_once_scrolled_into_view()
time.sleep(5)
elem.click()
elem = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[4]/div[2]/ul/li[2]/a')
elem.click()
left = '/html/body/div[5]/div[2]/div[4]/div[2]/div/div[1]/div/a[1]'
right = '/html/body/div[5]/div[2]/div[4]/div[2]/div/div[1]/div/a[2]'
#time.sleep(5)
#elem = browser.find_element_by_xpath(right)
time.sleep(5)
#elem.click()

for x in range(16):
    print x
    if x%2 == 0:
        elem = browser.find_element_by_xpath(right)
        print 'click right'
        elem.click()
    else:
        elem = browser.find_element_by_xpath(left)
        print 'click left'
        elem.click()
 









#browser.get('https://www.whoscored.com/')
#print 'aaa'
#cookies = browser.get_cookies()
#print cookies
#req_cookies = sele2req_cookies(cookies)
#r = requests.get('https://www.whoscored.com/', headers=headers, cookies=req_cookies)
#print r
#print r.text
#browser.quit()

'''
headers = {
        'user_agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        #'cookie':'visid_incap_774904=eQdO0IxkRsaEDBOs3tpO1ATcbFkAAAAAQUIPAAAAAACGqcF8ABwfbfW+of2MK+lU; incap_ses_406_774904=dFTYA0oRTkqKXCPr22iiBQTcbFkAAAAA0J38dtOJaY92OxaPNl5VOg==; _ga=GA1.2.758762943.1500306434; _gid=GA1.2.1470139774.1500306434',
        #'referer':'https://www.whoscored.com',
        #'host':'www.whoscored.com'
        }
url = 'https://nba.hupu.com/teams/warriors'
session = requests.session()
r = session.get(url, headers=headers)
#r = requests.get(url, headers=headers)
print r.text
'''


