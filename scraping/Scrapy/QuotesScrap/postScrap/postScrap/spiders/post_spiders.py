import scrapy


# class PostsSpider(scrapy.Spider):
#     name = "posts"

#     start_urls = [
#         'https://quotes.toscrape.com/page/1/',
#         'https://quotes.toscrape.com/page/2/',
#     ]

#     def parse(self,response):
#         page = response.url.split('/')[-1]
#         # filename = 'posts-%s.html' % page 
#         filename = f'posts-{page}.html'
#         with open(filename,'wb') as f:
#             f.write(response.body)

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://quotes.toscrape.com',
        
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{
                'quotation': quote.css('.text::text').get(),
                'author':quote.css('.author::text').get(),
                'about':quote.css('a').get()
            }
        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)