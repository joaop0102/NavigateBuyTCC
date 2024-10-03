import scrapy

class RennerSpider(scrapy.Spider):
    name = 'renner'
    start_urls = ['https://www.lojasrenner.com.br/b?Ntt=pulseira']

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    def parse(self, response):
        for product in response.xpath('//div[contains(@class, "ProductBox_productBoxContent__DAUwH")]'):
            product_link = product.xpath('.//a[contains(@class, "ProductBox_productBox__juRuk")]/@href').get(default='').strip()
            product_image = product.xpath('.//img[contains(@class, "ProductBox_productImg__B_6VV")]/@src').get(default='').strip()
            product_title = product.xpath('.//h3[contains(@class, "ProductBox_title__x9UGh")]/text()').get(default='').strip()
            price_original = product.xpath('.//div[contains(@class, "ProductBox_price__d7hDK")]/span/text()').get(default='').strip()
            price_value = product.xpath('.//span[contains(@class, "ProductBox_installments__Hlk0q")]/text()').get(default='').strip()

            if product_title:
                yield {
                    'title': product_title,
                    'link': response.urljoin(product_link),  
                    'image': product_image,
                    'price_original': price_original,
                    'price_value': price_value,
                }

