#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 9 assingment part 2"""

from bs4 import BeautifulSoup
import json
import urllib2

url = 'https://www.nasdaq.com/symbol/aapl/historical'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")


def Stock_price():
    """This function will dump apple stock price for last 3 months"""
    rows = soup.find_all('tr')
    for row in rows:
        try:
            date = row.find_all('td')[0].text.strip()
            close = row.find_all('td')[4].text.strip()
            print ("Date: {}, Apples Stock Closing Price is: ${}").format(
                date, close)
        except:
            continue
    return


if __name__ == "__main__":
    Stock_price()
