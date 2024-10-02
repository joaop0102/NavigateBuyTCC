import scrapy

class MagaluSpider(scrapy.Spider):
    name = 'magalu'
    start_urls = ['https://www.magazineluiza.com.br/busca/pulseira/']

    

    def parse(self, response):
        for i in response.xpath('//li[@class="sc-fTyFcS iTkWie"]'):
            product_link = i.xpath('.//a[@data-testid="product-card-container"]/@href').get(default='').strip()
            product_image = i.xpath('.//img[@data-testid="image"]/@src').get(default='').strip()
            product_title = i.xpath('.//h2[@data-testid="product-title"]/text()').get(default='').strip()
            price_original = i.xpath('.//p[@data-testid="price-original"]/text()').get(default='').strip()
            price_value = i.xpath('.//p[@data-testid="price-value"]/text()').get(default='').strip()
            stars = i.xpath('.//span[@data-testid="review"]/text()').get(default='').strip()
            evaluations = i.xpath('.//span[contains(@class, "sc-cezyBN")]/text()').get(default='').strip()

            if price_value:
                yield {
                    'Preço com Desconto': price_value,
                    'Título': product_title,
                    'Link do Produto': product_link,
                    'Estrelas': stars,
                    'Avaliações': evaluations,
                    'Imagem do Produto': product_image
                }
            else:
                yield {
                    'Preço Original': price_original,
                    'Título': product_title,
                    'Link do Produto': product_link,
                    'Estrelas': stars,
                    'Avaliações': evaluations,
                    'Imagem do Produto': product_image
                }
