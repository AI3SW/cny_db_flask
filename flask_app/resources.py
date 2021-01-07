import logging

from flask_restful import Resource

from flask_app.database import get_all_chinese_words
from flask_app.serialize import chinse_words_list_schema

ENDPOINT = '/words'

class ChineseWordResource(Resource):
    def get(self):
        logging.info('GET %s/', ENDPOINT)
        
        logging.info('Querying all chinese words')
        results = get_all_chinese_words()
        logging.info('%s chinese words queried', len(results))
        return chinse_words_list_schema.dump(results)
