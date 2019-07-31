from apartment import *
import scrapy
from scrapy.crawler import CrawlerProcess
import urllib.parse

class Restaurant(scrapy.Spider):
    name = 'tenedor'
    allowed_domains = ['www.eltenedor.es']
    start_urls = ['https://www.eltenedor.es/']

    def __init__(self, pApartamento = Apartment):
        self.__apartamento = pApartamento
        
        #self.__strUrl = 'https://www.eltenedor.es/busqueda/?searchText=' + self.__apartamento.nombreCiudad() + ', ' + self.__apartamento.nombrePais() + '&locality=' + self.__apartamento.nombreCiudad() + '&coordinate=' + self.__apartamento.latitud() + ',' + self.__apartamento.longitud()        
        self.__strUrl = 'https://blog.scrapinghub.com'
        self.__strUrl = urllib.parse.quote(self.__strUrl)
        self.start_urls[0] = self.__strUrl
        
        process = CrawlerProcess({
            'USER_AGENT': 'RVEGAS CRAWLER'
        })

        process.crawl(Restaurant)
        process.start()
        
    def parse(self, response):
        print(response.url)
        #for result in response.css('li.resultItem'):
            #id = result.css('data-restaurant-id ::text').extract_first()
            #print(id)