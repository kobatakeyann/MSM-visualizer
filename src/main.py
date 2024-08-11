from datetime import date

from constants.constant import is_surface
from figure.drawing.plot import FigureFactory

if __name__ == "main":
    target_date = date(2023, 8, 21)
    factory = FigureFactory(utc_date=target_date, is_surface=is_surface)
    factory.make_whole_day_figures()
