import scrapy


class Top100ListSpider(scrapy.Spider):
    name = 'top100'
    start_urls = ['https://www.billboard.com/charts/hot-100/2020-01-04']
    week_dates = ['2020-01-04', '2020-01-11', '2020-01-18', '2020-01-25', '2020-02-01', '2020-02-08', '2020-02-15',
                  '2020-02-22', '2020-02-29', '2020-03-07', '2020-03-14', '2020-03-21', '2020-03-28', '2020-04-04',
                  '2020-04-11', '2020-04-18', '2020-04-25', '2020-05-02', '2020-05-09', '2020-05-16', '2020-05-23',
                  '2020-05-30', '2020-06-06', '2020-06-13', '2020-06-20', '2020-06-27', '2020-07-04', '2020-07-11',
                  '2020-07-18', '2020-07-25', '2020-08-01', '2020-08-08', '2020-08-15', '2020-08-22', '2020-08-29',
                  '2020-09-05', '2020-09-12', '2020-09-19', '2020-09-26', '2020-10-03', '2020-10-10', '2020-10-17',
                  '2020-10-24', '2020-10-31', '2020-11-07', '2020-11-14', '2020-11-21', '2020-11-28', '2020-12-05',
                  '2020-12-12', '2020-12-19', '2020-12-26']
    url = 'https://www.billboard.com/charts/hot-100/'
    ID = 0
    week_id = 0

    def parse(self, response):
        week_date = self.week_dates[self.week_id]
        for list_element in response.css('li.chart-list__element'):
            self.ID += 1
            yield {
                'id': self.ID,
                'rank': list_element.css('span.chart-element__rank__number::text').get(),
                'artist': list_element.css('span.chart-element__information__artist::text').get(),
                'song': list_element.css('span.chart-element__information__song::text').get(),
                'rank_last_week': list_element.css('span.chart-element__information__delta__text.text--last::text').get(),
                'peak_rank': list_element.css('span.chart-element__information__delta__text.text--peak::text').get(),
                'weeks_on_chart': list_element.css('span.chart-element__information__delta__text.text--last::text').get(),
                'date': week_date
            }
        if self.week_id < len(self.week_dates):
            self.week_id += 1
            next_page_url = self.url+week_date
            yield scrapy.Request(next_page_url, self.parse)
        pass
