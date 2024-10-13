import warnings

import nakametpy.thermo as nt
import numpy as np
import xarray as xr
from nakametpy.kinematics import distance, divergence_2d

from constants.configuration import PRESSURE_PLAIN


def reshape_pressure_array(
    p: np.ndarray, time_num: int, lat_num: int, lon_num: int
) -> np.ndarray:
    p_reshaped = np.reshape(p, (1, p.shape[0], 1, 1))
    p_reshaped = np.tile(p_reshaped, (time_num, 1, lat_num, lon_num))
    return p_reshaped


def calc_mixing_ratio(
    rh: np.ndarray, temperature: np.ndarray, p: np.ndarray
) -> np.ndarray:
    time_num, lat_num, lon_num = rh.shape[0], rh.shape[2], rh.shape[3]
    p_reshaped = reshape_pressure_array(p, time_num, lat_num, lon_num)
    return (
        nt.mixing_ratio_from_relative_humidity(
            rh / 100, temperature, p_reshaped * 100
        )
        * 1000
    )


def calc_water_vapor_concentration(
    rh: np.ndarray, temperature: np.ndarray, p: np.ndarray
) -> np.ndarray:
    mixing_ratio = calc_mixing_ratio(rh, temperature, p)
    time_num, lat_num, lon_num = rh.shape[0], rh.shape[2], rh.shape[3]
    p_reshaped = reshape_pressure_array(p, time_num, lat_num, lon_num)
    return (p_reshaped / (287 * temperature)) * mixing_ratio


def calc_wind_speed(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    return np.sqrt(u**2 + v**2)


def calc_water_vapor_flux(
    u: np.ndarray, v: np.ndarray, q: np.ndarray, p: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    flux_u = u * q
    flux_v = v * q
    flux_magnitude = np.sqrt(flux_u**2 + flux_v**2)
    return flux_u, flux_v, flux_magnitude


def calc_horizontal_divergence(
    u: xr.DataArray, v: xr.DataArray, lon: np.ndarray, lat: np.ndarray
) -> np.ndarray:
    u = u.sel(p=PRESSURE_PLAIN)
    v = v.sel(p=PRESSURE_PLAIN)
    dx, dy = distance(lon, lat)
    divergence_array = np.zeros((u.shape[0], 16, u.shape[1], u.shape[2]))
    warnings.simplefilter("ignore", FutureWarning)
    for i in range(u.shape[0]):
        divergence_array[i, :, :, :] = divergence_2d(
            u[i, :, :], v[i, :, :], dx, dy
        )
    return divergence_array
