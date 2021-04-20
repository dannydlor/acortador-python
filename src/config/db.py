import mariadb


config = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '12345678',
    'database' : 'enlaces',
}

DB = mariadb.connect(**config)
DB.autocommit = True