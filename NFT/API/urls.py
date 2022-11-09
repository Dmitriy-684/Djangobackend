
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('admin/', admin.site.urls),
    path('register/', views.create_person),
    path("login/", views.user_authorization),
    path('reg-user', views.post_for_registration),
    path('auth-user', views.post_for_authorization),
    path('get/<str:address>', views.get_person_by_address),
    path('get/', views.get_person_all),
    path('update/<str:address>', views.update_person_data),

]
