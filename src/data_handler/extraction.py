import os
from datetime import date

from constants.configuration import (
    CONTOUR_VARNAME,
    PRESSURE_PLAIN,
    SHADE_VARNAME,
    U_VEXTOR_VARNAME,
    V_VEXTOR_VARNAME,
    contour_plot,
    shade_plot,
    vector_plot,
)
from constants.variables_dictionary import VARIABLES_DICTIONARY
from data_handler.netcdf_reader import NetcdfHandler
from download.file_downloader import download_file
from helper.time import PaddingDatetime
from util.path import generate_path


class ArrayExtraction:
    def __init__(self, date: date, is_surface: bool) -> None:
        time_elements = PaddingDatetime(date)
        self.year, self.month, self.day = (
            time_elements.year,
            time_elements.month,
            time_elements.day,
        )
        self.set_neccessary_attributes(is_surface=is_surface)
        self.prepare_netcdf_file()

    def set_neccessary_attributes(self, is_surface: bool) -> None:
        if is_surface:
            stored_nc_dir = "surface"
            self.nc_identifier = "S"
            self.plain = "surface"
            self.saving_img_dir = generate_path(
                f"/img/{self.year}/{self.month}/{self.day}/surface/"
            )
        else:
            stored_nc_dir = "pressure_plain"
            self.nc_identifier = "P"
            self.plain = f"{PRESSURE_PLAIN}hPa"
            self.saving_img_dir = generate_path(
                f"/img/{self.year}/{self.month}/{self.day}/{PRESSURE_PLAIN}hpa/"
            )
        self.nc_dir = generate_path(
            f"/data/netcdf/{stored_nc_dir}/{self.year}/{self.month}/"
        )
        nc_filename = f"{self.month}{self.day}.nc"
        self.nc_path = os.path.join(self.nc_dir, nc_filename)

    def prepare_netcdf_file(self) -> None:
        if not os.path.isfile(self.nc_path):
            os.makedirs(self.nc_dir, exist_ok=True)
            url = f"http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/gpv/netcdf/MSM-{self.nc_identifier}/{self.year}/{self.month}{self.day}.nc"
            download_file(url=url, save_dir=self.nc_dir)

    def load_netcdf_data(self) -> None:
        nc_handler = NetcdfHandler(self.nc_path)
        nc_handler.get_lon_lat_array()
        self.lon = nc_handler.lon
        self.lat = nc_handler.lat
        if shade_plot:
            self.shade_var = (
                f"{self.plain} {VARIABLES_DICTIONARY[SHADE_VARNAME]}"
            )
            self.shade_array = nc_handler.extract_data_array(
                var_name=SHADE_VARNAME
            )
            self.saving_img_dir += SHADE_VARNAME
        if contour_plot:
            self.contour_var = (
                f"{self.plain} {VARIABLES_DICTIONARY[CONTOUR_VARNAME]}"
            )
            self.contour_array = nc_handler.extract_data_array(
                var_name=CONTOUR_VARNAME
            )
            self.saving_img_dir += f"_{CONTOUR_VARNAME}"
        if vector_plot:
            self.vector_var = (
                f"{self.plain} {VARIABLES_DICTIONARY[U_VEXTOR_VARNAME]}"
            )
            self.u_array = nc_handler.extract_data_array(
                var_name=U_VEXTOR_VARNAME
            )
            self.v_array = nc_handler.extract_data_array(
                var_name=V_VEXTOR_VARNAME
            )
            self.saving_img_dir += f"_{U_VEXTOR_VARNAME}"
