import scrapy
import json

class PlayerSpider(scrapy.Spider):
    name = "player_spider"
    start_urls = []

    def __init__(self):
        self.file_handle = open("player_stats", 'a')
        self.base_url = "http://www.espncricinfo.com/{0}/content/player/{1}"
        self.pic_base_url = "http://www.espncricinfo.com/{}"
        self.country_names = ["australia", "bangladesh", "england", "india", "newzealand", "pakistan", "southafrica", "srilanka", "westindies", "zimbabwe"]
        self.country_codes = [2, 25, 1, 6, 5, 7, 3, 8, 4, 9]
        code_to_name = dict(zip(self.country_codes, self.country_names))

        with open('result_players', 'r') as file_handle:
            for line in file_handle:
                country, player_id = line.split(',')
                PlayerSpider.start_urls.append(self.base_url.format(code_to_name[int(country)], player_id))


    def parse(self, response):
        NAME_SELECTOR = '//p[@class="ciPlayerinformationtxt"]/span/text()'
        TABLE_SELECTOR = '//table[@class="engineTable"]'
        data = response.xpath(NAME_SELECTOR).extract()
        if data != []:
            self.player_name = data[0]
        table = response.xpath(TABLE_SELECTOR)
        player_data_dict = {}
        table1_key = "batting"
        table2_key = "bowling"
        if table != [] and len(table) >= 2:
            first = table[0]
            #print "first table", table.extract()
            first_headers = first.xpath('.//th/text()').extract()
            table_data_rows = first.xpath('.//tbody/tr')
            table_dict = {}
            rows_list = []
            for row in table_data_rows:
                row_dict = {}
                key = row.xpath('.//td/b/text()').extract()
                if key != []:
                    row_data = row.xpath('.//td/text()').extract()
                    result_dict = {}
                    for item in zip(first_headers, row_data):
                        result_dict[item[0]] = item[1]
                    row_dict[key[0]] = result_dict
                rows_list.append(row_dict)
            table_dict[table1_key] = rows_list

            second = table[1]
            #print "first table", table.extract()
            second_headers = second.xpath('.//th/text()').extract()
            table_data_rows = second.xpath('.//tbody/tr')
            rows_list = []
            for row in table_data_rows:
                row_dict = {}
                key = row.xpath('.//td/b/text()').extract()
                if key != []:
                    row_data = row.xpath('.//td/text()').extract()
                    result_dict = {}
                    for item in zip(first_headers, row_data):
                        result_dict[item[0]] = item[1]
                    row_dict[key[0]] = result_dict
                rows_list.append(row_dict)
            table_dict[table2_key] = rows_list
            pic_selector = '//img[@title="{}"]/@src'.format(self.player_name)
            pic = response.xpath(pic_selector).extract()
            if pic != []:
                pic_url = self.pic_base_url.format(pic[0])
                table_dict['pic'] = pic_url
            player_data_dict[self.player_name] = table_dict
            self.file_handle.write(json.dumps(player_data_dict) + '\n')
