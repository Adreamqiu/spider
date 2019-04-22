# -*- encoding: utf-8 -*-

import scrapy

from kuaixun.items import BishijieItem

class BishijieSpider(scrapy.Spider):
	name = 'bishijie'
	allowed_domains = ['bishijie.com']
	start_urls = [
		'https://www.bishijie.com/kuaixun/'
	]

	def parse(self, response):
		for sel in response.xpath('//div[@class="kuaixun_list"]/div/ul'):
			item = BishijieItem()
			item['ct'] = sel.xpath('span/text()').extract()
			item['title'] = sel.xpath('li/h2/a/text()').extract()
			item['content'] = sel.xpath('li/div/a/text()').extract()
			yield item
