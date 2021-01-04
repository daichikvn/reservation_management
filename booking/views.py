from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ScheduleForm
from .models import Schedule
import calendar
from datetime import datetime, timedelta
import locale
import re


def index(request):
    today = datetime.today() # now
    this_month_date_str_list = [] # 当月日付リスト
    booking_count = 0 # 予約組数 / 日
    num_of_people_total = 0 # 予約人数 / 日
    booking_data_list = []
    booking_data_dict = {}

    if 'param' in request.GET:
        param = request.GET['param']
        this_year = int(request.GET['year'])
        this_month = int(request.GET['month'])
        print(param, this_year, this_month)
        if param == 'previous':
            if this_month == 1:
                this_year -= 1
                this_month = 12
            else:
                this_month -= 1
        elif param == 'next':
            if this_month == 12:
                this_year += 1
                this_month = 1
            else:
                this_month += 1
        else:
            pass
    else:
        """年月取得"""
        this_year = int(today.strftime("%Y"))
        this_month = int(today.strftime("%m"))

    """前月&次月作成"""
    if this_month == 1:
        previous_month = 12
        next_month = this_month + 1
    elif this_month == 12:
        previous_month = this_month - 1
        next_month = 1
    else:
        previous_month = this_month - 1
        next_month = this_month + 1

    """日数取得"""
    this_month_num_day = calendar.monthrange(this_year, this_month)[1]

    """月リスト作成"""
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    this_month_date_list = [datetime(this_year, this_month, 1) + timedelta(days=i) for i in range(this_month_num_day)]
    this_month_date_str_list = [d.strftime("%-d日 (%a)") for d in this_month_date_list]

    """組,件数リスト作成"""
    for i in range(1, this_month_num_day+1):
        day_data = Schedule.objects.filter(date__year=this_year, date__month=this_month, date__day=i)
        for d in day_data:
            num_of_people_total += d.num_of_people
            booking_count += 1
        booking_data_list.append(str(booking_count) + "組 - " + str(num_of_people_total) + "人")
        num_of_people_total = 0
        booking_count = 0

    for i in range(this_month_num_day):
        booking_data_dict[this_month_date_str_list[i]] = booking_data_list[i]

    return render(request, 'booking/index.html',{
        'booking_data_dict': booking_data_dict,
        'this_year': this_year,
        'this_month': this_month,
        'previous_month': previous_month,
        'next_month': next_month,
    })

def details(request, year, month, day):
    day = re.sub("\\D", "", day)
    details_data = Schedule.objects.filter(date__year=year, date__month=month, date__day=day)
    day = str(int(day))

    return render(request, 'booking/details.html',{
        'details_data': details_data,
        'year': year,
        'month': month,
        'day': day,
    })


class BookingCreateView(CreateView):
    model = Schedule
    form_class = ScheduleForm
    success_url = reverse_lazy('booking:create_done')

def create_done(request):
    return render(request, 'booking/create_done.html')


class BookingUpdateView(UpdateView):
    model = Schedule
    form_class = ScheduleForm
    success_url = reverse_lazy('booking:update_done')

def update_done(request):
    return render(request, 'booking/update_done.html')


class BookingDeleteView(DeleteView):
    model = Schedule
    success_url = reverse_lazy('booking:delete_done')

def delete_done(request):
    return render(request, 'booking/delete_done.html')
