//you need to pip install selenium
//and also download your preferred browser driver
//my source https://medium.com/@dawran6/twitter-scraper-tutorial-with-python-requests-beautifulsoup-and-selenium-part-2-b38d849b07fe#.ddh6g4mwd

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
base_url = u'https://twitter.com/search?q='
query = u'%23beyhive&src=typd'
url = base_url + query
browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(40):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    
tweets = browser.find_elements_by_class_name('tweet-text')

for tweet in tweets:
    print(tweet.text)
    
driver.quit()
