import csv
import requests

from bs4 import BeautifulSoup

class Product():
    def __init__(self,name,link, price, num):
        self.name = name
        self.link = link
        self.price = price 
        self.num = num

def parser(url):
    page = 1
    count_items = 0
    max_item = 175
    products_lst = []

    while max_item > count_items:
        res = requests.get(f"{url}&p={page}")
        soup = BeautifulSoup(res.text, "lxml")
        products = soup.find_all("div", class_="product-card")

        for product in products:
            if count_items >= max_item:
                break
            name = product.get("data-product-name")
            num = product.find("span", class_ = "product-card__key").text
            name_elem = product.find("meta", itemprop="name")
            link = name_elem.findNext().get("href")
            price_elem = product.find("span", itemprop="price")
            price = price_elem.get("content")
            products_lst.append(Product(name=name,
                                        link=link,
                                        price=price,
                                        num=num))
            count_items += 1
        page += 1
    
    return products_lst


def main():
    products_lst = parser(url = "https://glavsnab.net/otdelochnie-materiali/oboi/oboi-pod-pokrasku-1.html") 
    
    with open(f"parser_res.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "name",
            "link",
            "price",
            "num"
        ])
    
    with open(f"parser_res.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        for product in products_lst:
            writer.writerow([
                product.name,
                product.link,
                product.price,
                product.num
            ])


if __name__ == "__main__":
    main()
