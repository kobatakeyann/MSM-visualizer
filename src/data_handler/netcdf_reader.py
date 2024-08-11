import numpy as np
import xarray as xr

from constants.configuration import PRESSURE_PLAIN, is_surface
from constants.constant import LAT_BOTTOM, LAT_TOP, LON_LEFT, LON_RIGHT


class NetcdfHandler:
    def __init__(self, netcdf_path: str) -> None:
        ds = xr.open_dataset(netcdf_path)
        self.ds = self.slice_dataset(ds)

    def slice_dataset(
        self,
        ds: xr.Dataset,
    ) -> xr.Dataset:
        if is_surface:
            hours_of_initial_value = [hour for hour in range(0, 24, 3)]
            ds = ds.isel(time=hours_of_initial_value)
            pass
        else:
            ds = ds.sel(p=PRESSURE_PLAIN)
        ds = ds.sel(
            lon=slice(LON_LEFT, LON_RIGHT), lat=slice(LAT_TOP, LAT_BOTTOM)
        )
        return ds

    def get_lon_lat_array(self) -> None:
        self.lon = self.ds["lon"].values
        self.lat = self.ds["lat"].values

    def extract_data_array(self, var_name: str) -> np.ndarray:
        target_array = self.ds[var_name].values
        return target_array
