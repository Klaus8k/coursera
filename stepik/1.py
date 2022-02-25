import calendar

a = int(input())

if calendar.isleap(a):
    print('Високосный')
else:
    print('Обычный')