from __future__ import absolute_import
from apartment import *
import scrapy
from scrapy.crawler import CrawlerProcess
import urllib.parse
import logging

class Restaurant(scrapy.Spider):
    name = 'tenedor'
    allowed_domains = ['www.eltenedor.es']
    start_urls = ['https://www.eltenedor.es/']
    logging.getLogger('scrapy').propagate = False  # No mostrar log de scrapy

    def setData(self, pApartamento = Apartment):
        self.__apartamento = pApartamento
        
        self.__strUrl = 'https://www.eltenedor.es/busqueda/?searchText=' + self.__apartamento.nombreCiudad() + ', ' + self.__apartamento.nombrePais() + '&locality=' + self.__apartamento.nombreCiudad() + '&coordinate=' + self.__apartamento.latitud() + ',' + self.__apartamento.longitud()
        #self.__strUrl = urllib.parse.quote(self.__strUrl)
        self.start_urls.append(self.__strUrl)
        
    def empieza(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

        process.crawl(Restaurant)
        process.start()
        
    def parse(self, response):
        if response.url == 'https://www.eltenedor.es/':
            return
            
        print(response.url)
        #for result in response.css('li.resultItem'):
            #id = result.css('data-restaurant-id ::text').extract_first()
            #print(id)