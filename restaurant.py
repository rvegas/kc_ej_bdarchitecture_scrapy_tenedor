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
        
        strUrl = 'https://www.eltenedor.es/busqueda/?searchText=' + pApartamento.nombreCiudad() + ', ' + pApartamento.nombrePais() + '&locality=' + pApartamento.nombreCiudad() + '&coordinate=' + pApartamento.latitud() + ',' + pApartamento.longitud()        
        
        strUrl = urllib.parse.quote(strUrl)
        
        #self.start_urls = [strUrl]
        
        #process = CrawlerProcess({
        #    'USER_AGENT': 'RVEGAS CRAWLER'
        #})

        #process.crawl(Restaurant)
        #process.start()
        
    def parse(self, response):
        for result in response.css('li.resultItem'):
            id = result.css('data-restaurant-id ::text').extract_first()
            print(id)