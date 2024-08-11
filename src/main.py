from datetime import date

from constants.configuration import is_surface
from figure.drawing.plot import FigureFactory

if __name__ == "__main__":
    target_date = date(2015, 8, 28)
    factory = FigureFactory(utc_date=target_date, is_surface=is_surface)
    factory.make_whole_day_figures()
