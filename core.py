from collections import namedtuple
from config import url, url_day
import models
import requests


def get_last_price(ticket):
    try:
        valor = requests.get(url + ticket + ".SA").json()["Time Series (1min)"]
        return float(valor[list(valor.keys())[0]]['4. close'])
    except KeyError:
        return 3.14


def get_day_price(ticket, data):
    try:
        return float(requests.get(url_day + ticket + ".SA").json()["Time Series (Daily)"][data]['4. close'])
    except KeyError:
        return 3.14


def get_value_initial_position():
    return sum([x[1] * x[3]for x in models.query_view_position_date()])


def get_value_last_position():
    return sum([get_day_price(x[0], x[2]) * x[1] for x in models.query_view_position_date()])


def ibov_value():
    ibov = namedtuple('ibov', ['annual', 'monthly', 'weekly', 'daily'])
    return ibov


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
    positions = namedtuple('positions', ['id', 'ticket', 'amount', 'average', 'total', 'last_value'])
    return [positions._make(ticket) for ticket in union_ticket_and_value()]


if __name__ == "__main__":
    print(get_value_last_position())
