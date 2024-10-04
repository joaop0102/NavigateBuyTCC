import scrapy

class MagaluSpider(scrapy.Spider):
    name = 'magalu'
    start_urls = ['https://www.magazineluiza.com.br/busca/geladeira/?from=submit']

    def parse(self, response):
        for i in response.xpath('//li[@class="sc-fTyFcS iTkWie"]'):
            product_link = response.urljoin(i.xpath('.//a[@data-testid="product-card-container"]/@href').get(default='').strip())
            product_image = i.xpath('.//img[@data-testid="image"]/@src').get(default='').strip()
            product_title = i.xpath('.//h2[@data-testid="product-title"]/text()').get(default='').strip()
            price_original = i.xpath('.//p[@data-testid="price-original"]/text()').get(default='').strip()
            price_vl = i.xpath('.//p[@data-testid="price-value"]/text()').get(default='').strip()

            price_value = price_vl.replace('R$', '').strip()  

            stars_text = i.xpath('.//span[contains(@class, "sc-cezyBN")]/text()').get(default='').strip()
            evaluations_text = i.xpath('.//span[contains(@class, "sc-cezyBN")]/text()').get(default='').strip()

            if stars_text:
                stars = stars_text.split()[0]
            else:
                stars = ''

            if evaluations_text:
                evaluations = evaluations_text.split('(')[-1].strip() 
                evaluations = '(' + evaluations 
            else:
                evaluations = ''

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