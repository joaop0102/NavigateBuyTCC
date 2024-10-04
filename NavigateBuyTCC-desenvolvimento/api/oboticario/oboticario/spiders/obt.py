import scrapy

class ObtSpider(scrapy.Spider):
    name = 'obt'
    start_urls = ['https://www.boticario.com.br/cabelos/shampoo/']

    def parse(self, response):
        for i in response.xpath('//div[@class="showcase-item   js-event-product-click"]'):
            product_link = i.xpath('.//a[@class="showcase-item-image "]/@href').get(default='').strip()

            product_image = i.xpath('.//img[@class="showcase-image"]/@src').get()
            if not product_image:
                product_image = i.xpath('.//img[@class="showcase-image"]/@data-src').get()
            if not product_image:
                product_image = i.xpath('.//source/@srcset').get()
            if not product_image:
                product_image = i.xpath('.//source/@data-srcset').get()

            product_image = product_image.strip() if product_image else 'Imagem não disponível'

            product_title = i.xpath('.//a[@class="showcase-item-title"]/text()').get(default='').strip()
            price_value = i.xpath('.//span[@class="price-value"]/text()').get(default='').strip()
       
            yield {
                'Preço': price_value,
                'Título': product_title,
                'Link do Produto': product_link,
                'Imagem do Produto': product_image
                }


