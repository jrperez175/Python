import argparse #Es una herramienta completa de análisis de argumentos de línea de comandos, y maneja argumentos opcionales y requeridos
import logging #Presentar por consola
from common import config
import news_pages_objects as news
import re #MOdulo que importa expresiones regulares
import datetime
import csv
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError 

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__) #__name__ variable locar que almacena el nombre del archivo

# Exrresiones regulares
# r --> indica a python que es un string
# ^ --> inicio del patron
# ? --> caracter anterior opcional
# .+ --> una o más letras
# $ —> final del patrón

is_well_formed_link = re.compile(r'^https?://.+/.+$')
is_root_path = re.compile(r'^/.+$')  #/somte-text

def _new_scraper(news_sites_uid):
    host = config()['news_sites'][news_sites_uid]['url']
    
    logging.info('Beginning Scraper for {}'.format(host))
    homepage = news.HomePage(news_sites_uid,host)

    articles = []
    for link in homepage.article_links:
        article = _fetch_article(news_sites_uid,host,link)

        if article:
            logger.info('Article fetch!!')
            articles.append(article)
            print(article.title)
            print(article.body)
            #break
    
    print('The articles number is:{}'.format(len(articles)))

    _save_articles(news_sites_uid,articles)

def _save_articles(news_sites_uid,articles):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = '{news_sites_uid}_{datetime}_articles.csv'.format(news_sites_uid=news_sites_uid, datetime=now)

    
    #dir muestra las propiedades en orden alfabético.
    #csv_headers = ['title', 'body', 'url'] esta linea puede reemplazar la funcion lamda

    csv_headers = list(filter(lambda property: not property.startswith('_'), dir(articles[0])))

    with open(out_file_name, mode='w+', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            row = [str(getattr(article,prop)) for prop in csv_headers] 
            writer.writerow(row)




def _fetch_article(news_sites_uid,host,link):
    logger.info('Start Fetch article at {}'.format(link))

    article = None

    try:
        article = news.ArticlePage(news_sites_uid, _build_link(host,link))
        logger.info(_build_link(host,link))
    except (HTTPError, MaxRetryError) as e:
        logger.warning('Error while fetching the article', exc_info=False)

    if article and not article.body:
        logger.warning('Invalide article. There is not body')
        return None
    
    return article

def _build_link(host,link):
    if is_well_formed_link.match(link):
        return(link)
    elif is_root_path.match(link):
        return '{}{}'.format(host,link)
    else:
        return '{host}/{uri}'.format(host=host,uri=link)


if __name__ == '__main__':
    parser = argparse.ArgumentParser() #Crea  un objeto analizador y decirle qué argumentos esperar

    new_site_choices = list(config()['news_sites'].keys())

    parser.add_argument('news_sites',
                        help='The news site that you want to scrape',
                        type=str,
                        choices= new_site_choices) #almacena el argumento (individualmente o como parte de una lista)

args = parser.parse_args() #El valor de retorno de parse_args() es un Namespace que contiene los argumentos para el comando

_new_scraper(args.news_sites)