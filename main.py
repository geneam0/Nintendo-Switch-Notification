import os
import time
import requests
import selenium
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getStock(url):
    PATH = "/Users/genelam/Downloads/chromedriver"
    with webdriver.Chrome(PATH) as driver:
        try:
            driver.get(url)
            buttons=driver.find_element_by_tag_name('button')
            time.sleep(10)
        finally:
            driver.quit()
    '''
    # http_respone 200 means OK status
    if resp.status_code == 200:
        print("Successfully opened the web page")
        # we need a parser,Python built-in HTML parser is enough .
        soup = BeautifulSoup(resp.text, 'html.parser')
        # l is the list which contains all the text i.e news
        container = soup.find_all("div",{"data-test":"FAOldVsNew_new"})
        print(container[0].innerText)

        # now we want to print only the text part of the anchor.
        # find all the elements of a, i.e anchor
    else:
        print("Error, unable to connect to webpage")
    '''

def notification():
    getStock('https://www.gamestop.com/video-games/switch/consoles/products/nintendo-switch-with-neon-blue-and-neon-red-joy-con/11095819.html?rt=productDetailsRedesign&utm_expid=.Hn2ODSotSjW4yWszOrBF7Q.1&utm_referrer=https%3A%2F%2Fwww.gamestop.com%2Fsearch%2F%3Fq%3Dnintendo%252Bswitch%26lang%3Ddefault%26rule%3Dbest-matches')
    getStock('https://www.target.com/p/animal-crossing-new-horizons-8211-nintendo-switch/-/A-76780148')
    getStock('https://www.target.com/p/nintendo-switch-with-neon-blue-and-neon-red-joy-con/-/A-77464001?clkid=a786bdcdNbe8311ea81b742010a246e0e&lnm=81938&afid=NeuIntel%2C%20LLC&ref=tgt_adv_xasd0002')
    getStock('https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255')
    while True:
        '''
        if (gamestopHasGame):
            os.system('osascript send.scpt {} "{}"'.format(7188134058, "Gamestop has the switch"))
        if (targetHasGame):
            os.system('osascript send.scpt {} "{}"'.format(7188134058, "Target has the switch"))
        if (bbHasGame):
            os.system('osascript send.scpt {} "{}"'.format(7188134058, "Best Buy has the switch"))
        '''
        time.sleep(30)
notification()
