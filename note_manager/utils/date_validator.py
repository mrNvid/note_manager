import datetime


def validate_date(date):
    try:
        datetime.datetime.strftime(date, "%d-%m-%Y")
        return True
    except ValueError:
        return False