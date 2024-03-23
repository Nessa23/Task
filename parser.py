import os as os_module
import scrapy
import json
from selenium import webdriver
from scrapy.selector import Selector
from collections import Counter
import pandas as pd
from scrapy import signals
from scrapy.signalmanager import dispatcher
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


class OzonSpider(scrapy.Spider):
    name = 'ozon_spider'
    allowed_domains = ['ozon.ru']
    start_urls = ['https://www.ozon.ru/category/smartfony-15502/?sorting=rating']
    
    custom_settings = { 
        'USER_AGENT':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'COOKIES_ENABLED': True,
        'DOWNLOAD_DELAY': 0.25,
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.RFPDupeFilter',
        'ROBOTSTXT_OBEY': True,
        'HTTPPROXY_ENABLED': True,
        'ROTATING_PROXY_LIST': [
           
            'http://proxy1.com:8000',
            'http://proxy2.com:8000',
            
        ],
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
            'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
            'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
        },
    }
   
    def __init__(self):
        options = Options()
        options.headless = True
        service = Service('/home/anastasia/Downloads/geckodriver-v0.34.0-linux64/geckodriver')
        self.driver = webdriver.Firefox(service=service, options=options)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def parse(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        links = sel.xpath('//a[@class="tile-link"]/@href').extract()
        for link in links[:100]:
            yield scrapy.Request(url=link, callback=self.parse_phone)

    def parse_phone(self, response):
        os = 'OS information not found'  
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        os_extracted = sel.xpath('//dt[text()="Операционная система"]/following-sibling::dd/text()').get()
        if os_extracted is not None:
            os = os_extracted
        data = {'os': os}
        with open('results.json', 'a') as f:
            f.write(json.dumps(data) + '\n')

    def analyze_data(self):
        if os_module.path.exists('results.json'):
            df = pd.read_json('results.json')
            os_counts = df['os'].value_counts()
            for os, count in os_counts.items():
                print(f"{os} — {count}")
        else:
            print("No data has been scraped yet.")

    def spider_closed(self, spider):
        self.analyze_data()
        self.driver.close()


from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(OzonSpider)
    process.start()

if __name__ == "__main__":
    main()
