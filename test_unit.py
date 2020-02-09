import mysql.connector
import config
import core
import models


def test_connection_db():
    assert mysql.connector.connect(**config.config_db)


def test_core_get_last_price():
    assert core.get_last_price("petr4") > 10


def test_core_ticket():
    assert core.get_tickets()


def test_get_value_tickets():
    assert core.get_value_tickets()


def test_core_union_ticket_and_value():
    assert core.union_ticket_and_value()


def test_query_view_position():
    assert models.query_view_position()


def test_query_view_position_date():
    assert models.query_view_position_date()


def test_get_day_price():
    assert core.get_day_price("vvar3", "2020-02-03") == 14.49
