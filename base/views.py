from django.http import HttpResponse
from django.shortcuts import render
from base.app.hh import hh_parser, to_db


def panel(request):
    return render(request, 'panel.html')

def start(request):
    employers = hh_parser()
    to_db(employers)
    return HttpResponse('ok')