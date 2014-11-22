__author__ = 'Przemyslaw "Blasto" Wentrys'

import umysql
from config.configuration import SQL


class uMySQL_Connection():
    def __init__(self):
        """
        Pass.
        :return:
        """
        pass

    def execute_query(self, server, query):
        """
        Get attempts connection to server.
        If successful -> run query and return result.
        If error -> return error.
        Close connection to server.
        :param server:
        :param query:
        :return:
        """
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
            return result
        except Exception as error:
            return error
        finally:
            cnn.close()