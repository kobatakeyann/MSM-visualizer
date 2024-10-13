import numpy as np
import xarray as xr

from constants.configuration import (
    PRESSURE_PLAIN,
    is_additional_variable,
    is_surface,
)
from constants.constant import LAT_BOTTOM, LAT_TOP, LON_LEFT, LON_RIGHT
from data_handler.calculation import (
    calc_horizontal_divergence,
    calc_mixing_ratio,
    calc_water_vapor_concentration,
    calc_water_vapor_flux,
    calc_wind_speed,
)


class NetcdfHandler:
    def __init__(self, netcdf_path: str) -> None:
        ds = xr.open_dataset(netcdf_path)
        if is_additional_variable:
            ds = self.add_other_variables(ds)
        self.ds = self.slice_dataset(ds)

    def add_other_variables(self, ds: xr.Dataset) -> xr.Dataset:
        p = ds["p"].values
        rh = ds["rh"].values
        temprature = ds["temp"].values
        u = ds["u"].values
        v = ds["v"].values
        lon = ds["lon"].values
        lat = ds["lat"].values
        mixing_ratio = calc_mixing_ratio(rh, temprature, p)
        wv_flux_u, wv_flux_v, wv_flux_mag = calc_water_vapor_flux(
            u, v, mixing_ratio
        )
        ds = self.add_variable_to_dataset(
            ds,
            var_name="mixing_ratio",
            var_array=mixing_ratio,
            var_unit="g/kg",
            var_long_name="water vapor mixing ratio",
        )
        ds = self.add_variable_to_dataset(
            ds,
            var_name="wv_concentration",
            var_array=calc_water_vapor_concentration(rh, temprature, p),
            var_unit="g/m^3",
            var_long_name="water vapor concentration",
        )
        ds = self.add_variable_to_dataset(
            ds,
            var_name="wind_speed",
            var_array=calc_wind_speed(u, v),
            var_unit="m/s",
            var_long_name="water speed",
        )
        ds = self.add_variable_to_dataset(
            ds,
            var_name="wv_flux_mag",
            var_array=wv_flux_mag,
            var_unit="g m kg^-1 s^-1",
            var_long_name="magnitude of water vapor flux",
        )
        ds = self.add_variable_to_dataset(
            ds,
            var_name="wv_flux_u",
            var_array=wv_flux_u,
            var_unit="g m kg^-1 s^-1",
            var_long_name="u component of water vapor flux",
        )
        ds = self.add_variable_to_dataset(
            ds,
            var_name="wv_flux_v",
            var_array=wv_flux_v,
            var_unit="g m kg^-1 s^-1",
            var_long_name="v component of water vapor flux",
        )
        ds = self.add_variable_to_dataset(
            ds,
            var_name="wind_div",
            var_array=calc_horizontal_divergence(ds["u"], ds["v"], lon, lat),
            var_unit="s^-1",
            var_long_name="horizontal wind divergence",
        )
        ds = self.add_variable_to_dataset(
            ds,
            var_name="wv_flux_div",
            var_array=calc_horizontal_divergence(
                ds["wv_flux_u"], ds["wv_flux_v"], lon, lat
            ),
            var_unit="g kg^-1 s^-1",
            var_long_name="divergence of horizontal water vapor flux",
        )
        return ds

    def add_variable_to_dataset(
        self,
        ds: xr.Dataset,
        var_name: str,
        var_array: np.ndarray,
        var_unit: str,
        var_long_name: str,
    ) -> xr.Dataset:
        coords = ("time", "p", "lat", "lon")
        ds[var_name] = (coords, var_array)
        ds[var_name].attrs["long_name"] = var_long_name
        ds[var_name].attrs["units"] = var_unit
        return ds

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
