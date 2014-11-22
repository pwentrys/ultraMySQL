__author__ = 'Przemyslaw "Blasto" Wentrys'


from functions import uMySQL_Functions


server = 'Naboo'
query = 'show processlist;'
result_string = "Key: {0} | Value: {1}"

result_raw = uMySQL_Functions().example(server, query)

result_formatted = uMySQL_Functions().result_format(result_raw)

for key in result_formatted:
    print result_string.format(key, result_formatted[key])