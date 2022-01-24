import datetime
from termcolor import colored
import time

def timer(f):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        rv = f(*args, **kwargs)
        end = time.perf_counter()
        t = end - start
        ts = '{0:.16f}'.format(t)
        digits = 0
        precision = 3
        for i, s in enumerate(ts):
            if s != '0' and s != '.':
                digits = i
                break

        print(f'Function "{f.__name__}" executed in {ts[:digits+precision]} seconds.')
        return rv
    return wrapper


def convertProxies(proxies):
    return [convertProxy(n) for n in proxies]


def convertProxy(proxy):
    ip = ''
    port = ''
    login = ''
    password = ''
    counter = 0

    for c in proxy:
        if c is ':':
            counter += 1
        elif counter is 0:
            ip += c
        elif counter is 1:
            port += c
        elif counter is 2:
            login += c
        elif counter is 3:
            password += c
    converted_proxy = f'{login}:{password}@{ip}:{port}'
    return converted_proxy


def getTime():
    now = datetime.datetime.now()

    day = now.day
    month = now.month
    year = now.year
    hour = now.hour
    minute = now.minute
    second = now.second

    if day < 10:
        day = "0" + str(day)
    if month < 10:
        month = "0" + str(month)
    if hour < 10:
        hour = "0" + str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    if second < 10:
        second = "0" + str(second)

    # return str(day) + "." + str(month) + "." + str(year) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
    return f'{day}.{month}.{year} {hour}:{minute}:{second}'

def log(*args, **kwargs):
    print(getLog(*args, **kwargs))

def getLog(*args, **kwargs):
    args_ = []

    separator = ''
    color = None
    displayTime = False
    timeSeparator = ' '
    timeColor = None

    if 'separator' in kwargs:
        separator = kwargs['separator']
    if 'color' in kwargs:
        color = kwargs['color']
    if 'displayTime' in kwargs:
        displayTime = kwargs['displayTime']
    if 'timeSeparator' in kwargs:
        timeSeparator = kwargs['timeSeparator']
    if 'timeColor' in kwargs:
        timeColor = kwargs['timeColor']

    for i, arg in enumerate(args):
        if i == len(args) - 1:
            separator = ''
        if hasattr(arg, '__len__') and type(arg) is not str:
            if len(arg) > 1 and type(arg) is not str:
                args_.append([f'{arg[0]}{separator}', arg[1]])
            elif len(arg) > 0 and type(arg) is not str:
                args_.append([f'{arg[0]}{separator}', color])
        else:
            args_.append([f'{arg}{separator}', color])
    if displayTime:
        rv = f'{colored(getTime(), timeColor)}{timeSeparator}'
    else:
        rv = ''

    for arg in args_:
        rv += colored((str(arg[0])), arg[1])
    return rv
