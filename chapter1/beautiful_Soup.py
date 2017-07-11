from bs4 import BeautifulSoup
from first_scraping import download
'''
broken_html = '<ul class=country><li>area <li>population</ul>'
soup = BeautifulSoup(broken_html, 'html5lib')
fixed_html = soup.prettify()
print(fixed_html)
'''

url = 'http://example.webscraping.com/places/default/view/Aland-Islands-2'
html = download(url)
soup = BeautifulSoup(html,"html5lib")
tr = soup.find(attrs={'id':'places_area__row'})
td = tr.find(attrs={'class':'w2p_fw'})
area = td.text
print(area)
