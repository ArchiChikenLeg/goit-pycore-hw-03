import datetime
def get_days_from_today(date):
    inDate = datetime.date.fromisoformat(date)
    todayDate = datetime.date.today()
    return (todayDate - inDate).days

inputDate = input('Enter your date: ')
try:
    print(get_days_from_today(inputDate))
except ValueError:
    print('Date you entering is not correct')
except:
    print('Unexpected error occured')