
from bs4 import BeautifulSoup #静的コンテンツ専用
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from pymongo import MongoClient




# UR
if __name__ == "__main__":

    # 価格の低い順
    fullur_url = "https://pokemon-card-fullahead.com/shopbrand/rarity-ur/page2/price/"


    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    client = MongoClient('mongodb://localhost:27017')
    db = client.pokemon_card


    try:



         i = 0

         driver.get(fullur_url)
         soup = BeautifulSoup(driver.page_source, "lxml")
         collection = db.fullahead


         for cardlist in soup.select("#contents > div.indexItemBox.cf"):
            for cards in cardlist.find_all("div"):
                for names in cards.find_all(class_="itemName"):
                    card_data = names.get_text().split()

                    model_list = card_data[0].replace("【キズ格安】","").replace("PK-","").split("-")


                    print(model_list)


                    name = card_data[1]
                    if name == "ガラル":
                       name = card_data[1]+card_data[2]

                    rarity = card_data[2]

                    if "UR" != rarity:
                        rarity = "UR"








         # for next in soup.find_all(class_="next"):
         #     next_urla = next.find("a")
         #     next_url = next_urla.get("href")
         #     fullahead_url = "https://pokemon-card-fullahead.com" + next_url



    except Exception as e :
        print("エラーが発生しました:" +str(e))

    finally:
        driver.close()
        driver.quit()




