import logging
import subprocess #Permite tener la consola de python e interactuar con sus procesos
import os
import shutil
import pandas as pd
from load.base import engine, Session
from load.article import Article

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

news_sites_uids = ['elcolombiano']
main_path = os.path.dirname(os.path.realpath('__file__'))
path_extract = main_path +'\\extract' 
path_transform = main_path +'\\transform'
path_load = main_path +'\\load'


def main():
    _extract()
    _transform()
    _load()
    _readPandas()
    #_readSqlalchemy()
    

def _extract():
    logger.info('Starting extract process')
    
    
    for news_sites_uid in news_sites_uids:
        subprocess.run(['python',   'main.py', news_sites_uid], cwd='./extract')
        # subprocess.run(['find', '.', '-name', '{}*'.format(news_sites_uid),
        #                     '-exec', 'mv', '{}', '../transform/{}_.csv'.format(news_sites_uid),
        #                     ';'], cwd = './extract')
        
        
        file = _search_file(main_path,news_sites_uid)
        if file:
            _move_file(path_extract +'\\'+file, path_transform + '\\'+file)
            news_sites_uids[news_sites_uids.index(news_sites_uid)] = file
        else:
            logger.info('File extract, not found')
            exit()
        

def _transform():
    logger.info('Starting transform process')
    for news_sites_uid in news_sites_uids:
        #dirty_data_filename = '{}_.csv'.format(news_sites_uid)
        dirty_data_filename = news_sites_uid
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)

        subprocess.run(['python','main.py', dirty_data_filename], cwd= './transform')
        #subprocess.run(['rm', dirty_data_filename], cwd='./transform')
        # subprocess.run(['mv', clean_data_filename, '../load/{}.csv'.format(news_sites_uid)],
        #                 cwd='./transform'

        _remove_file(path_transform,dirty_data_filename)
        _move_file(path_transform +'\\'+ clean_data_filename, path_load + '\\'+ clean_data_filename)


        

def _load():
    logger.info('Strating load process')

    for news_sites_uid in news_sites_uids:
        #clean_data_file = '{}.csv'.format(news_sites_uid)
        clean_data_file = 'clean_{}'.format(news_sites_uid)
        subprocess.run(['python', 'main.py', clean_data_file], cwd='./load')
        #subprocess.run(['rm', clean_data_file], cwd='./load')
        _remove_file(path_load,clean_data_file)

def _readPandas():
    df2 = pd.read_sql_query("Select * from articles",engine)
    print(df2)

def _readSqlalchemy():
    session = Session()
    article = session.query(Article).get(1)
    print(article)
    articles = session.query(Article).all()
    print(articles)
    count_articles = session.query(Article).count()
    print(count_articles)
    n_tokens_title = session.query(Article).filter(Article.n_tokens_title < 30).all()
    print(n_tokens_title)
    n_registros = session.query(Article).order_by(Article.id)[1:5]
    printSqlalchemy(n_registros)

def printSqlalchemy(consulta):
    for row in consulta:
        print(row)
        print(row.title, row.body)

def _search_file(main_patch,  file_match):
    logger.info('Searching file')
    path_extract = main_path + '\\extract'
    

    for paths in list(os.walk(path_extract))[0]:
        if len(paths) > 1:
            for file in paths:
                if file_match in file:
                    return file
    return None

def _move_file(source, destination):
    logger.info('Moving file')
    shutil.move(source, destination)

def _remove_file(path, file):
    logger.info(f'Removing file {file}')
    os.remove(f'{path}\\{file}')



if __name__ == '__main__':
    main()
