from django.urls import path

from app2 import views

urlpatterns = [
    # 视图函数返回字符串
    path('index1/', views.app2_index1),

    # 视图函数返回字符串中可以有html标签
    path('index2/', views.app2_index2),

    # 视图函数返回模板
    path('index3/', views.app2_index3),


]