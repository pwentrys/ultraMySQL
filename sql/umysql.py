__author__ = 'Przemyslaw "Blasto" Wentrys'

import umysql
from config.configuration import SQL


class MySQL_Connection():
    def __init__(self):
        pass

    def execute_query(self, server, query):
        result = 'None'
        cnn = umysql.Connection()

        try:
            cnn.connect(
                SQL['MySQL'][server]['ADDRESS'],
                SQL['MySQL'][server]['PORT'],
                SQL['MySQL'][server]['USERNAME'],
                SQL['MySQL'][server]['PASSWORD'],
                SQL['MySQL'][server]['DATABASE']
            )

            result = cnn.query(query)
        except Exception as error:
            print error

        cnn.close()
        return result