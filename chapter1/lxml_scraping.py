# from lxml import lxml
import lxml.html
broken_html = '<ul class=country><li>area<li>population</ul>'
tree = lxml.html.fromstring(broken_html)
fixed_html = lxml.html.tostring(tree, pretty_print=True)
print(fixed_html)

import urllib.request
import cssselect as external_cssselect
from first_scraping import download

def scrape(html):
    tree = lxml.html.fromstring(html)
    td = tree.cssselect('tr#places_area__row>td.w2p_fw')[0]
    area = td.text_content()
    return area

if __name__ == '__main__':
    url = 'http://example.webscraping.com/places/default/view/Aland-Islands-2'

    html = urllib.request.urlopen(url).read()
    text = scrape(html)
    print(text)
