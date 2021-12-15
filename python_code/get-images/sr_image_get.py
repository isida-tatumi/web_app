
import requests
import lxml
from bs4 import BeautifulSoup #静的コンテンツ専用
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import chromedriver_binary
import time
from pymongo import MongoClient
import pandas as pd

if __name__ == "__main__":

    urls = []
    for a in range(1,16):

        urls.append("https://www.pokemon-card.com/card-search/index.php?keyword=&se_ta=&regulation_sidebar_form=all&pg=&sc_rare_sr=1&illust=&sm_and_keyword=true&page=" + str(a))
        a += 1

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    try:
        x = 0
        while True:

            driver1 = driver.get(urls[x])
            time.sleep(5)
            driver.execute_script('javascript:void(0);')
            soup = BeautifulSoup(driver.page_source, "lxml")
            pages = soup.find_all('img')
            time.sleep(5)

            i = 0
            for page in pages:
                if page.get('data-src') is not None:
                    page_urs = page.get('data-src')
                    image_url = "https://www.pokemon-card.com/" + page_urs
                    path = "/home/vagrant/share/picture_data/" + str(x) + str(i) + ".jpg"
                    req = requests.get(image_url)
                    time.sleep(5)

                    if req.status_code == 200:
                        with open(path, 'wb') as file:
                            file.write(req.content)
                            print(str(x) +str(i) + "枚目保存成功:")
                            i += 1
            if x >=  16 :
                break
            else:
                x += 1



    except Exception as e :
        print("エラーが発生しました:" +str(e))

    finally:
        driver.close()
        driver.quit()

