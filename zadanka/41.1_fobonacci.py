import datetime

def fibonacci_r(x):
    if x <= 1:
        return x
    else:
        return fibonacci_r(x-1) + fibonacci_r(x-2)

def fibonacci_l(x):
    f, s = 0, 1
    for _ in range(x):
        f,s = s, f + s
    return f


start_time = datetime.datetime.now()
print(fibonacci_r(20))
stop_time = datetime.datetime.now()

print(f"Czas: {(stop_time - start_time).microseconds}[ms]")


start_time = datetime.datetime.now()
print(fibonacci_l(10000))
stop_time = datetime.datetime.now()

print(f"Czas: {(stop_time - start_time).microseconds}[ms]")