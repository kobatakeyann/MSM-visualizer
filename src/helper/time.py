from datetime import date, datetime

import arrow


class PaddingDatetime:
    def __init__(self, datetime_object: date | datetime) -> None:
        arrow_object = arrow.get(datetime_object)
        self.pad_with_zero(arrow_object)

    def pad_with_zero(self, arrow_object: arrow.Arrow) -> None:
        self.year, self.month, self.day, self.hour = (
            arrow_object.format("YYYY"),
            arrow_object.format("MM"),
            arrow_object.format("DD"),
            arrow_object.format("HH"),
        )
