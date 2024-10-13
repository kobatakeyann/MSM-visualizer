# surface or pressure data
is_surface = False
PRESSURE_PLAIN = 950

# whether to plot additional variable or not
is_additional_variable = True

# shade
shade_plot = True
SHADE_VARNAME = "mixing_ratio"
SHADE_MAX = 22
SHADE_MIN = 14
SHADE_INTERVAL = 0.5
SHADE_MULTIPLIER = 1
SHADE_ADDITION = 0
COLOR_MAP_NAME = "Blues"
CBAR_UNIT = "[g/kg]"

# contour
contour_plot = True
CONTOUR_VARNAME = "z"
CONTOUR_MAX = 6000
CONTOUR_MIN = 5000
CONTOUR_INTERVAL = 10
CONTOUR_MULTIPLIER = 1
CONTOUR_ADDITION = 0
CONTOUR_COLOR = "black"
plot_contour_label = True
CONTOUR_LABEL_INTERVAL = 50

# vector
vector_plot = True
U_VEXTOR_VARNAME = "u"
V_VEXTOR_VARNAME = "v"
VECTOR_DENSITY = 22
VECTOR_REDUCTION_SCALE = 20
VECTOR_COLOR = "brown"
VECTOR_LEDEND_VALUE = 20
VECTOR_LEDEND_SIZE = 8
VECTOR_LEGEND_NAME = f"{VECTOR_LEDEND_VALUE} " + r"[$\mathrm{m\,s^{-1}}$]"

# title
TITLE = "temperature and horizontal wind"
TITLE_SIZE = 12
