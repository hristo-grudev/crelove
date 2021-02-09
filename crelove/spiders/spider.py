import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import CreloveItem
from itemloaders.processors import TakeFirst


class CreloveSpider(scrapy.Spider):
	name = 'crelove'
	start_urls = ['https://www.crelove.it/news/']

	def parse(self, response):
		post_links = response.xpath('//h2/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//a[@class="next page-numbers"]/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response):
		title = response.xpath('//h1[@class="title is--large"]/text()').get()
		description = response.xpath('//div[@class="content"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//span[@class="article-date"]/text()').getall()
		date = [p.strip() for p in date]
		date = ' '.join(date).strip()
		if date:
			date = re.findall(r"(\d+\s[a-zA-Z]+\s\d+)", date)[0]

		item = ItemLoader(item=CreloveItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
