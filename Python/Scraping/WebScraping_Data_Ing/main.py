import argparse
import logging #Presentar por consola
from common import config
import news_pages_objects as news

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__) #__name__ variable locar que almacena el nombre del archivo


def _new_scraper(news_sites_uid):
    host = config()['news_sites'][news_sites_uid]['url']
    
    logging.info('Beginning Scraper for {}'.format(host))
    homepage = news.HomePage(news_sites_uid,host)

    for link in homepage.article_links:
        print(link)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    new_site_choices = list(config()['news_sites'].keys())

    parser.add_argument('news_sites',
                        help='The news site that you want to scrape',
                        type=str,
                        choices= new_site_choices)

args = parser.parse_args()

_new_scraper(args.news_sites)