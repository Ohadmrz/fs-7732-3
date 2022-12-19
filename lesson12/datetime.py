# # -*- coding: utf-8 -*-
# """Datetime.ipynb
#
# Automatically generated by Colaboratory.
#
# Original file is located at
#     https://colab.research.google.com/drive/1L8jKlZXMpGNmLN1dmk543TShv_T037VR
#
# # Dates, Times, intervals, timezones, unix time
# """
#
# import datetime
# # from datetime import datetime # do not do it
#
# # datetime.date
# # datetime.datetime
# # datetime.timedelta
#
# """##  Get Current Date and Time"""
#
# datetime_object = datetime.datetime.now()
# # print(type(datetime_object))
# print(datetime_object)
# # print(datetime.datetime.utcnow())
#
# print(type(datetime_object))
#
# datetime_object.day
# print(datetime_object.month)
# print(datetime_object.hour)
# print(datetime_object.weekday())
#
#
#
# """## Get Current Date"""
#
# date_object = datetime.date.today()
# print(type(date_object))
# print(date_object)
#
# """## datetime classes
# * date Class
# * time Class
# * datetime Class
# * timedelta Class
#
# ## date
# """
#
# d = datetime.date(2019, 4, 13)
#
# print(d)
#
# d1 = datetime.date(2000, 2, 29)
#
# today = datetime.date.today()
#
# print("Current date =", today)
#
# # timestamp = datetime.date.fromtimestamp(1326244364)
# timestamp = datetime.date.fromtimestamp(1652595804)
# # timestamp = datetime.date.fromtimestamp(0)
# print("Date =", timestamp)
#
# """### Print today's year, month and day"""
#
# # date object of today's date
# today = datetime.date.today()
#
# print("type:", type(today))
# print("Current year:", today.year)
# print("Current month:", today.month)
# print("Current day:", today.day)
# print("Current weekday:", today.weekday())
#
#
#
# """## time"""
#
# # time(hour = 0, minute = 0, second = 0)
# a = datetime.time()
# print("a =", a)
#
# # time(hour, minute and second)
# b = datetime.time(11, 34, 56)
# print("b =", b)
#
# # time(hour, minute and second)
# c = datetime.time(hour = 11, minute = 34, second = 56)
# print("c =", c)
#
# # time(hour, minute, second, microsecond)
# d = datetime.time(11, 34, 56, 234566)
# print("d =", d)
#
# a = datetime.time(11, 34, 56)
#
# print("hour =", a.hour)
# print("minute =", a.minute)
# print("second =", a.second)
# print("microsecond =", a.microsecond)
#
# """## datetime"""
#
# #datetime(year, month, day)
# a = datetime.datetime(2018, 11, 28)
# print(a)
#
# d = datetime.date(2018, 11, 28)
# print(d)
#
# # datetime(year, month, day, hour, minute, second, microsecond)
# b = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
# print(b)
#
# b.timestamp()
#
# from datetime import datetime
#
# a = datetime(2017, 11, 28, 23, 55, 59, 342380)
# print("year =", a.year)
# print("month =", a.month)
# print("hour =", a.hour)
# print("minute =", a.minute)
# print("timestamp =", a.timestamp())
#
#
#
# """## timededlta"""
#
# import datetime
#
# t1 = datetime.date(year = 2018, month = 7, day = 12)
# t2 = datetime.date(year = 2017, month = 12, day = 23)
# t3 = t1 - t2
# print("type of t3: ", type(t3))
# print("t3 =", t3)
#
#
# # print("type of t3 =", type(t3))
# # print("type of t6 =", type(t6))
#
# t4 = datetime.datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
# t5 = datetime.datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
# t6 = t4 - t5
# print("t6 =", t6)
# print("abs t6 =", abs(t6))
#
# t3.days
#
# t3.seconds
#
# t3.total_seconds()
#
# t6.days
#
# t6.seconds
#
# t6.total_seconds()
#
# t1 = datetime.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
# t2 = datetime.timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
# t3 = t1 - t2
# t33 = t1 + t2
#
# print("t3 =", t3)
# print("t33 =", t33)
#
# datetime.datetime.now() + datetime.timedelta(days=100, hours=23, minutes=59)
#
# """## Negative timedelta"""
#
# from datetime import timedelta
#
# t1 = timedelta(seconds = 33)
# t2 = timedelta(seconds = 54)
# t3 = t1 - t2
#
# print("t3 =", t3)
# print("t3 =", abs(t3))
#
# import datetime
#
# d1 = datetime.date(2022, 2, 13)
# # d2 = datetime.date(2022, 2, 15)
# t1 = datetime.timedelta(days=2)
#
# # d2 + d1
# d1 + t1
#
# d1 = datetime.datetime(2000, 2, 13, 15, 5, 30)
# # d2 = datetime.date(2022, 2, 15)
# # t1 = datetime.timedelta(days=2, hours=10, minutes=5)
# t1 = datetime.timedelta(days=16)
#
# # d2 + d1
# d1 + t1
#
# """## Time duration"""
#
# from datetime import timedelta
#
# t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
# print("total seconds =", t.total_seconds())
#
# # tip - logging how much time it takes for some code to run
# import datetime
# mul = 1
# start = datetime.datetime.now()
# for i in range(1, 100000):
#   mul = mul * i
# end = datetime.datetime.now()
# print(f"total seconds: {(end-start).total_seconds()}")
#
# """## Formatting datetime objects
#
# [Format codes](https://strftime.org/)
#
# ### Python strftime() - datetime object to string
# """
#
# import datetime
#
# # current date and time
# now = datetime.datetime.now()
# print(now)
#
# # May 15, 2022
#
# t = now.strftime("%H:%M:%S")
# print("time:", t)
#
# s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("s1:", s1)
#
# s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("s2:", s2)
#
# s3 = now.strftime("%a, %d/%m/%Y, %I:%M %p")
# # dd/mm/YY H:M:S format
# print("s3:", s3)
#
# """### Python strptime() - string to datetime"""
#
# import datetime
#
# date_string = "21 June, 2018"
# print("date_string =", date_string)
#
# date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
# print("date_object type", type(date_object))
# print("date_object =", date_object)
#
# """## Bad format - raises an exception"""
#
# # date_string = "21 June, 2018"
# date_string = "21-06-2018"
# date_string = "21/06/2018"
# date_string = input("Enter: ")
# try:
#   date_object = datetime.datetime.strptime(date_string, "%d-%m-%Y")
#   print('first format')
# except ValueError:
#   try:
#     date_object = datetime.datetime.strptime(date_string, "%d/%m/%Y")
#     print('second format')
#   except:
#     print("You are stupid")
#
# datetime.datetime.strptime("11/02/2022", "%d-%m-%Y")
#
# import this
#
# """## Exercises
#
# 1. write a function that gets a string that represents datetime in the following format: "2021-12-08, Wed, 10:00" and returns name of the weekday 3 days after the received date.
#
# For example, for the input provided, the output should be: Saturday
#
# Note: you **cannot** assume that the format is necesserily correct
# """
#
# print(weekday_in_3_days("2021-12-08, Wed, 10:00"))
# print(weekday_in_3_days("2021-12-01, Wed, 08:15"))
# print(weekday_in_3_days("2021-12-02, Tue, 07:24"))
#
# """## isoformat"""
#
# date_object.isoformat()
#
# """## Handling timezone in Python - pytz module"""
#
# import pytz
#
# import datetime
#
#
# # not aware of timezone object
# local = datetime.datetime.now()
# print(local)
#
# # aware of timezone object
# local_aware = datetime.datetime.now(pytz.UTC)
# print(local_aware)
#
# pytz.all_timezones
#
# tz_NY = pytz.timezone('America/New_York')
# datetime_NY = datetime.datetime.now(tz_NY)
# print(datetime_NY)
#
# tz_London = pytz.timezone('Europe/London')
# datetime_London = datetime.datetime.now(tz_London)
# print(datetime_London)
#
# pytz.all_timezones
#
# datetime_NY.tzname()
#
# datetime_NY.astimezone(tz_London)
#
# tz_Jerusalem = pytz.timezone('Israel')
#
# print(datetime_NY.astimezone(tz_Jerusalem))
#
# """Note: do not assume that differences in timezones are in round hours!
#
# More info:
#
# https://www.timeanddate.com/time/time-zones-interesting.html
# """