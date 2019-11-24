import datetime as dt
from datetime import timedelta, date
def daterange(date1, date2):
    for n in range(int ((date2-date1).days)+1):
        yield date1 + timedelta(n)
if __name__ == '__main__':
    start_dt = dt.date(2015, 12, 20)
    end_dt = dt.date(2016, 1, 11)
    print('Printing date start from ',start_dt,' and end with ',end_dt)
    for d in daterange(start_dt, end_dt):
        print(d.strftime("%Y-%m-%d"))