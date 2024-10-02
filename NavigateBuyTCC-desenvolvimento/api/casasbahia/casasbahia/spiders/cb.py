import scrapy

class CasasBSpider(scrapy.Spider):
    name = 'cb'
    start_urls = ['https://www.casasbahia.com.br/pulseira/b']

    custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }



    def parse(self, response):
        for i in response.xpath('//div[@class="css-329s0i"]'):
            product_link = i.xpath('.//a[@class="dsvia-link-overlay css-1ogn60p"]/@href').get(default='').strip()
            product_image = i.xpath('.//img[@class="product-card__image"]/@src').get(default='').strip()
            product_title = i.xpath('.//h3[@class="product-card__title"]/text()').get(default='').strip()
            price_original = i.xpath('.//div[@dclass="product-card__highlight-price"]/text()').get(default='').strip()
            price_value = i.xpath('.//span[@class="css-1vmkvrm"]/text()').get(default='').strip()
            stars = i.xpath('.//span[@class="css-1vmkvrm"]/text()').get(default='').strip()

            if price_value:
                yield {
                    'Preço com Desconto': price_value,
                    'Título': product_title,
                    'Link do Produto': product_link,
                    'Estrelas': stars,
                    'Imagem do Produto': product_image
                }
            else:
                yield {
                    'Preço Original': price_original,
                    'Título': product_title,
                    'Link do Produto': product_link,
                    'Estrelas': stars,
                    'Imagem do Produto': product_image
                }
