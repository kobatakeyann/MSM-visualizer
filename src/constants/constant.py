LON_LEFT = 130.5
LON_RIGHT = 140.2
LAT_BOTTOM = 30.2
LAT_TOP = 35.4
LAT_TICKS_INTERVAL = 1
LON_TICKS_INTERVAL = 2
is_deg_min_format = False

is_surface = False
PRESSURE_PLAIN = 850
TITLE = "850hPa geopotential"
TITLE_SIZE = 11

shade_plot = True
SHADE_VARNAME = "h"
SHADE_MIN = -6
SHADE_MAX = -2
SHADE_INTERVAL = 0.5
SHADE_MULTIPLIER = 1
SHADE_ADDITION = -273

COLOR_MAP_NAME = "Blues"
CBAR_EXTENTION = "both"
paint_all = True
WHITE_PART_NUM_FROM_MIDDLE = 2

CBAR_TICKS_INTERVAL = 20
CBAR_TICKS_BASE = 1
CBAR_UNIT = "[℃]"
CBAR_LABEL_SIZE = 10
CBAR_LABEL_LOCATION = 3
cbar_auto_ticks = True

contour_plot = False
CONTOUR_VARNAME = "HGT"
CONTOUR_MIN = 150
CONTOUR_MAX = 2150
CONTOUR_INTERVAL = 100
CONTOUR_MULTIPLIER = 1
CONTOUR_ADDITION = 0
CONTOUR_WIDTH = 0.1
CONTOUR_COLOR = "black"
CONTOUR_LABEL_SIZE = 5
plot_contour_label = False
CONTOUR_LABEL_INTERVAL = 2000

vector_plot = False
U_VEXTOR_VARNAME = "uvmet10"
V_VEXTOR_VARNAME = "uvmet10"
VECTOR_DENSITY = 22
VECTOR_REDUCTION_SCALE = 30
VECTOR_COLOR = "lightslategray"
VECTOR_MULTIPLIER = 1

VECTOR_LEDEND_VALUE = 100
VECTOR_LEDEND_SIZE = 8
VECTOR_LEGEND_NAME = (
    f"{VECTOR_LEDEND_VALUE} " + r"[$\mathrm{g\,kg^{-1}\,m\,s^{-1}}$]"
)

grid_line = True
GRIDLINE_COLOR = "grey"
GRIDLINE_WIDTH = 0.5

VAR_INFO_XLOCATION = -0.05
VAR_INFO_YLOCATION = -0.125
