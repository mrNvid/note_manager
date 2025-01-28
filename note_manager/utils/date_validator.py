import datetime


def validate_date(date_str):
    try:
        datetime.datetime.strftime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False