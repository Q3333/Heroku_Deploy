from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    # crud/
    path('new/', views.new), 
    # crud/new/
    path('create/', views.create), 
    # crud/create/ = form 데이터를 받아서 db 저장함.
    path('<int:pk>/article/', views.detail),
    # crud/pk/article/ detail page
    path('<int:pk>/update/', views.update),
    # crud/pk/update 수정 페이지(폼)

    path('<int:pk>/modify/', views.modify),
    # 실제 업데이트 시켜주는 역할
    path('<int:pk>/delete/', views.delete),
    # 삭제해주기
]

