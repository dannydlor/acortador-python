import mariadb


config = {
    'host' : 'localhost',
    'port' : 3309,
    'user' : 'root',
    'password' : 'Maleja21*',
    'database' : 'enlaces',
}

DB = mariadb.connect(**config)
DB.autocommit = True