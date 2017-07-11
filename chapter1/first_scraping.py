
# import whois
# print(whois.whois('appspot.com'))

# 下载网页

from urllib import request
import re
from urllib import parse
# 重试
# 用户代理

def download(url, num_retries=2, user_agent='wswp'):
    print('Downloading------>:', url)
    headers = {'User-agent':user_agent}
    downloadRequest = request.Request(url, data=None, headers=headers, origin_req_host=None, unverifiable=False, method=None)
    try:
        html = request.urlopen(downloadRequest).read()
    except request.URLError as e:
        print('Download error', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500<=e.code<600:
                return download(url, num_retries-1, user_agent)
    return html


# sitemap
# def crawl_sitemap(url):
#     sitemap = download(url)
#     links = re.findall(b'<loc>(.*?)</loc>', sitemap)
#     for link in links:
#         html = download(link)
# id
# 链接爬虫
def link_crawler(seed_url, link_regex):
    # 记录重复url
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url  = crawl_queue.pop()
        html = download(url)
        # print(html)

        for link in get_links(html):
            if re.match(link_regex, link):
                link = parse.urljoin(seed_url, link)
                print(link)

                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)
    

def get_links(html):
    '''return a list of links from html
    '''
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    html = html.decode('utf-8')
    return webpage_regex.findall(html)

# 高级功能，解析robot
# rp = RobotFileParser(url='http://example.webscraping.com/robots.txt')
# rp.read()
# url = 'http://example.webscraping.com'
# user_agent = 'BadCrawler'

# 下载限速
# class Throttle:
#     def __init__(self, delay):
#         self.delay = delay
#         self.domains = {}
#     def wait(self, url):
#         domain = parse.urlparse(url).netloc
# 避免爬虫陷阱

if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/places/default/(index|view)')