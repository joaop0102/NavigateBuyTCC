import scrapy


class UfSpider(scrapy.Spider):
    name = "beleza"
    start_urls = [
        # Beleza
        "https://www.ultrafarma.com.br/categoria/beleza",
        "https://www.ultrafarma.com.br/categoria/cuidados-diarios",
        ]

    def parse(self, response, **kwargs):
        for i in response.xpath('//div[@class="product-wrapper in-stock"]'):
            yield {
                'preço': i.xpath('.//span[@class="product-price-sell"]/text()').get().strip(),
                'título': i.xpath('.//h3[@class="product-name font-bold"]/text()').get().strip(),
                'link': response.urljoin(i.xpath('.//a[contains(@class, "product-item-link")]/@href').get(default='')),
                'loja': 'ultrafarma',
                'estrelas': '0.0',
                'avaliações': 'sem',
                'imagem': i.xpath('.//figure/img/@data-original').get(default=''),
            }
