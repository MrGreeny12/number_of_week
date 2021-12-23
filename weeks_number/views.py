import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from weeks_number.services import WeeksCounter


class CountWeeksView(View):
    '''
    Представление для подсчёта количества недель
    '''

    def get(self, request):
        counter = WeeksCounter()
        date = datetime.datetime.now()
        context = {
            "count": counter.count_weeks_from_date(date=date),
            "today": date.date()
        }

        return render(request=request, template_name='weeks_number/home.html', context=context)

    def post(self, request):
        try:
            counter = WeeksCounter()
            if 'date' in request.POST:
                date = datetime.datetime.strptime(request.POST.get('date'), '%d.%m.%Y')
                if date < counter.start_first_week:
                    return HttpResponse(status=401)
            else:
                date = datetime.datetime.now()
            context = {
                "count": counter.count_weeks_from_date(date=date),
                "today": date.date()
            }

            return render(request=request, template_name='weeks_number/home.html', context=context)
        except ValueError:
            return HttpResponse(status=401)
