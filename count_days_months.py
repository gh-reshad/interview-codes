import numpy as np
from datetime import date

def dayAndMonth(d1, d2):
    d1, d2 = d1.split('-'), d2.split('-')
    months = abs(int(d1[0]) - int(d2[0]))
    days = months * 30  - (int(d1[1]) + int(d2[1]))
    return days, months



if __name__ == '__main__':
    date1 = '12-5-2020'
    date2 = '8-10-2020'
    day , month = dayAndMonth(date1, date2)
    print(day)
    print(month)
