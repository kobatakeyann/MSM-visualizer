from constants.configuration import PRESSURE_PLAIN, TITLE, is_surface
from helper.time import PaddingDatetime


class TextGenerator(PaddingDatetime):
    def get_title_text(self) -> str:
        if is_surface:
            plain = "surface"
        else:
            plain = f"{PRESSURE_PLAIN}hPa"
        title = f"{self.year}/{self.month}/{self.day} {self.hour}00UTC  {plain} {TITLE}"
        return title

    def get_filename(self) -> str:
        filename = f"{self.year}{self.month}{self.day}_{self.hour}00UTC.jpg"
        return filename
