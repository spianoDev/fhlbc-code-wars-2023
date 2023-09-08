from datetime import date

def date_today():
    day = date.today()
    print(day.strftime('%B %-d, %Y'))


