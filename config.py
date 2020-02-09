

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=1min&apikey=EL5PEVKNPNABAHJB&symbol="

url_day = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&interval=1min&apikey=EL5PEVKNPNABAHJB&symbol="


config_db = {
    'user': 'root',
    'password': 'password',
    'database': 'market',
    'raise_on_warnings': True,
    'auth_plugin': 'mysql_native_password'
}
