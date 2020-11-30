from django.urls import path

from two import views

urlpatterns = [
    path('twoindex/', views.twoindex),

    path('twoindex1/', views.twoindex1),

    # 模板的基本使用
    path('testTem/', views.testTem),

    # 模板的底层实现
    path('testTem1/',views.testTem1),
]