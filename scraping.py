import requests
from urllib.request import urlretrieve
import os, time, sys
import re
from bs4 import BeautifulSoup

# 取得するURL
url = "https://seifukudoncky.com/shopbrand/ct6/"
pages = ['page1/order/','page2/order/','page3/order/','page4/order/','page5/order/', \
         'page6/order/','page7/order/','page8/order/','page9/order/','page10/order/']

#保存フォルダの指定
savedir = "uniform"

wait_time = 1

def main():
    for page in pages:
        response = requests.get(url + page)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text,'lxml')
        imgs = soup.find_all('img', src=re.compile('^https://shop33-makeshop.akamaized.net/shopimages/doncky/0'))
        time.sleep(wait_time)

        for img in imgs:
            img_urls = []
            img_urls.append(img.get('src'))
            img_urls = str(img_urls)[1:-2]
            img_copy = img_urls
            reg = re.compile("(.*)doncky/(.*)")
            mat = reg.match(img_urls)
            mat = mat.group(2)
            filepath = savedir + "/" + mat
            if os.path.exists(filepath): continue
            urlretrieve(img_copy[1:],filepath)

if __name__ == "__main__":
    main()
