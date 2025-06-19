import requests
from bs4 import BeautifulSoup
import time
from tkinter import *


def web_scrapper(url):
    """to get the price of the bitcoin """
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.content, features="html.parser")

        price = soup.find("span", class_="sc-65e7f566-0 esyGGG base-text")

        if price:
            p = price.get_text(strip=True)
            return p
        else:
            print("price not found")
    except EXCEPTION as error:
        print(f"got an error: {error}")


def refresh():
    """to run the function wi=eb_Scraper and to refresh the window after every 10 sec"""
    link = "https://coinmarketcap.com/currencies/bitcoin/"
    price_tag = web_scrapper(url=link)
    canvas.itemconfig(price_display, text=price_tag)
    print(f"Refreshed price at {time.strftime('%H:%M:%S')}")   # sometimes prices are same as they were
    # before 10 sec to have note of refresh So I added a note to stay updated
    window.after(10000, refresh)  # to refresh the price after every 10 seconds


# creating window price and label
window = Tk()
canvas = Canvas(width=270, height=225, bg="cyan")
price_label = canvas.create_text(135, 80, text="Bitcoin price", fill="white", font=("arial", 32, "bold"))
price_display = canvas.create_text(135, 130, text="Loading...", fill="white", font=("arial", 32, "bold"))
canvas.grid(row=0, column=0)
refresh()
window.mainloop()


