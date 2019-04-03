#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 9 assingment part 1"""

import urllib2
from bs4 import BeautifulSoup


def main():
    url = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), "lxml")
    stats = soup.find_all("table", attrs={"class": "data"})[
        0].find_all('tr', attrs={"valign": "top"})
    counter = 0
    print"*************************************************************"
    print "The top 20 players with the most touchdowns in the year 2018."
    print"*************************************************************"
    for stat in stats:
        name = stat.find_all('td')[0].find_all('a')[0].contents[0]
        position = stat.find_all('td')[1].contents[0]
        team = stat.find_all('td')[2].find_all('a')[0].contents[0]
        tds = stat.find_all('td')[6].contents[0]
        counter += 1
        print ("Player rank: {}, Player Name: {}, Position: {}, "
               "Team: {}, TDs: {}").format(counter, name, position, team, tds)
        if counter >= 20:
            break


if __name__ == '__main__':
    main()
