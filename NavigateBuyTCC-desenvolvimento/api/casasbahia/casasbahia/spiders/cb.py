import scrapy

class CasasBSpider(scrapy.Spider):
    name = 'cb'
    start_urls = ['https://www.casasbahia.com.br/carregador/b']

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 2,
        'AUTOTHROTTLE_ENABLED': True,
        'COOKIES_ENABLED': True,
        'RETRY_ENABLED': True,
        'RETRY_TIMES': 3,
        'RETRY_HTTP_CODES': [403, 500, 502, 503, 504, 522, 524, 408],
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.google.com/',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
    }

    def parse(self, response):
        for i in response.xpath('//div[@class="css-1enexmx"]'):
            product_link = i.xpath('.//a[@class="dsvia-link-overlay css-1ogn60p"]/@href').get(default='').strip()
            product_image = i.xpath('.//img[@class="product-card__image"]/@src').get(default='').strip()
            product_title = i.xpath('.//span[@aria-hidden="true"]/text()').get(default='').strip()
            price_value = i.xpath('.//b[@aria-hideen="true"]/text()').get(default='').strip()
            stars = i.xpath('.//span[@class="css-1vmkvrm"]/text()').get(default='').strip()

            yield {
                    'Preço do produto': price_value,
                    'Título': product_title,
                    'Link do Produto': product_link,
                    'Estrelas': stars,
                    'Imagem do Produto': product_image
                }
