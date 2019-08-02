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
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'DOWNLOAD_DELAY': 0.25,
            'COOKIES_ENABLED': 'False'
        })

        #process = CrawlerProcess({
        #    'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        #    'DOWNLOAD_DELAY': 0.25,
        #    'COOKIES_ENABLED': 'False'
        #})

        process.crawl(Restaurant)
        process.start()
        
    def parse(self, response):
        if response.url == 'https://www.eltenedor.es/':
            return

        for result in response.css('li.resultItem'):
            id = result.css('li.resultItem::attr(data-restaurant-id)').extract_first()
            
            for info in result.css('div.resultItem-information h3'):
                url = info.css('a::attr(href)').extract_first()
                nombre = info.css('a::text').extract_first()

            direccion = self.trataCadenas(result.css('div.resultItem-address::text').extract_first())

            precioMedio = self.trataCadenas(result.css('div.resultItem-averagePrice::text').extract_first())

            valoracion = result.css('span.rating-ratingValue::text').extract_first()

            print('Id:',id,'Nombre:',nombre,'Url:',url, 'Dirección:', direccion, 'Precio medio:', precioMedio, 'Valoración:',valoracion)

        for next_page in response.css('li.next'):
            siguiente = next_page.css('a::attr(href)').extract_first()
            print(siguiente)

    def trataCadenas(self, pCadena):
        pCadena = pCadena.replace('\n', '')
        pCadena = pCadena.strip()

        return pCadena