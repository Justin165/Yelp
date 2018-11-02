
import requests
from pyquery import PyQuery as pq

from lxml import etree
import urllib

i = 0
restaurants = ""

while i < 1000:
    print('Start processing ' + str(i+1) + ' to ' + str(i + 30))
    pageDOM = pq(url='https://www.yelp.ca/search?find_loc=Burnaby,+BC&start=' + str(i) + '&cflt=restaurants')
    restaurantDOMs = pageDOM(".regular-search-result")
    for restaurantDOM in restaurantDOMs.items():
        restaurants += restaurantDOM('.biz-name').text() + '\t' + 'https://www.yelp.ca' + restaurantDOM('.biz-name').attr('href') + '\t' + restaurantDOM('.category-str-list').text() + '\t' + restaurantDOM('.biz-phone').text() + '\t' + restaurantDOM('address').text() + '\t' + restaurantDOM('.biz-city').text() + '\n'
    i = i + 30

textFile = open('Output.txt', "w")
textFile.write(restaurants)
textFile.close()
print('ALL DONE!!')