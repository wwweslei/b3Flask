import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from model.db import Query
from stocks import get_last_price
from collections import namedtuple




def get_value():
    position = [x.ticket for x in Query().position()]
    stock = namedtuple('stock', ['ticket', 'value'])
    values = [get_last_price(x) for x in position]
    return [stock(*ticket) for ticket in zip(position, values)]


if __name__ == "__main__":
    print(get_value())
