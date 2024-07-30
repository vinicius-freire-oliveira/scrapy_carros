import scrapy

class ForbesSpider(scrapy.Spider):
    name = 'forbes'
    allowed_domains = ['forbes.com.br']
    start_urls = ['https://forbes.com.br/forbeslife/forbes-motors/2023/01/os-dez-carros-classicos-mais-caros-do-mundo/']

    def parse(self, response):
        # Ajuste o XPath para selecionar os elementos <h4> que contêm os títulos dos carros
        cars = response.xpath('//h4/text()').getall()

        for car in cars:
            yield {
                'Os dez carros clássicos mais caros do mundo': car.strip()
            }

        # Adicione mensagens de depuração
        self.log(f'Extracted cars: {cars}')
