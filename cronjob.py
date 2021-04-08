
from scrapy.crawler import CrawlerProcess
from apscheduler.schedulers.twisted import TwistedScheduler
from us import ScrapSpiderUS
from uk import ScrapSpiderUK

process = CrawlerProcess()
scheduler = TwistedScheduler()

scheduler.add_job(process.crawl, 'cron', args=[ScrapSpiderUK], hour=13, minute=15)
scheduler.add_job(process.crawl, 'cron', args=[ScrapSpiderUK], hour=13, minute=16)
scheduler.add_job(process.crawl, 'cron', args=[ScrapSpiderUK], hour=13, minute=17)
scheduler.start()
process.start(False)
