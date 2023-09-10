from __future__ import annotations

import datetime

import matplotlib.dates as mdates
from dateutil import parser as date_parser


def set_date_xaxis(ax, start_date="01/01/2020", end_date=None) -> None:
    if end_date is None:
        end_date = datetime.datetime.now()
    ax.set_xlim(date_parser.parse(start_date), end_date)
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1,)))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=(7,)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.xaxis.set_minor_formatter(mdates.DateFormatter("%b"))
    ax.xaxis.set_tick_params(rotation=0)
