import numpy as np

from constants.configuration import (
    CONTOUR_INTERVAL,
    CONTOUR_LABEL_INTERVAL,
    CONTOUR_MAX,
    CONTOUR_MIN,
    SHADE_INTERVAL,
    SHADE_MAX,
    SHADE_MIN,
)
from constants.constant import LAT_BOTTOM, LAT_TOP, LON_LEFT, LON_RIGHT


def calculate_figsize() -> tuple:
    lat_dif = LAT_TOP - LAT_BOTTOM
    lon_dif = LON_RIGHT - LON_LEFT
    figsize = (8, 8 * float(float(lat_dif) / float(lon_dif)))
    return figsize


def get_cbar_levels() -> np.ndarray:
    levels = np.arange(
        float(SHADE_MIN),
        float(SHADE_MAX) + 0.000000000000001,
        float(SHADE_INTERVAL),
    )
    return levels


def get_contour_levels() -> np.ndarray:
    levels = np.arange(
        float(CONTOUR_MIN),
        float(CONTOUR_MAX) + 0.000000000000001,
        float(CONTOUR_INTERVAL),
    )
    return levels


def get_clabel_levels() -> np.ndarray:
    levels = np.arange(
        float(CONTOUR_MIN),
        float(CONTOUR_MAX) + 0.000000000000001,
        float(CONTOUR_LABEL_INTERVAL),
    )
    return levels
