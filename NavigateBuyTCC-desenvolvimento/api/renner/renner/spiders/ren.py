import scrapy

class RennerSpider(scrapy.Spider):
    name = 'renner'
    start_urls = ['https://www.lojasrenner.com.br/b?Ntt=pulseira']

    custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    def parse(self, response):
        for i in response.xpath('//div[@class="ProductBox_productBoxContent__DAUwH"]'):
            product_link = i.xpath('.//a[@class="ProductBox_productBox__juRuk"]/@href').get(default='').strip()
            product_image = i.xpath('.//div[@class="ProductBox_productImg__B_6VV"]/@src').get(default='').strip()
            product_title = i.xpath('.//h3[@class="ProductBox_title__x9UGh"]/text()').get(default='').strip()
            price_original = i.xpath('.//div[@class="ProductBox_price__d7hDK"]/text()').get(default='').strip()
            price_value = i.xpath('.//span[@class="ProductBox_installments__Hlk0q"]/text()').get(default='').strip()
        
            if price_value:
                yield {
                    'Preço com Desconto': price_value,
                    'Título': product_title,
                    'Link do Produto': product_link,
                    'Imagem do Produto': product_image
                }
            else:
                yield {
                    'Preço Original': price_original,
                    'Título': product_title,
                    'Link do Produto': product_link,
                    'Imagem do Produto': product_image
                }
