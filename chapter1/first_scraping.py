
import whois
# print(whois.whois('appspot.com'))

# 下载网页

from urllib import request
import re
# 重试
# 用户代理

def download(url, num_retries=2, user_agent='wswp'):
    print('Downloading:', url)
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
def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall(b'<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download(link)


if __name__ == '__main__':
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')
    # print(download('http://blog.csdn.net/drdairen/article/details/51149498'))
    # http://www.baidu.com/