from django.http import HttpResponse
from django.shortcuts import render


def app2_index1(request):
    # 视图函数返回字符串
    return HttpResponse('成功了！, app2_index1')


def app2_index2(request):
    # 视图函数返回字符串中可以有html标签
    return HttpResponse('<h1>视图函数返回字符串中可以有html标签</h1>')


def app2_index3(request):
    # 视图函数返回模板,前提是templates是放在app下的
    # 如果templates是放在app下 那么必须要在settings中的installed_apps要注册app
    return render(request, 'app2index3.html')
