## Python *datetime*

# - Python has got _datetime_ module to handle date and time.

import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# - With dir or help built-in commands it is possible to know the available functions in a certain module. As you can see, in the datetime module there are many functions, but we will focus on _date_, _datetime_, _time_ and _timedelta_. Let se see them one by one.

### Getting *datetime* Information


from datetime import datetime
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

# - Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.

### Formatting Date Output Using *strftime*

from datetime import datetime
new_year = datetime(2024, 2, 19)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0


# - Formatting date time using *strftime* method and the documentation can be found [here](https://strftime.org/).

from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)




# - Here are all the _strftime_ symbols we use to format time. An example of all the formats for this module.

# ![strftime](../images/strftime.png)

### String to Time Using *strptime*
# - Here is a [documentation](https://www.programiz.com/python-programming/datetime/strptimet) hat helps to understand the format. 

from datetime import datetime
date_string = "19 February, 2024"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


### Using *date* from *datetime*

from datetime import date
d = date(2024, 2, 19)
print(d)
print('Current date:', d.today())    
# date object of today's date
today = date.today()
print("Current year:", today.year)   
print("Current month:", today.month) 
print("Current day:", today.day)     

### Time Objects to Represent Time

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)

# output  
# a = 00:00:00  
# b = 10:30:50  
# c = 10:30:50  
# d = 10:30:50.200555

### Difference Between Two Points in Time Using

today = date(year=2024, month=2, day=19)
new_year = date(year=2025, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2024, month = 2, day = 19, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2025, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) 
### Difference Between Two Points in Time Using *timedelata*

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)

  