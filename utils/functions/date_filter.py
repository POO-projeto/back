from datetime import datetime, timedelta
from calendar import monthrange
from models.daily import Daily


def calculate_week_range(weeknum):
    today = datetime.today()
    start_of_current_week = today - timedelta(days=today.weekday())
    start_of_week = start_of_current_week - timedelta(weeks=weeknum)
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week


def calculate_month_days(monthnum):
    today = datetime.today()
    target_month = today.month - monthnum
    target_year = today.year

    if target_month <= 0:
        target_month += 12
        target_year -= 1

    num_days = monthrange(target_year, target_month)[1]
    month_days = []

    for day in range(1, num_days + 1):
        current_date = datetime(target_year, target_month, day)
        if current_date.weekday() < 5:
            month_days.append(current_date)

    return month_days


def apply_date_filter(query, filter_by, args):
    if filter_by == "week":
        weeknum = args.get("weeknum", 0)
        start_of_week, end_of_week = calculate_week_range(weeknum)
        query = query.filter(Daily.date >= start_of_week, Daily.date <= end_of_week)
    elif filter_by == "month":
        monthnum = args.get("monthnum", 0)
        month_days = calculate_month_days(monthnum)
        query = query.filter(Daily.date.in_(month_days))
    return query
