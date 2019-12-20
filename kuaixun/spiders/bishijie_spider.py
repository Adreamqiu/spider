# -*- encoding: utf-8 -*-

import scrapy

from kuaixun.items import BishijieItem


class BishijieSpider(scrapy.Spider):
    name = 'bishijie'
    allowed_domains = ['bishijie.com']
    start_urls = ['https://www.bishijie.com/kuaixun/']

    def parse(self, response):
        for sel in response.xpath('//div[@class="content-wrap"]/ul/li/div'):
            item = BishijieItem()
            item['ct'] = sel.xpath('a/h3/span/text()').extract_first()
            item['title'] = sel.xpath('a/h3/text()').extract_first()
            item['content'] = sel.xpath('div[@class="news-content"]/div[@class="h63"]/text()').extract_first()
            yield item
