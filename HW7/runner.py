from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from leroy import settings
from leroy.spiders.leroymerlin import LeroySpider


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    search = input('Введите товар (по умолчанию поиск обоев):')
    if not search:
        search = 'обои'
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroySpider, query=search)
    process.start()
