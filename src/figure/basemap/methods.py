import cartopy.crs as ccrs
from cartopy.mpl.geoaxes import GeoAxes
from cartopy.mpl.ticker import LatitudeFormatter, LongitudeFormatter

from constants.constant import LAT_BOTTOM, LAT_TOP, LON_LEFT, LON_RIGHT
from figure.ticks.ticks_formatter import format_latitude, format_longitude
from figure.ticks.ticks_setter import TicksLocation


class Basemap:
    def __init__(self, ax: GeoAxes) -> None:
        self.ax = ax

    def plot_coastline(self) -> None:
        self.ax.coastlines(linewidths=1, resolution="10m")

    def set_ticks(self) -> None:
        ticks = TicksLocation()
        self.ax.set_xticks(ticks.xloc, crs=ccrs.PlateCarree())
        self.ax.set_yticks(ticks.yloc, crs=ccrs.PlateCarree())
        self.ax.xaxis.set_major_formatter(LongitudeFormatter())
        self.ax.yaxis.set_major_formatter(LatitudeFormatter())

    def express_in_deg_min_format(self) -> None:
        self.ax.xaxis.set_major_formatter(format_longitude)
        self.ax.yaxis.set_major_formatter(format_latitude)

    def narrow_down_the_plot_area(self) -> None:
        self.ax.set_extent(
            (LON_LEFT, LON_RIGHT, LAT_BOTTOM, LAT_TOP), ccrs.PlateCarree()
        )
