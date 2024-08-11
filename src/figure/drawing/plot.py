import os
import pickle
from datetime import date, datetime

import arrow
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

from constants.configuration import (
    CONTOUR_ADDITION,
    CONTOUR_MULTIPLIER,
    SHADE_ADDITION,
    SHADE_MULTIPLIER,
    contour_plot,
    shade_plot,
    vector_plot,
)
from constants.constant import (
    VAR_INFO_XLOCATION,
    VAR_INFO_YLOCATION,
    VECTOR_MULTIPLIER,
    cbar_auto_ticks,
    grid_line,
)
from data_handler.extraction import ArrayExtraction
from figure.basemap.maker import make_base_map
from figure.drawing.methods import PlottingAxes
from figure.helper.calculation import calculate_figsize
from figure.helper.text import TextGenerator
from helper.time import PaddingDatetime


class FigureFactory:
    def __init__(self, utc_date: date, is_surface: bool) -> None:
        fig = plt.figure(figsize=calculate_figsize())
        ax = fig.add_axes(
            (0.11, 0.15, 0.8, 0.8),
            projection=ccrs.PlateCarree(),
        )
        make_base_map(ax)
        self.basefig = pickle.dumps(fig, protocol=pickle.HIGHEST_PROTOCOL)
        self.dataset = ArrayExtraction(utc_date, is_surface=is_surface)
        self.dataset.load_netcdf_data()
        self.date = utc_date

    def make_figure(self, utc_datetime: datetime) -> None:
        basefig = pickle.loads(self.basefig)
        target_ax = PlottingAxes(plt.gca())
        time_helper = PaddingDatetime(utc_datetime)
        hour = int(time_helper.hour)
        if shade_plot:
            self.plot_shade(ax=target_ax, hour=hour)
        if contour_plot:
            self.plot_contour(ax=target_ax, hour=hour)
        if vector_plot:
            self.plot_vector(ax=target_ax, hour=hour)
        if grid_line:
            target_ax.draw_gridlines()
        text_helper = TextGenerator(utc_datetime)
        target_ax.set_title(text_helper.get_title_text())
        filename = text_helper.get_filename()
        os.makedirs(self.dataset.saving_img_dir, exist_ok=True)
        target_ax.save_figure(
            fig=basefig,
            save_dir=self.dataset.saving_img_dir,
            filename=filename,
        )
        plt.cla()
        plt.close()

    def make_whole_day_figures(self) -> None:
        arrow_dt = arrow.get(self.date)
        exe_utc_hour = 0
        while exe_utc_hour <= 21:
            exe_utc_datetime = arrow_dt.shift(hours=exe_utc_hour)
            print(
                f"Now making {exe_utc_datetime.format('YYYYMMDD-HHmm')}UTC figure …"
            )
            self.make_figure(exe_utc_datetime.datetime)
            exe_utc_hour += 3
        print("Successfully Completed!")

    def plot_shade(self, ax: PlottingAxes, hour: int) -> None:
        time_index = int(hour / 3)
        ax.plot_shading(
            self.dataset.lon,
            self.dataset.lat,
            self.dataset.shade_array[time_index, :, :] * SHADE_MULTIPLIER
            + SHADE_ADDITION,
        )
        ax.plot_colorbar(is_auto_ticks=cbar_auto_ticks)
        ax.set_cbar_label()
        ax.plot_text(
            VAR_INFO_XLOCATION,
            VAR_INFO_YLOCATION,
            f"shade    :  {self.dataset.shade_var}",
        )

    def plot_contour(self, ax: PlottingAxes, hour: int) -> None:
        time_index = int(hour / 3)
        ax.plot_contour(
            self.dataset.lon,
            self.dataset.lat,
            self.dataset.contour_array[time_index, :, :] * CONTOUR_MULTIPLIER
            + CONTOUR_ADDITION,
        )
        ax.plot_text(
            VAR_INFO_XLOCATION,
            VAR_INFO_YLOCATION - 0.04,
            f"contour :  {self.dataset.contour_var}",
        )

    def plot_vector(self, ax: PlottingAxes, hour: int) -> None:
        time_index = int(hour / 3)
        ax.plot_vector(
            self.dataset.lon,
            self.dataset.lat,
            self.dataset.u_array[time_index, :, :] * VECTOR_MULTIPLIER,
            self.dataset.v_array[time_index, :, :] * VECTOR_MULTIPLIER,
        )
        ax.plot_legend_vector()
        ax.plot_text(
            VAR_INFO_XLOCATION,
            VAR_INFO_YLOCATION - 0.08,
            f"vector   :  {self.dataset.vector_var}",
        )
