import re
from bs4 import BeautifulSoup #静的コンテンツ専用
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from pymongo import MongoClient


# SR/SSRポケモン

if __name__ == "__main__":


    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    client = MongoClient('mongodb://localhost:27017')
    db = client.pokemon_card


    try:
        srpokemon_url = "https://www.tcgacademy.com/product-group/43/0/photo?division=17&num=100&sort=price-desc&page=1"

        while True:

            driver.get(srpokemon_url)
            soup = BeautifulSoup(driver.page_source, "lxml")
            collection = db.tcgacademy

            for cardlist in soup.select("#main_container > article > div > div.page_contents.clearfix.grouplist_contents > div > div.itemlist_box.clearfix"):
                for cards in cardlist.find_all(class_="item_data"):
                    names = cards.find(class_ = "goods_name").get_text()
                    prices = cards.find(class_ = "price").get_text()
                    stocks = cards.find(class_= "stock").get_text()

                    name = names.split('[')
                    model_num = name[1].replace("PKM_","").replace("]","").split('_')
                    model = model_num[0]
                    if "s" != model[0]:
                        model = "pro"

                    fractions = model_num[len(model_num) - 1].split('/')
                    numerator = fractions[0]



                    rarity = fractions[1]
                    if rarity == "28":
                        rarity = "P"
                    elif "SSR" in rarity:
                        rarity = "SSR"
                    elif "SR" in rarity:
                        rarity = "SR"
                    elif "SM-P" in rarity:
                        rarity = "P"


                    poke_name = name[0]

                    price = prices.replace("\n", "").replace(",", "").replace("円", "").replace("(税込)", "")

                    if stocks == "在庫なし":
                        stock = 0
                    else:
                        stock = stocks.replace("在庫数 ","").replace("点","")



                    insert_data = {
                        "model": model,
                        "numerator" : numerator,
                        "rarity" : rarity,
                        "name": poke_name,
                        "price": int(price),
                        "stock": int(stock)
                    }
                    collection.insert_one(insert_data)
                    print(insert_data)


            for next in soup.find_all(class_="to_next_page pager_btn"):
                next_urls = next.get("href")
                next_url = "https://www.tcgacademy.com/" + next_urls

            if next_url == srpokemon_url:
                break
            else:
                srpokemon_url = next_url




    except Exception as e :
        print("エラーが発生しました:" +str(e))

    finally:
        driver.close()
        driver.quit()


#　SRサポート
if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    client = MongoClient('mongodb://localhost:27017')
    db = client.pokemon_card
    try:
        srsupport_url = "https://www.tcgacademy.com/product-group/219/0/photo?division=17&num=100&sort=price-desc"

        while True:

            driver.get(srsupport_url)
            soup = BeautifulSoup(driver.page_source, "lxml")
            collection = db.fullahead

            for cardlist in soup.select("#main_container > article > div > div.page_contents.clearfix.grouplist_contents > div > div.itemlist_box.clearfix"):
                for cards in cardlist.find_all(class_="item_data"):
                    names = cards.find(class_ = "goods_name").get_text()
                    prices = cards.find(class_="price").get_text()
                    stocks = cards.find(class_= "stock").get_text()

                    price = prices.replace("\n", "").replace(",", "").replace("円", "").replace("(税込)", "")

                    name = names.split('[')
                    model_num = name[1].replace("PKM_", "").replace("]", "").split('_')

                    model = model_num[0]
                    if "s" != model[0]:
                        model = "pro"

                    fractions = model_num[len(model_num) - 1].split('/')
                    numerator = fractions[0]

                    rarity = fractions[1]

                    if "SSR" in rarity:
                        rarity = "SSR"
                    elif "SR" in rarity:
                        rarity = "SR"
                    elif "P" in rarity:
                        rarity = "P"


                    if stocks == "在庫なし":
                        stock = 0
                    else:
                        stock = stocks.replace("在庫数 ","").replace("点","")


                    sup_name = name[0]

                    insert_data = {
                        "model": model,
                        "numerator" : numerator,
                        "rarity" : rarity,
                        "name": sup_name,
                        "price": int(price),
                        "stock": int(stock)
                    }
                    collection.insert_one(insert_data)
                    print(insert_data)

            for next in soup.find_all(class_="to_next_page pager_btn"):
                next_urls = next.get("href")
                next_url = "https://www.tcgacademy.com/" + next_urls

            if next_url == srsupport_url:
                break
            else:
                srsupport_url = next_url






    except Exception as e :
        print("エラーが発生しました:" +str(e))

    finally:
        driver.close()
        driver.quit()






