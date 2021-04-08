
from scrapy.crawler import CrawlerProcess
from apscheduler.schedulers.twisted import TwistedScheduler
from us import ScrapSpiderUS
from uk import ScrapSpiderUK

process = CrawlerProcess()
scheduler = TwistedScheduler()

scheduler.add_job(process.crawl, 'cron', args=[ScrapSpiderUK], hour=9, minute=10)
scheduler.add_job(process.crawl, 'cron', args=[ScrapSpiderUK], hour=9, minute=11)
scheduler.add_job(process.crawl, 'cron', args=[ScrapSpiderUK], hour=9, minute=12)
scheduler.start()
process.start(False)
