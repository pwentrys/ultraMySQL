__author__ = 'Przemyslaw "Blasto" Wentrys'


from sql.ultramysql import uMySQL_Connection


class uMySQL_Functions():
    def __init__(self):
        """
        Pass.
        :return:
        """
        pass

    def example(self, server, query):
        """
        Executes query
        :param server:
        :param query:
        :return:
        """
        return uMySQL_Connection().execute_query(server, query)

    def result_format(self, result):
        """
        Formats passed result set.

        Example format: {1: {'ColA': 'ABC', 'BCol': 123}, 2: {'ColA': 'DEF', 'BCol': 456}}

        :param result:
        :return:
        """
        formatted_result = {}

        for row_id in range(0, len(result.rows)):
            formatted_row = {}
            row = result.rows[row_id]
            for col_id in range(0, len(row)):
                try:
                    formatted_row.update({result.fields[col_id][0]: int(row[col_id])})
                except:
                    formatted_row.update({result.fields[col_id][0]: str(row[col_id])})

            formatted_result.update({row_id: formatted_row})

        return formatted_result