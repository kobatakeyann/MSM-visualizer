from constants.constant import TITLE
from helper.time import PaddingDatetime


class TextGenerator(PaddingDatetime):
    def get_title_text(self) -> str:
        title = (
            f"{self.year}/{self.month}/{self.day} {self.hour}00UTC  {TITLE}"
        )
        return title

    def get_filename(self) -> str:
        filename = f"{self.year}{self.month}{self.day}_{self.hour}00UTC.jpg"
        return filename
