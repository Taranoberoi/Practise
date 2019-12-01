import datetime

def dt():
    return str(datetime.datetime.now().strftime("%H:%M:%S"))

print(dt())

