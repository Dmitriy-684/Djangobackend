
from django.contrib import admin
from django.urls import path
# noinspection PyUnresolvedReferences
from API import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create_person),
    path('get/<str:address>', views.get_person_by_address),
    path('get/', views.get_person_all),
    path('', views.main_page),
    path('update/<str:address>', views.update_person_data),
]
