import scrapy

class MagaluSpider(scrapy.Spider):
    name = 'kl'
    start_urls = ['https://www.kalunga.com.br/busca/1?q=pulseira']

    def parse(self, response):
        for i in response.xpath('//div[@class="blocoproduto   col-6 col-md-4 col-xl-3"]'):
            product_link = i.xpath('.//a[@class="blocoproduto__link h-100"]/@href').get(default='').strip()

            product_image = i.xpath('.//img[@class="blocoproduto__image"]/@src').get()
            if not product_image:
                product_image = i.xpath('.//img[@class="blocoproduto__image"]/@data-src').get()
            if not product_image:
                product_image = i.xpath('.//source/@srcset').get()
            if not product_image:
                product_image = i.xpath('.//source/@data-srcset').get()


            product_image = product_image.strip() if product_image else 'Imagem não disponível'
            product_title = i.xpath('.//h2[@class="blocoproduto__title mb-0 mt-2 pb-2 pb-lg-3"]/text()').get(default='').strip()
            price_original = i.xpath('.//span[@class="blocoproduto__text blocoproduto__text--bold blocoproduto__price"]/text()').get(default='').strip()
            price_value = i.xpath('.//span[@class="blocoproduto__text blocoproduto__text--bold blocoproduto__price"]/text()').get(default='').strip()
            stars = i.xpath('.//span[@class="reviews__star_text ps-2"]/text()').get(default='').strip()

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
