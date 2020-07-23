import os
import time
from datetime import datetime
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

// TODO
phone_number=
PATH =

def getStock(store,url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(PATH,options=options)
    print("Checking "+store+" "+datetime.now().strftime("%H:%M:%S"))
    try:
        driver.get(url)
        time.sleep(30)
        if(store == "GameStop"):
            search = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[4]/div[7]/div[2]/div[1]/label/div/div[5]/span[2]")
            button_click = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[4]/div[5]/div[3]/div/div/div[2]/div/span").click()
            search2 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[4]/div[7]/div[2]/div[1]/label/div/div[5]/span[2]")
            if (search.text == "OUT OF STOCK" and search2.text == "OUT OF STOCK"):
                return False
        if(store == "Target"):
            search=driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[3]/div[1]/div/div[3]")
            if(search.text=="This item isn't eligible for shipping."):
                return False
        if (store == "BestBuy"):
            search = driver.find_element_by_xpath("/html/body/div[4]/main/div[1]/div[3]/div[2]/div/div/div[7]/div[1]/div")
            if(search.text=="Sold Out"):
                return False
        return True
    except selenium.common.exceptions.NoSuchElementException:
        print("No such element")
        return False
    except selenium.common.exceptions.ElementClickInterceptedException:
        return False
    finally:
        driver.close()
        driver.quit()

def main():
    Out_of_Stock = True
    while Out_of_Stock:
        gameStop_hasGame=getStock("GameStop",'https://www.gamestop.com/video-games/switch/consoles/products/nintendo-switch-with-neon-blue-and-neon-red-joy-con/11095819.html?rt=productDetailsRedesign&utm_expid=.h77-PyHtRYaskNpc14UbmA.1&utm_referrer=https%3A%2F%2Fwww.gamestop.com%2Fsearch%2F%3Fq%3Dnintendo%2Bswitch%26lang%3Ddefault')
        target_hasGame=getStock("Target",'https://www.target.com/p/nintendo-switch-with-neon-blue-and-neon-red-joy-con/-/A-77464001')
        bestbuy_hasGame=getStock("BestBuy",'https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255')
        if gameStop_hasGame:
            os.system('osascript send.scpt {} "{}"'.format(phone_number, "Gamestop has the switch"))
            print("Gamestop has the switch")
            Out_of_Stock=False
        if target_hasGame:
            os.system('osascript send.scpt {} "{}"'.format(phone_number, "Target has the switch"))
            print("Target has the switch")
            Out_of_Stock=False
        if bestbuy_hasGame:
            os.system('osascript send.scpt {} "{}"'.format(phone_number, "Best Buy has the switch"))
            print("Best Buy has the switch")
            Out_of_Stock=False
        time.sleep(60)

if __name__ == "__main__":
	main()