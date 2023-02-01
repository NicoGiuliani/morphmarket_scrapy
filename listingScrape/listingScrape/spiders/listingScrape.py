import scrapy


class ListingSpider(scrapy.Spider):
    name = "listingScrape"
    allowed_domains = ["morphmarket.com"]
    start_urls = ["https://www.morphmarket.com/us/c/amphibians"]

    def parse(self, response):
        data = response.css("div.row-container.d-flex.flex-wrap")
        names = data.css("span.title::text").getall()
        types = data.css("span.animal-type::text").getall()
        prices = data.css("span.price::text").getall()
        links = data.css(
            'div.col-lg-3.col-md-4.col-sm-4.col-6.item-col.move-up a::attr("href")'
        ).getall()

        for i in range(len(names)):
            yield {
                "name": names[i],
                "type": types[i],
                "price": prices[i],
                "link": links[i],
            }

        # next_page = response.css('a[title*="Next Page"]::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
