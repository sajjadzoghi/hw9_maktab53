import argparse
from datetime import date
from datetime import datetime
import pytz
from persiantools.jdatetime import JalaliDate


def age(birthdate):
    birthdate = birthdate.split("-")
    birthdate = [int(i) for i in birthdate]
    birthdate = date(birthdate[0], birthdate[1], birthdate[2])
    ag = date.today() - birthdate
    years = ag.days // 365
    ag = ag.days / 365
    ag = ag - years
    months = int(ag * 12)
    ag = ag * 12
    ag = ag - months
    days = int(ag * 30)
    return f'{years}year & {months}month & {days}day'


def dt_zone(ticks):
    iran = datetime.fromtimestamp(ticks, pytz.timezone('Asia/Tehran'))
    utc = datetime.fromtimestamp(ticks, pytz.timezone('UTC'))
    return f'{utc.strftime("UTC: %Y/%m/%d %H:%M:%S")}\n' \
           f'{iran.strftime("Iran: %Y/%m/%d %H:%M:%S")}\n' \
           f'{iran.strftime("Difference: %z")}'


# def dt_zone(ticks):
#     iran = datetime.fromtimestamp(ticks, pytz.timezone('Asia/Tehran'))
#     utc = datetime.fromtimestamp(ticks, pytz.timezone('UTC'))
#     stri = f'+{iran.utcoffset()}'
#     ut = stri.split(':')
#     return f'{utc.strftime("UTC: %Y/%m/%d %H:%M:%S")}\n' \
#            f'{iran.strftime("Iran: %Y/%m/%d %H:%M:%S")}\n' \
#            f'Difference: {ut[0]}:{ut[1]}'


def is_past(ticks):
    now = datetime.now()
    dt = datetime.fromtimestamp(ticks)
    return now > dt


def today():
    return f'Christian: {date.today().strftime("%Y/%m/%d")}\n' \
           f'Jalali: {JalaliDate.today().strftime("%Y/%m/%d")}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculating and working with dates and times')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-B', '--binery', type=str, help='Get age of a person in years, months and days.')
    group.add_argument('-E', '--epoch', type=float,
                       help='Turn timestamp into Iran and GMT "date" and "time" with "UTCoffset".')
    group.add_argument('-P', '--past', type=float,
                       help='Get the timestamp and give us that it is related to past or not.')

    args = parser.parse_args()
    try:
        if args.binery:
            print(age(args.binery))
        elif args.epoch:
            print(dt_zone(args.epoch))
        elif args.past:
            print(is_past(args.past))
        else:
            print(today())
    except IndexError:
        raise IndexError("You've entered an invalid input.")
