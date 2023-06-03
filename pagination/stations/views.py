import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV

with open(BUS_STATION_CSV, 'r', newline='', encoding='utf-8') as f:
    reader = list(csv.DictReader(f))




def index(request):
    return redirect(reverse('bus_stations'))





def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    num_page = int(request.GET.get('page', 1))
    paginator = Paginator(reader,10)
    p_page = paginator.get_page(num_page)
    page = paginator.page(num_page)




    context = {
        'bus_stations': p_page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
