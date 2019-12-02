import datetime as dt
from datetime import timedelta, date
#note this is a generator
def daterange(date1, date2):
    for n in range(int ((date2-date1).days)+1):
        yield date1 + timedelta(n)
if __name__ == '__main__':
    start_dt = dt.date(2015, 12, 25)
    end_dt = dt.date(2016, 1, 1)
    print('Printing date start from ',start_dt,' and end with ',end_dt)
    for d in daterange(start_dt, end_dt):
        print(d.strftime("%Y-%m-%d"))

    time_text='2016/10/18 18:33:00'
    date_object =dt.datetime.strptime(time_text,'%Y/%m/%d %H:%M:%S')
    print('date in',time_text,'is ',date_object.date())

    #subtract 5 days from today
    timedeltadt = dt.date.today()-dt.timedelta(5)
    print('Current Date :', dt.date.today())
    print('5 days before Current Date :', timedeltadt)

    # Convert a UNIX timestamp into a readable date
    print('Convert a UNIX timestamp into a readable date')
    print(dt.datetime.fromtimestamp(int("1344205682")).strftime('%Y:%m:%d %H:%M:%S'))