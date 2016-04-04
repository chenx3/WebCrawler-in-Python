# -*- coding: utf-8 -*-

# Scrapy settings for movieCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'movieCrawler'

SPIDER_MODULES = ['movieCrawler.spiders']
NEWSPIDER_MODULE = 'movieCrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubanmovie (+http://www.yourdomain.com)'
FEED_URI = u'file:///D:/Academics/Project/movieCrawler/movie.csv'
FEED_FORMAT = 'CSV'