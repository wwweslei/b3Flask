import requests

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=1min&apikey=EL5PEVKNPNABAHJB&symbol="


def get_last_price(ticket):
    try:
        valor = requests.get(url + ticket + ".SA").json()["Time Series (1min)"]
        return float(valor[list(valor.keys())[0]]['1. open'])
    except KeyError:
        return 0


if __name__ == '__main__':
    print(get_last_price("vvar3"))
