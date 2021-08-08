import urllib
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


url = 'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&marketplace=FLIPKART&otracker=product_breadCrumbs_Mobiles'
page = urllib.request.urlopen(url)
webpage = urlopen(url).read()


a = BeautifulSoup(page)

print(a.prettify())
#print(a.title.string)
#print(a.find_all("a"))