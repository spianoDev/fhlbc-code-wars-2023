import datetime

def today_is():
    day = datetime.datetime.now()
    print(day.strftime('%B %-d, %Y'))


