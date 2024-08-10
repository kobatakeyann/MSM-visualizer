import numpy as np

from data_handler.netcdf_reader import NetcdfHandler


class SurfaceDataHandler(NetcdfHandler):
    def __init__(self, netcdf_path: str) -> None:
        super().__init__(netcdf_path)
        self.ds = self.ds.drop_dims("ref_time")
        self.get_lon_lat_array()

    def extract_data_array(self, var_name: str) -> np.ndarray:
        target_array = self.ds[var_name].values
        return target_array
