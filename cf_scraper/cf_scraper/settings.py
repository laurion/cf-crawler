# Scrapy settings for cf_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cf_scraper'

SPIDER_MODULES = ['cf_scraper.spiders']
NEWSPIDER_MODULE = 'cf_scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cf_scraper (+http://www.yourdomain.com)'
