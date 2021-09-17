import datetime


def generate_week_dates(start_year, end_year):
    arr = []
    for year in range(start_year, end_year):
        for week in range(0, 52):
            week_string = str(year)+'-W'+str(week)
            week_date = datetime.datetime.strptime(week_string + '-6', "%Y-W%W-%w")
            week_date_string = str(week_date).split(' ')[0]
            arr.append(week_date_string)
    return arr


print(generate_week_dates(2019, 2020))
