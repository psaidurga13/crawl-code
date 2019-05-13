import os
import json
import lxml.html
import requests

def main():
    #url = "curl 'https://stats.nba.com/stats/playercareerstats?LeagueID=00&PerMode=PerGame&PlayerID={}' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-GB,en;q=0.9,en-US;q=0.8,te;q=0.7' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' -H 'Accept: application/json, text/plain, */*' -H 'x-nba-stats-token: true' -H 'Referer: https://stats.nba.com/player/76001/career/' -H 'Cookie: AMCVS_248F210755B762187F000101%40AdobeOrg=1; check=true; _ga=GA1.2.626879186.1557591046; _gid=GA1.2.1488331122.1557591046; s_cc=true; ug=5cd6f4040d8cdf0a3f92ba0015f84c6f; ugs=1; AMCVS_7FF852E2556756057F000101%40AdobeOrg=1; s_vi=[CS]v1|2E6B7A0305032FD0-4000118D80000901[CE]; __gads=ID=49a2fc06554ad8ef:T=1557591046:S=ALNI_MYVv8rrbhGeO5oRl7lVX1JL9B-lWg; AMCV_7FF852E2556756057F000101%40AdobeOrg=1687686476%7CMCIDTS%7C18028%7CMCMID%7C84874934904358391580142893365191899024%7CMCAAMLH-1558195847%7C3%7CMCAAMB-1558195847%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1557598246s%7CNONE%7CMCAID%7C2E6B7A0305032FD0-4000118D80000901%7CvVersion%7C3.0.0; _fbp=fb.1.1557591050600.329316597; AMCV_248F210755B762187F000101%40AdobeOrg=1687686476%7CMCIDTS%7C18028%7CMCMID%7C84872070385936442330142592690038117871%7CMCAAMLH-1558213778%7C3%7CMCAAMB-1558213778%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1557616178s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.0.0; s_sq=%5B%5BB%5D%5D; mbox=PC#34bca904aaea4d4b8c2675b83257cb49.22_31#1620924311|session#8d5183d64b994e26aebc740031a0f974#1557681371; _gat=1' -H 'Connection: keep-alive' -H 'x-nba-stats-origin: stats' --compressed"

    #name_url = "curl 'https://stats.nba.com/player/{}/career/' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'Referer: https://stats.nba.com/player/76001/' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-GB,en;q=0.9,en-US;q=0.8,te;q=0.7' -H 'Cookie: AMCVS_248F210755B762187F000101%40AdobeOrg=1; check=true; _ga=GA1.2.626879186.1557591046; _gid=GA1.2.1488331122.1557591046; s_cc=true; ug=5cd6f4040d8cdf0a3f92ba0015f84c6f; ugs=1; AMCVS_7FF852E2556756057F000101%40AdobeOrg=1; s_vi=[CS]v1|2E6B7A0305032FD0-4000118D80000901[CE]; __gads=ID=49a2fc06554ad8ef:T=1557591046:S=ALNI_MYVv8rrbhGeO5oRl7lVX1JL9B-lWg; AMCV_7FF852E2556756057F000101%40AdobeOrg=1687686476%7CMCIDTS%7C18028%7CMCMID%7C84874934904358391580142893365191899024%7CMCAAMLH-1558195847%7C3%7CMCAAMB-1558195847%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1557598246s%7CNONE%7CMCAID%7C2E6B7A0305032FD0-4000118D80000901%7CvVersion%7C3.0.0; _fbp=fb.1.1557591050600.329316597; AMCV_248F210755B762187F000101%40AdobeOrg=1687686476%7CMCIDTS%7C18028%7CMCMID%7C84872070385936442330142592690038117871%7CMCAAMLH-1558284313%7C3%7CMCAAMB-1558284313%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1557686713s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.0.0; ak_bmsc=3B48572CC5CFABED34E8DF4759141CD4686203449F6500009B4DD85C5795360D~plBBAelmT+n7snIxGPB2FcvzdGwywRe1IU7jzH/Jv0iK8+KPweLXqD3qOwbOhHGECKi6CMBB8TpubKvUgguPKWHDW+TZJsI0IRoGanNjsnPh2Oqw1Z4CDAICPBSFv35mpzujbWm5CQ/pSB+w7OOcfru0Bt5UcHNfDK3KeI0t7A6OC4U/wLnKF71NMyMEkdYN1fMCoSwayq5QJ6/jKr4+tMR13tSwpVaxYM9BOpBGCl1xM=; s_sq=%5B%5BB%5D%5D; mbox=PC#34bca904aaea4d4b8c2675b83257cb49.22_34#1620927615|session#42f97aa1f97c43508cdb5cb724a3bf5e#1557684677; bm_sv=2635126D9DBE2B42E0766BAD01F6ED1A~QTaQlc5OWjni4hq/pOzzQqvzyjEWkgyyj9aJlpV34h9yK9d9MBfabkTdgX1X9ppACNyICR13OH+BFDwyvZJrP6b3W8wkfBonxg1OpXxfMPY4p1PC2d1bwvDoSZMYp2vphfQP3jyQdmqjxMt5/WMeXw==' --compressed"

    base_url = "curl 'http://mlb.mlb.com/pubajax/wf/flow/stats.splayer?season={0}&sort_order=%27desc%27&sort_column=%27avg%27&stat_type=hitting&page_type=SortablePlayer&game_type=%27R%27&player_pool=ALL&season_type=ANY&sport_code=%27mlb%27&results=1000&recSP={1}&recPP=50' -H 'Cookie: stUtil_cookie=1%7C%7C5020076431557772932962; AMCVS_A65F776A5245B01B0A490D44%40AdobeOrg=1; _gcl_au=1.1.1073783287.1557772933; s_cc=true; btIdentify=5d16de78-12da-4163-d379-bd73b25b1528; _bts=bd409ebf-7ebb-4ae4-c6eb-868e9eb26c3b; seerses=e; seerses=e; seerid=110921.28560730613; seerid=110921.28560730613; __gads=ID=3fac2b9214784068:T=1557772933:S=ALNI_MbYutgQYN5tuI2UrjE_y6CAgH5TiQ; _fbp=fb.1.1557772934835.1495004498; _bti=%7B%22app_id%22%3A%22mlb%22%2C%22attributes%22%3A%5B%7B%22created_at%22%3Anull%2C%22name%22%3A%22last_updated%22%2C%22updated_at%22%3Anull%2C%22value%22%3A%222019-05-13T18%3A42%3A15%2B00%3A00%22%7D%5D%2C%22bsin%22%3A%22zc%2FGHFsLn03M%2FtATSh6Ric1QamLh1tpOREo8g%2FGhaGN2Af0aYpnay66s9MMm5js99F18mkl4yedWjMus1XbafQ%3D%3D%22%7D; AMCV_A65F776A5245B01B0A490D44%40AdobeOrg=1687686476%7CMCIDTS%7C18030%7CMCMID%7C16823655971928491672597050467630586231%7CMCAAMLH-1558377903%7C3%7CMCAAMB-1558377903%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1557780303s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18037%7CvVersion%7C3.0.0; s_lv_s=First%20Visit; gpv_v48=Arizona%20Diamondbacks%3A%20Team%3A%20Player%20Information; s_ppn=Arizona%20Diamondbacks%3A%20Team%3A%20Player%20Information; AAMC_mlb_0=REGION%7C3; aam_uuid=16673103295845009192625911746352635599; s_ppvl=Arizona%2520Diamondbacks%253A%2520Team%253A%2520Player%2520Information%2C100%2C27%2C4324.181640625%2C1745%2C856%2C1920%2C1080%2C1.1%2CP; s_getNewRepeat=1557773430803-New; s_lv=1557773430806; s_pvs=0; s_ppv=Arizona%2520Diamondbacks%253A%2520Team%253A%2520Player%2520Information%2C100%2C100%2C4324%2C847%2C856%2C1920%2C1080%2C1.1%2CL; s_tps=686; s_sq=%5B%5BB%5D%5D' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-GB,en;q=0.9,en-US;q=0.8,te;q=0.7' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://mlb.mlb.com/stats/sortable.jsp' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed" 

    #file_handle = open("/home/sai/My_stuff/Practice/Python/Scrapy/players/JsSpider/basket_ball_players",'r')
    result_file = open("./base_ball_player_stats.txt",'a')

    #for line in file_handle:
    #player = line.split('/')
    #player = player[2]
    for year in range(1876, 2020):
        url = base_url.format(year, 1)
        result = json.loads(os.popen(url).read())
        total_pages = result['stats_sortable_player']['queryResults']['totalP']
        for i in range(1, total_pages+1):
            url = base_url.format(year, i)
            result = json.loads(os.popen(url).read())
            players = result['stats_sortable_player']['queryResults']['row']
            total_pages = result['stats_sortable_player']['queryResults']['totalP']
            #data = result['resultSets'][1]['rowSet'][0]
            #player_stats = dict(zip(headers, data))
            #player_html = os.popen(name_url.format(player)).read()
            for player in players:
                player_url = "https://www.mlb.com/player/{}"
                name = player['name_display_first_last']
                player_id = player['player_id']
                param = name.lower().replace(' ','-') + '-' + player_id
                player_url = player_url.format(param)
                player_html = requests.get(player_url)
                player_html = player_html.content
                doc = lxml.html.fromstring(player_html)
                player_img = doc.xpath('//div[@class="player-header__container"]/img/@src')
                #player_name = player_name[0].split('|')[1]
                player['img_url'] = player_img
                result_file.write(json.dumps(player) + '\n')


if __name__ == "__main__":
    main()
