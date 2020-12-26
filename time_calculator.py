from datetime import datetime, timedelta


def add_time(start, duration, weekday=None):

    start_time = datetime.strptime(start, "%I:%M %p")
    if weekday is not None:
        weekdays = (
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        )
        delta = weekdays.index(weekday.lower()) - start_time.weekday()
        start_time += timedelta(days=delta)

    [hours, minutes] = duration.split(":")

    end_time = start_time + timedelta(hours=int(hours), minutes=int(minutes))

    days_diff = end_time.date() - start_time.date()

    appendix = "" if days_diff.days == 0 else " (next day)"

    if days_diff.days > 1:
        appendix = f" ({days_diff.days} days later)"

    return datetime.strftime(
        end_time, f"%#I:%M %p{'' if weekday is None else ', %A'}{appendix}"
    )