# UR カード　
if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    client = MongoClient('mongodb://localhost:27017')
    db = client.pokemon_card
    try:
        urcard_url = "https://www.tcgacademy.com/product-group/44?division=17&num=100&sort=price-desc"

        while True:

            driver.get(urcard_url)
            soup = BeautifulSoup(driver.page_source, "lxml")
            collection = db.fullahead

            for cardlist in soup.select("#main_container > article > div > div.page_contents.clearfix.grouplist_contents > div > div.itemlist_box.clearfix"):
                for cards in cardlist.find_all(class_="item_data"):
                    names = cards.find(class_ = "goods_name").get_text()
                    prices = cards.find(class_="price").get_text()
                    stocks = cards.find(class_= "stock").get_text()

                    price = prices.replace("\n", "").replace(",", "").replace("円", "").replace("(税込)", "")

                    name = names.split('[')
                    model_num = name[1].replace("PKM_", "").replace("]", "").split('_')

                    model = model_num[0]
                    if "s" != model[0]:
                        model = "pro"
                    elif model == "sm5M76/66UR":
                        model = "sm5M"

                    fractions = model_num[len(model_num) - 1].split('/')
                    numerator = fractions[0]
                    if numerator == "sm5M76":
                        numerator = "76"


                    rarity = fractions[1]
                    if "UR" in rarity:
                        rarity = "UR"
                    elif "P" in rarity:
                        rarity = "P"


                    if stocks == "在庫なし":
                        stock = 0
                    else:
                        stock = stocks.replace("在庫数 ","").replace("点","")


                    urname = name[0]

                    insert_data = {
                        "model": model,
                        "numerator" : numerator,
                        "rarity" : rarity,
                        "name": urname,
                        "price": int(price),
                        "stock": int(stock)
                    }
                    collection.insert_one(insert_data)
                    print(insert_data)

            for next in soup.find_all(class_="to_next_page pager_btn"):
                next_urls = next.get("href")
                next_url = "https://www.tcgacademy.com/" + next_urls

            if next_url ==  urcard_url:
                break
            else:
                urcard_url = next_url



    except Exception as e :
        print("エラーが発生しました:" +str(e))

    finally:
        driver.close()
        driver.quit()





# HRサポート
if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    client = MongoClient('mongodb://localhost:27017')
    db = client.pokemon_card



    try:

        hrsupport_url = "https://www.tcgacademy.com/product-group/248?division=17&num=100&sort=price-desc"

        while True:

            driver.get(hrsupport_url)
            soup = BeautifulSoup(driver.page_source, "lxml")
            collection = db.fullahead

            for cardlist in soup.select("#main_container > article > div > div.page_contents.clearfix.grouplist_contents > div > div.itemlist_box.clearfix"):
                for cards in cardlist.find_all(class_="item_data"):
                    names = cards.find(class_ = "goods_name").get_text()
                    prices = cards.find(class_="price").get_text()
                    stocks = cards.find(class_= "stock").get_text()

                    price = prices.replace("\n", "").replace(",", "").replace("円", "").replace("(税込)", "")

                    name = names.split('[')
                    model_num = name[1].replace("PKM_", "").replace("]", "").split('_')

                    model = model_num[0]
                    if "s" != model[0]:
                        model = "pro"

                    fractions = model_num[len(model_num) - 1].split('/')
                    numerator = fractions[0]



                    rarity = fractions[1]
                    if "HR" in rarity:
                        rarity = "HR"
                    elif "P" in rarity:
                        rarity = "P"


                    if stocks == "在庫なし":
                        stock = 0
                    else:
                        stock = stocks.replace("在庫数 ","").replace("点","")


                    urname = name[0]

                    insert_data = {
                        "model": model,
                        "numerator" : numerator,
                        "rarity" : rarity,
                        "name": urname,
                        "price": int(price),
                        "stock": int(stock)
                    }
                    collection.insert_one(insert_data)
                    print(insert_data)


            break


    except Exception as e :
        print("エラーが発生しました:" +str(e))

    finally:
        driver.close()
        driver.quit()













