from collections import namedtuple
import models
import requests


url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY"\
      "&interval=1min&apikey=EL5PEVKNPNABAHJB&symbol="


def get_last_price(ticket):
    try:
        valor = requests.get(url + ticket + ".SA").json()["Time Series (1min)"]
        return float(valor[list(valor.keys())[0]]['4. close'])
    except KeyError:
        return 3.14


def get_value_positions():
    position = [x.ticket for x in models.position()]
    stock = namedtuple('stock', ['ticket', 'value'])
    values = [get_last_price(x) for x in position]
    return [stock(*ticket) for ticket in zip(position, values)]


if __name__ == "__main__":
    print(get_value_positions())
