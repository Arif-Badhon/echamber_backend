from datetime import date
from unittest import result


class TimeString:
    @staticmethod
    def time_str_to_min(time_str: str, am_pm: str) -> int:
        time_str_arr = time_str.split(':')
        hour_to_min = int(time_str_arr[0]) * 60
        if hour_to_min == 720:
            hour_to_min = 0
        rest_min = int(time_str_arr[1])
        all_min = hour_to_min + rest_min
        if am_pm == 'pm':
            all_min += 720
        return all_min

    @staticmethod
    def min_to_time_str(min: int) -> str:
        res_hour = int(min / 60)
        res_min = int(min % 60)
        if res_hour == 0:
            res_hour = 12
        if res_hour > 12:
            res_hour -= 12
        return f'{res_hour}:{res_min}'

    @staticmethod
    def diff_dates(y1: int, m1: int, d1: int, y2: int, m2: int, d2: int):
        date1 = date(y1, m1, d1)
        date2 = date(y2, m2, d2)

        result = abs(date2-date1).days
        return result
