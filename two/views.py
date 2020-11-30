from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from two.models import List


def twoindex(request):
    return HttpResponse('twoindex')

def twoindex1(request):
    return render(request, 'twoindex1.html')


def testTem(request):
    # django是如何将视图函数的数据传递到模板中？
    # 需要传递一个参数 该参数的的名字是context 翻译成中文就是上下文 承上启下 关联的是视图函数和模板
    # 该参数的类型 必须是字典
    context = {
        'name': '王小名',
        'sex': '男',
        'score_list': [0, 1, 2, 3]
    }
    return render(request, 'testTem.html', context=context)


def testTem1(request):
    # 模板的地层实现分两步，1.加载    2.实现

    # 1，加载
    index = loader.get_template('testTem1.html')
    context = {
        'name': '小名'
    }
    # 2, 渲染
    result = index.render(context=context)
    return HttpResponse(result)


def addList(request):
    l = List()
    l.name = '猪肚'
    l.age = '10'
    l.save()

    return HttpResponse('添加成功')


def findList(request):
    # 通过主键查询单个对象
    # list_first = List.objects.get(pk=1)
    # print(list_first.name, list_first.age)

    # 查询所有
    lists = List.objects.all()
    for list in lists:
        print(list.id, list.name, list.age)
    return HttpResponse('查询成功')


def updateList(request):
    list_first = List.objects.first()
    list_first.name = '羊杂'
    list_first.save()
    return HttpResponse('修改成功')


def deleteList(request):
    list_first = List.objects.first()
    list_first.delete()
    return HttpResponse('删除成功')