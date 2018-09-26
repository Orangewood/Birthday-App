import datetime


def header():
    print('------------------------------------')
    print('           BIRTHDAY APP')
    print('------------------------------------')
    print()


def get_birthday_from_user():
    print("When were you born?")
    year = int(input("Year [YYYY]:"))
    month = int(input("Month [MM]:"))
    day = int(input("Day [DD]:"))

    birfday = datetime.date(year, month, day)
    return birfday


def difference(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def birthday_information(days):
    if days < 0:
        print("Your birthday was {} days ago this year.".format(-days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("Happy birthday!!!!")


def main():
    header()
    birthday= get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = difference(birthday, today)
    birthday_information(number_of_days)


main()


