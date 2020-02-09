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


def get_tickets():
    return [ticket[1] for ticket in models.query_view_position()]


def get_value_tickets():
    return[get_last_price(ticket) for ticket in get_tickets()]


def union_ticket_and_value():
    positions = models.query_view_position()
    values = get_value_tickets()
    for x in range(len(positions)):
        positions[x].append(values[x])
    return positions


def get_position():
    positions = namedtuple('positions', ['id', 'ticket', 'amount',
                                         'average', 'total', 'last_value'])
    return [positions._make(ticket) for ticket in union_ticket_and_value()]


if __name__ == "__main__":
    print(get_position())
