import scrapy


class CricketSpider(scrapy.Spider):
    name = "cricket_spider"
    start_urls = []

    def __init__(self):
        self.file_handle = open("result_players", "a")
        self.country_codes = [2, 25, 1, 6, 5, 7, 3, 8, 4, 9]
        self.alpha_list = []
        base_url = "http://www.espncricinfo.com/ci/content/player/country.html?country={0};alpha={1}"

	alpha = 'A'
	for i in range(0, 26):
            self.alpha_list.append(alpha)
            alpha = chr(ord(alpha) + 1)

        for code in self.country_codes:
            for letter in self.alpha_list:
                CricketSpider.start_urls.append(base_url.format(code, letter))


    def parse(self, response):
        PLAYER_SELECTOR = '//a[starts-with(@href, "/ci/content/player") and @class="ColumnistSmry"]/@href'
        url = response.request.url
        c_code = url.split('?')[1].split(';')[0].split('=')[-1]
        players = response.xpath(PLAYER_SELECTOR).extract()
        for player in players:
            player = player.split('/')[-1]
            self.file_handle.write(c_code + ',' + player + '\n')
