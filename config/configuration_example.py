__author__ = 'Przemyslaw "Blasto" Wentrys'


from credentials import EXAMPLE_SERVER


#Connection info string.
SQL = {
    'MySQL':
        {
            'Server_Name': {
                'USERNAME': 'username',
                'PASSWORD': EXAMPLE_SERVER,
                'CONFIGS': '?charset=utf8',
                'DATABASE': 'dbname',
                'ADDRESS': 'db.address.com',
                'PORT': 3306,
            }
        }
}