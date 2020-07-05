import os
import time
import requests
from bs4 import BeautifulSoup

def getStock(url):
    # open with GET method
    resp = requests.get(url)

    # http_respone 200 means OK status
    if resp.status_code == 200:
        print("Successfully opened the web page")
        # we need a parser,Python built-in HTML parser is enough .
        soup = BeautifulSoup(resp.text, 'html.parser')

        # l is the list which contains all the text i.e news
        # l = soup.find("ul", {"class": "searchNews"})

        # now we want to print only the text part of the anchor.
        # find all the elements of a, i.e anchor
        #for i in l.findAll("a"):
         #   print(i.text)
    else:
        print("Error, unable to connect to webpage")

def notification():
    getStock('https://www.gamestop.com/video-games/switch/consoles/products/nintendo-switch-with-neon-blue-and-neon-red-joy-con/11095819.html?rt=productDetailsRedesign&utm_expid=.Hn2ODSotSjW4yWszOrBF7Q.1&utm_referrer=https%3A%2F%2Fwww.gamestop.com%2Fsearch%2F%3Fq%3Dnintendo%252Bswitch%26lang%3Ddefault%26rule%3Dbest-matches')
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
