import scrapy


class GeniusLyricsSpider(scrapy.Spider):
    name = 'genius'
    start_urls = ['https://genius.com/']
    url = 'https://genius.com/'


    def parse(self, response):
        pass
