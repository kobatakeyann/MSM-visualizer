# surface or pressure data
is_surface = False
PRESSURE_PLAIN = 850

# whether to plot additional variable or not
is_additional_variable = True

# shade
shade_plot = True
SHADE_VARNAME = "wv_flux_mag"
SHADE_MAX = 200
SHADE_MIN = 0
SHADE_INTERVAL = 20
SHADE_MULTIPLIER = 1
SHADE_ADDITION = 0
COLOR_MAP_NAME = "Blues"
CBAR_UNIT = r"[$\mathrm{g\,m\,kg^{-1}\,s^{-1}}$]"

# contour
contour_plot = True
CONTOUR_VARNAME = "z"
CONTOUR_MAX = 6000
CONTOUR_MIN = 1000
CONTOUR_INTERVAL = 10
CONTOUR_MULTIPLIER = 1
CONTOUR_ADDITION = 0
CONTOUR_COLOR = "black"
plot_contour_label = True
CONTOUR_LABEL_INTERVAL = 10

# vector
vector_plot = True
U_VEXTOR_VARNAME = "wv_flux_u"
V_VEXTOR_VARNAME = "wv_flux_v"
VECTOR_DENSITY = 20
VECTOR_REDUCTION_SCALE = 100
VECTOR_COLOR = "black"
VECTOR_LEDEND_VALUE = 100
VECTOR_LEDEND_SIZE = 8
# VECTOR_LEGEND_NAME = f"{VECTOR_LEDEND_VALUE} " + r"[$\mathrm{m\,s^{-1}}$]"
VECTOR_LEGEND_NAME = (
    f"{VECTOR_LEDEND_VALUE} " + r"[$\mathrm{g\,m\,kg^{-1}\,s^{-1}}$]"
)

# title
TITLE = "water vapor flux"
TITLE_SIZE = 12
