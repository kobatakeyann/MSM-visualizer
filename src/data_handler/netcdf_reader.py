import xarray as xr

from constants.constant import LAT_BOTTOM, LAT_TOP, LON_LEFT, LON_LIGHT


class NetcdfHandler:
    def __init__(self, netcdf_path: str) -> None:
        ds = xr.open_dataset(netcdf_path)
        self.ds = self.slice_dataset(ds)

    def slice_dataset(
        self,
        ds: xr.Dataset,
    ) -> xr.Dataset:
        ds = ds.isel(time=0)
        ds = ds.sel(
            lon=slice(LON_LEFT, LON_LIGHT), lat=slice(LAT_TOP, LAT_BOTTOM)
        )
        return ds

    def get_lon_lat_array(self) -> None:
        self.lon = self.ds["lon"].values
        self.lat = self.ds["lat"].values
