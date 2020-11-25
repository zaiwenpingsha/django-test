from django.http import HttpResponse
from django.shortcuts import render

def app2_index1(request):
    return HttpResponse('成功了！, app2_index1')
