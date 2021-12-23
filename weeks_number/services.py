import datetime


class WeeksCounter():

    def __init__(self):
        self.start_first_week = datetime.datetime.strptime('01.01.2019', '%d.%m.%Y')
        self.end_first_week = datetime.datetime.strptime('05.01.2019', '%d.%m.%Y')

    def count_weeks_from_date(self, date: datetime) -> int:
        '''
        Метод считает количество недель от определенной даты
        '''
        if self.start_first_week <= date <= self.end_first_week:
            count_weeks = 1
            return count_weeks
        else:
            # считаем разницу дат и добавляем 1 день, чтобы начать отсчёт с воскресения (end_first_week=суббота)
            delta = date - (self.end_first_week + datetime.timedelta(days=1))
            if (delta.days / 7) == 0:
                # если дата из первой недели, формула вернет 0. Возвращаем значение первой недели
                count_weeks = 1
                return count_weeks
            else:
                # считаем количество недель, начиная с 06.01.2019 (вс)
                count_weeks = (delta.days / 7) + 1
                return int(count_weeks)
