import numpy as np

from data_handler.netcdf_reader import NetcdfHandler


class PressureDataHandler(NetcdfHandler):
    def __init__(self, netcdf_path: str, pressure_plain: int) -> None:
        super().__init__(netcdf_path)
        self.pressure_plain = pressure_plain
        self.ds = self.ds.sel(p=self.pressure_plain)
        self.get_lon_lat_array()

    def extract_data_array(self, var_name: str) -> np.ndarray:
        target_array = self.ds[var_name].values
        return target_array
