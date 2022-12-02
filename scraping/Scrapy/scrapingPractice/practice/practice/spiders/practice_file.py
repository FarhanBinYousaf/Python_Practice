import scrapy



class PracticeSpider(scrapy.Spider):
    name = "practice"

    def start_requests(self):
        urls = [
            'https://www.geo.tv',
            'https://www.geo.tv/latest-news',
            'https://www.geo.tv/category/pakistan',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        page = response.url.split("/")[-1]
        filename = f'practice-{page}.html'
        with open(filename,'wb') as f:
            f.write(response.body)