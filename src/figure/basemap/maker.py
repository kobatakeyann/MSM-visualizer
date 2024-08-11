import matplotlib.style as mplstyle
from cartopy.mpl.geoaxes import GeoAxes

from constants.constant import is_deg_min_format
from figure.basemap.methods import Basemap


def make_base_map(ax: GeoAxes) -> GeoAxes:
    mplstyle.use("fast")
    basemap_ax = Basemap(ax)
    basemap_ax.plot_coastline()
    basemap_ax.set_ticks()
    if is_deg_min_format:
        basemap_ax.express_in_deg_min_format()
    basemap_ax.narrow_down_the_plot_area()
    return basemap_ax.ax
