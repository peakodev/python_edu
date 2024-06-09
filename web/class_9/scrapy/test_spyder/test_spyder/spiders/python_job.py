import scrapy


class PythonJobSpider(scrapy.Spider):
    name = "python_job"
    allowed_domains = ["realpython.github.io"]
    start_urls = ["https://realpython.github.io/fake-jobs"]

    def parse(self, response):
        cards = response.xpath("//div[@class='card']")
        for card in cards:
            yield {"location": card.xpath(".//p[@class='location']/text()").get(),
                   "job_title": card.xpath(".//h2[@class='title is-5']/text()").get()}
