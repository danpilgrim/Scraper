
import urllib2
from bs4 import BeautifulSoup

quote_page = ‘http://www.bloomberg.com/quote/SPX:IND'

# gets the html code of that url
page = urllib2.urlopen(quote_page)

# parse the html with BeautifulSoup
soup = BeautifulSoup(page, ‘html.parser’)

#because <h1 class = 'name'> S&P 500 Index </h1>
name_box = soup.find('h1', attrs={'class': 'name'})

name = name_box.text.strip()
print name


#gets the price of S & P
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print price


#Too easy, im installing Scrapy
