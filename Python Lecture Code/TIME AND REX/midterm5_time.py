# The function find_average_between_dates_in_a_log_file
# takes as a parameter a list of strings
# you will find the date when possible
# then calculate the difference between these dates
# then return the average between these dates in minute and you will return the list of these time interval in minute
import datetime
import re

def find_average_between_dates_in_a_log_file(lines):
    lines = '\n'.join(lines)
    list_different_between_dates = []
    average_between_dates = 0
    res = re.findall(r'\d{2}:\d{2}:\d{2}', lines)
    time_lst = []
    for r in res:
        t = datetime.datetime.strptime(r, "%H:%M:%S")
        time_lst.append(t)

    for i in range(len(time_lst) - 1):
        diff = time_lst[i + 1] - time_lst[i]
        list_different_between_dates.append(int((diff.total_seconds()) / 60))

    average_between_dates = sum(list_different_between_dates) / len(list_different_between_dates)

    return average_between_dates, list_different_between_dates