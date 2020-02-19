from collections import namedtuple
from datetime import date, timedelta
from pandas_datareader import data as wb
import models


def get_last_price(ticket):
    return float(wb.get_data_yahoo(ticket + ".SA").tail(1).Close)


def get_day_price(ticket, data):
    value = wb.get_data_yahoo(ticket + ".SA")
    return float(value.loc[data, "Close"])


def get_value_initial_position():
    return sum([x[1] * x[3]for x in models.query_view_position_date()])


def get_value_last_position():
    return sum([get_day_price(x[0], x[2]) * x[1] for x in models.query_view_position_date()])


def tickets():
    return [ticket[1] for ticket in models.query_view_position()]


def value_tickets():
    return[get_last_price(ticket) for ticket in tickets()]


def union_ticket_and_value():
    positions = models.query_view_position()
    values = value_tickets()
    for x in range(len(positions)):
        positions[x].append(values[x])
    return positions


def get_position():
    positions = namedtuple('positions', ['id', 'ticket', 'amount', 'average', 'total', 'last_value'])
    return [positions._make(ticket) for ticket in union_ticket_and_value()]


def first_day_week():
    return date.today() - timedelta(days=date.today().isoweekday() - 1)


def first_day_month():
    if ((date.today() - timedelta(days=date.today().day - 1)).isoweekday() == 6):
        return date.today() - timedelta(days=date.today().day - 3)
    if ((date.today() - timedelta(days=date.today().day - 1)).isoweekday() == 7):
        return date.today() - timedelta(days=date.today().day - 2)
    return date.today() - timedelta(days=date.today().day - 1)


def first_day_year():
    return date(date.today().year, 1, 1)


def ibov_value():
    values = wb.get_data_yahoo('^BVSP')
    day = float(wb.get_data_yahoo('^BVSP').tail(1).Close)
    last_day = float(wb.get_data_yahoo('^BVSP').tail(2).iloc[0].Close)
    day_week = float(values.loc[first_day_week()].Open)
    day_month = float(values.loc[first_day_month()].Open)
    day_year = float(values.loc[date(date.today().year, 1, 2)].Open)
    ibov = namedtuple('ibov', ['annual', 'monthly', 'weekly', 'daily', 'last_day'])
    print(day_month)
    return ibov(annual=day_year, monthly=day_month, weekly=day_week, daily=day, last_day=last_day)


def earnings():
    ibov = ibov_value()
    ibov_earnings = namedtuple('ibov', ['annual', 'monthly', 'weekly', 'daily'])
    earnings_year = round((ibov.daily / ibov.annual - 1) * 100, 2)
    earnings_month = round((ibov.daily / ibov.monthly - 1) * 100, 2)
    earnings_weekly = round((ibov.daily / ibov.weekly - 1) * 100, 2)
    earnings_daily = round((ibov.daily / ibov.last_day - 1) * 100, 2)
    return ibov_earnings(annual=earnings_year, monthly=earnings_month, weekly=earnings_weekly, daily=earnings_daily)


if __name__ == "__main__":
    print(first_day_month())
