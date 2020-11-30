from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


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