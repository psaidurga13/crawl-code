import scrapy
from scrapy_splash import SplashRequest


class MySpider(scrapy.Spider):
    name = "basketball_spider"
    def __init__(self):
        self.start_urls = ["https://stats.nba.com/players/list/?Historic=Y"]
        self.file_handle = open("basket_ball_players", 'a')

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    def parse(self, response):
        data = response.xpath('//li[@class="players-list__name"]/a/@href').extract()
        for element in data:
            self.file_handle.write(element + '\n')
