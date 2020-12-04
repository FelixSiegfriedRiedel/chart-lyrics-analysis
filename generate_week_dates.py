import datetime


def generate_week_dates(start_year, *args):
    arr = []
    upper_week_range = 53
    if args[0]:
        end_year = args[0]+1
    else:
        end_year = start_year+1
    if args[1]:
        upper_week_range = args[1]+1
    for year in range(start_year, end_year):
        for week in range(1, upper_week_range):
            week_string = str(year)+'-W'+str(week)
            week_date = datetime.datetime.strptime(week_string + '-6', "%Y-W%W-%w")
            week_date_string = str(week_date).split(' ')[0]
            arr.append(week_date_string)
    return arr
