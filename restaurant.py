from __future__ import absolute_import
from apartment import *
import scrapy
from scrapy.crawler import CrawlerProcess
import urllib.parse

class Restaurant(scrapy.Spider):
    name = 'tenedor'
    allowed_domains = ['']
    start_urls = ['https://www.eltenedor.es/']

    def __init__(self, pApartamento = Apartment):
        self.__apartamento = pApartamento
        
        self.__strUrl = 'https://www.eltenedor.es/busqueda/?searchText=' + self.__apartamento.nombreCiudad() + ', ' + self.__apartamento.nombrePais() + '&locality=' + self.__apartamento.nombreCiudad() + '&coordinate=' + self.__apartamento.latitud() + ',' + self.__apartamento.longitud()        
        self.__strUrl = urllib.parse.quote(self.__strUrl)
        self.start_urls.append(self.__strUrl)
        
    def empieza(self):
        process = CrawlerProcess({
            'USER_AGENT': 'RVEGAS CRAWLER'
        })

        process.crawl(Restaurant)
        process.start()
        
    def parse(self, response):
        print('FRANCHESCO: ' + response.url)
        print('FRANCHESCO: ' + response.url)
        print('FRANCHESCO: ' + response.url)
        print('FRANCHESCO: ' + response.url)
        print('FRANCHESCO: ' + response.url)
        print('FRANCHESCO: ' + response.url)
        print('FRANCHESCO: ' + response.url)
        print('FRANCHESCO: ' + response.url)
        #for result in response.css('li.resultItem'):
            #id = result.css('data-restaurant-id ::text').extract_first()
            #print(id)