# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['github.com']
    
    @property
    def start_urls(self):
        url_list = [
                'https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wN1QwMDozMzozMlrOBZKUCg%3D%3D&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wNlQxMDo1MjowMiswODowMM4FkjQ0&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMi0xNVQxNDo0ODo1NyswODowMM4BrD-o&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMC0zMVQxNDo1OTozMCswODowMM4Bioa8&tab=repositories'
                ]
        return url_list

    def parse(self, response):
        for course in response.css('li.public'):
            item = CourseItem({
                'name':course.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first('\s+(.*)'),
                'update_time':course.xpath('.//relative-time/@datetime').extract_first()
                })
            yield item
