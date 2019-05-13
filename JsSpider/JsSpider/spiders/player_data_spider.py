import scrapy
from scrapy_splash import SplashRequest


class PlayerSpider(scrapy.Spider):
    name = "player_spider"
    def __init__(self):
        self.start_urls = ["https://stats.nba.com/player/76001/career/"]
        self.file_handle = open("basket_ball_players", 'r')
        #self.base_url = "https://stats.nba.com{}"
        #for line in self.file_handle:
        #    line = line.strip('\n')
        #    self.start_urls.append(self.base_url.format(line))

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args={'wait':10})

    def parse(self, response):
        data = response.body
        print data
