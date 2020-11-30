from django.urls import path

from two import views

urlpatterns = [
    path('twoindex/', views.twoindex),

    path('twoindex1/', views.twoindex1),

    # 模板的基本使用
    path('testTem/', views.testTem),

    # 模板的底层实现
    path('testTem1/', views.testTem1),

    # 模型的添加
    path('addList/', views.addList),

    # 模型查询
    path('findList/', views.findList),

    # 模型的更新
    path('updateList/', views.updateList),

    # 模型的删除
    path('deleteList/', views.deleteList),
]
