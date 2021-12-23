import datetime

from django.test import TestCase

from weeks_number.services import WeeksCounter


class TestServices(TestCase):
    '''
    Тестирует работу сервисов
    '''

    def setUp(self) -> None:
        self.date = datetime.datetime.strptime('12.10.2020', '%d.%m.%Y')
        self.first_week_date = datetime.datetime.strptime('02.01.2019', '%d.%m.%Y')
        self.min_first_week_date = datetime.datetime.strptime('01.01.2019', '%d.%m.%Y')
        self.max_first_week_date = datetime.datetime.strptime('05.01.2019', '%d.%m.%Y')

    def test_correct_counting_weeks(self):
        counting = WeeksCounter().count_weeks_from_date(date=self.date)
        counting_first_week = WeeksCounter().count_weeks_from_date(date=self.first_week_date)
        counting_min_first_week = WeeksCounter().count_weeks_from_date(date=self.min_first_week_date)
        counting_max_first_week = WeeksCounter().count_weeks_from_date(date=self.max_first_week_date)
        self.assertEqual(counting, 93)
        self.assertEqual(counting_first_week, 1)
        self.assertEqual(counting_min_first_week, 1)
        self.assertEqual(counting_max_first_week, 1)


class TestViews(TestCase):
    '''
    Тестирует работу представлений
    '''

    def setUp(self) -> None:
        self.correct_date = str(datetime.datetime.strptime('12.10.2020', '%d.%m.%Y'))
        self.incorrect_date = str(datetime.datetime.strptime('12.10.2000', '%d.%m.%Y'))
        self.incorrect_date_format = datetime.datetime.strptime('12.10.2000', '%d.%m.%Y')
        self.incorrect_date_value = 'incorrect_data'

    def test_correct_counting_weeks_view(self):
        response = self.client.post('', data={'date': self.correct_date},
                                    content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 200)

    def test_incorrect_counting_weeks_view(self):
        response = self.client.post('', data={'date': self.incorrect_date})
        response_2 = self.client.post('', data={'date': self.incorrect_date_format})
        response_3 = self.client.post('', data={'date': self.incorrect_date_value})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response_2.status_code, 401)
        self.assertEqual(response_3.status_code, 401)
