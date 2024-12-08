import requests
import os
from bs4 import BeautifulSoup
import threading
import time

if not os.path.exists("images/"):
    os.mkdir("images")

main_urls = []
urls = []
img_urls = []
downloaded_urls = []


def download_urls() -> None:
    global main_urls
    global urls
    web_url = "https://www.varzesh3.com/"
    try:
        while True:
            response = requests.get(web_url)
            print("A request has been sent to varzesh3.")
            if response.status_code != 200:
                print("Request failed!")
                continue
            soup = BeautifulSoup(response.content, "html.parser")
            news_list = soup.find_all("div", {"class": "news-main-list"})
            news_urls = [news_link["href"] for news in news_list for news_link in news.find_all("a") if
                         "video" not in news_link["href"] if "album" not in news_link["href"]]
            counter = 0
            for url in news_urls:
                if url not in main_urls:
                    print("urls list has been updated!")
                    counter += 1
                    main_urls.append(url)
                    urls.append(url)
            print(counter, "new news urls has been added to urls list.")
            time.sleep(10)
    except Exception as e:
        print("Error happened in download_links function: ", e)


def download_image(src: str) -> bool:
    try:
        ext = src.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[-1]
        name = src.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[0]
        img_response = requests.get(src.strip())
        if img_response.status_code != 200:
            return False
        content = img_response.content
        with open(n := "images/" + name + "." + ext, "wb") as file:
            file.write(content)
            print(f"image {name} has been downloaded!")
        return True
    except Exception as e:
        print("Error happened in download_image function: ", e)


def get_images_url() -> None:
    global downloaded_urls
    global img_urls
    global urls
    try:
        while True:
            if not urls:
                continue
            news_url = urls.pop(0)
            if news_url in downloaded_urls:
                continue
            web = requests.get(news_url)
            if web.status_code != 200:
                urls.append(news_url)
                continue
            soup = BeautifulSoup(web.content, "html.parser")
            images = soup.find_all("div", {"class": "news-main-image"})
            if images:
                download_img_status = download_image(images[0].find("img")["src"])
                if not download_img_status:
                    downloaded_urls.append(news_url)
    except Exception as e:
        print("Error happened in get_images_url function: ", e)


threads = []

th1 = threading.Thread(target=download_urls)
th1.start()
threads.append(th1)

th2 = threading.Thread(target=get_images_url())
th2.start()
threads.append(th2)

for thread in threads:
    thread.join()