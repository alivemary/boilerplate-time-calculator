from datetime import datetime, timedelta


class TimeProcessor:
    def __init__(self, start, duration, weekday=None):
        self.show_weekday = weekday is not None
        self.start = self.__get_start(start, weekday)
        self.end = self.__get_end(duration)

    def __get_start(self, start, weekday):
        parsed_start = datetime.strptime(start, "%I:%M %p")
        weekdays = (
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        )
        days = (
            weekdays.index(weekday.lower()) - parsed_start.weekday()
            if self.show_weekday
            else 0
        )
        return parsed_start + timedelta(days=days)

    def __get_end(self, duration):
        [hours, minutes] = duration.split(":")
        return self.start + timedelta(hours=int(hours), minutes=int(minutes))

    def end_time(self):
        delta = self.end.date() - self.start.date()
        appendix = "" if delta.days == 0 else " (next day)"
        if delta.days > 1:
            appendix = f" ({delta.days} days later)"
        return datetime.strftime(
            self.end, f"%#I:%M %p{'' if not self.show_weekday else ', %A'}{appendix}"
        )


def add_time(start, duration, weekday=None):
    processor = TimeProcessor(start, duration, weekday)
    return processor.end_time()