# スペシャルアート
if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    client = MongoClient('mongodb://localhost:27017')
    db = client.pokemon_card



    try:

        specialart_url = "https://www.tcgacademy.com/product-group/220?division=17&num=100&sort=price-desc"

        while True:

            driver.get(specialart_url)
            soup = BeautifulSoup(driver.page_source, "lxml")
            collection = db.fullahead

            for cardlist in soup.select("#main_container > article > div > div.page_contents.clearfix.grouplist_contents > div > div.itemlist_box.clearfix"):
                for cards in cardlist.find_all(class_="item_data"):
                    names = cards.find(class_ = "goods_name").get_text()
                    prices = cards.find(class_="price").get_text()
                    stocks = cards.find(class_= "stock").get_text()

                    price = prices.replace("\n", "").replace(",", "").replace("円", "").replace("(税込)", "")

                    name = names.split('[')


                    model_num = name[1].replace("PKM_", "").replace("]", "").split('_')

                    model = model_num[0]
                    if "s" != model[0]:
                        model = "pro"

                    fractions = model_num[len(model_num) - 1].split('/')
                    numerator = fractions[0]



                    rarity = fractions[1]
                    if "HR" in rarity:
                        rarity = "HR"
                    elif "SR" in rarity:
                        rarity = "SR"
                    elif "P" in rarity:
                        rarity = "P"


                    if stocks == "在庫なし":
                        stock = 0
                    else:
                        stock = stocks.replace("在庫数 ","").replace("点","")


                    spname = name[0].replace("【スペシャルアートSA】", "")

                    insert_data = {
                        "model": model,
                        "numerator" : numerator,
                        "rarity" : rarity,
                        "name": spname,
                        "price": int(price),
                        "stock": int(stock)
                    }
                    collection.insert_one(insert_data)
                    print(insert_data)

            for next in soup.find_all(class_="to_next_page pager_btn"):
                next_urls = next.get("href")
                next_url = "https://www.tcgacademy.com/" + next_urls

            if next_url == specialart_url:
                break
            else:
                specialart_url = next_url


    except Exception as e :
        print("エラーが発生しました:" +str(e))

    finally:
        driver.close()
        driver.quit()







#   HRポケモン
if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    client = MongoClient('mongodb://localhost:27017')
    db = client.pokemon_card



    try:

        hrpokemon_url = "https://www.tcgacademy.com/product-group/249?division=17&num=100&sort=price-desc"

        while True:

            driver.get(hrpokemon_url)
            soup = BeautifulSoup(driver.page_source, "lxml")
            collection = db.fullahead

            for cardlist in soup.select("#main_container > article > div > div.page_contents.clearfix.grouplist_contents > div > div.itemlist_box.clearfix"):
                for cards in cardlist.find_all(class_="item_data"):
                    names = cards.find(class_ = "goods_name").get_text()
                    prices = cards.find(class_="price").get_text()
                    stocks = cards.find(class_= "stock").get_text()

                    price = prices.replace("\n", "").replace(",", "").replace("円", "").replace("(税込)", "")

                    name = names.split('[')


                    model_num = name[1].replace("PKM_", "").replace("]", "").split('_')

                    model = model_num[0]
                    if "s" != model[0]:
                        model = "pro"

                    fractions = model_num[len(model_num) - 1].split('/')
                    numerator = fractions[0]



                    rarity = fractions[1]
                    if "HR" in rarity:
                        rarity = "HR"
                    elif "P" in rarity:
                        rarity = "P"


                    if stocks == "在庫なし":
                        stock = 0
                    else:
                        stock = stocks.replace("在庫数 ","").replace("点","")


                    hrpokename = name[0]

                    insert_data = {
                        "model": model,
                        "numerator" : numerator,
                        "rarity" : rarity,
                        "name": hrpokename,
                        "price": int(price),
                        "stock": int(stock)
                    }
                    collection.insert_one(insert_data)
                    print(insert_data)
            break




    except Exception as e :
        print("エラーが発生しました:" +str(e))

    finally:
        driver.close()
        driver.quit()