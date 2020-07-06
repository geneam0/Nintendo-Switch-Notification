import os
import time
import requests

def getStock(url):
    with requests.Session() as s:
        url = url
        time_between_checks = 5  # seconds

        page1 = s.get(url)
        time.sleep(time_between_checks)  # pause execution
        page2 = s.get(url)  # "new page" that will be compared against "old page"

        if page1.content != page2.content:
            print("Change detected")
            return True
        else:
            print(page1.content)
            print(page2.content)
            return False
        page1 = None
        page2 = None

def main():
    while True:
        gameStop=getStock('https://www.gamestop.com/video-games/switch/consoles/products/nintendo-switch-with-neon-blue-and-neon-red-joy-con/11095819.html?rt=productDetailsRedesign&utm_expid=.Hn2ODSotSjW4yWszOrBF7Q.1&utm_referrer=https%3A%2F%2Fwww.gamestop.com%2Fsearch%2F%3Fq%3Dnintendo%252Bswitch%26lang%3Ddefault%26rule%3Dbest-matches')
        target=getStock('https://www.target.com/p/nintendo-switch-with-neon-blue-and-neon-red-joy-con/-/A-77464001?clkid=a786bdcdNbe8311ea81b742010a246e0e&lnm=81938&afid=NeuIntel%2C%20LLC&ref=tgt_adv_xasd0002')
        bestbuy=getStock('https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255')
        if gameStop:
            #os.system('osascript send.scpt {} "{}"'.format(phone_number, "Gamestop has the switch"))
            print("Gamestop has the switch")
        if(target):
            #os.system('osascript send.scpt {} "{}"'.format(phone_number, "Target has the switch"))
            print("Target has the switch")
        if(bestbuy):
            #os.system('osascript send.scpt {} "{}"'.format(phone_number, "Best Buy has the switch"))
            print("Best Buy has the switch")
        time.sleep(60)

if __name__ == "__main__":
	main()