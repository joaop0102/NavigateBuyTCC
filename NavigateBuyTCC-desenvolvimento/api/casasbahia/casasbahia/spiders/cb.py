import scrapy

class CasasBSpider(scrapy.Spider):
    name = 'cb'
    start_urls = ['https://www.casasbahia.com.br/carregador/b']

    def parse(self, response):
        for i in response.xpath('//div[@class="css-1enexmx"]'):
            product_link = i.xpath('.//a[@class="dsvia-link-overlay css-1ogn60p"]/@href').get(default='').strip()
            product_image = i.xpath('.//img[@class="product-card__image"]/@src').get(default='').strip()
            product_title = i.xpath('.//span[@aria-hidden="true"]/text()').get(default='').strip()

            price_value = i.xpath('.//div[@class="product-card__highlight-price" and @aria-hidden="true"]/text()').get(default='').strip()
            if not price_value:
                price_value = i.xpath('.//span[contains(@class, "css-1vmkvrm") and not(contains(text(), "estrelas"))]/text()').get(default='').strip()

            stars_text = i.xpath('.//span[@class="css-1vmkvrm"]/text()').get(default='').strip()
            if 'média' in stars_text:  
                stars = stars_text.split('média')[-1].strip()  
                stars = stars.split('.')[0].strip() 
            else:
                stars = ''

            avaliotion = ' '.join(i.xpath('.//span[@class="product-card__reviews-count-text"]//text()').getall()).strip()

            yield {
                    'Preço do produto': price_value,
                    'Título': product_title,
                    'Link do Produto': product_link,
                    'Estrelas': stars,
                    'Avaliações': avaliotion,
                    'Imagem do Produto': product_image
                }