
from scrapy.crawler import CrawlerProcess
from apscheduler.schedulers.twisted import TwistedScheduler
from us import ScrapSpiderUS
from uk import ScrapSpiderUK

process = CrawlerProcess()
scheduler = TwistedScheduler()

scheduler.add_job(process.crawl, 'cron', args=[ScrapSpiderUK], hour=10, timezone='UTC')
scheduler.add_job(process.crawl, 'cron', args=[ScrapSpiderUK], hour=13, timezone='UTC')
scheduler.add_job(process.crawl, 'cron', args=[
                  ScrapSpiderUK], hour=15, minute=30, timezone='UTC')

scheduler.add_job(process.crawl, 'cron', args=[ScrapSpiderUS], hour=10, timezone='US/Eastern')
scheduler.add_job(process.crawl, 'cron', args=[ScrapSpiderUS], hour=13, timezone='US/Eastern')
scheduler.add_job(process.crawl, 'cron', args=[
                  ScrapSpiderUS], hour=15, minute=30, timezone='US/Eastern')

scheduler.start()
process.start(False)
