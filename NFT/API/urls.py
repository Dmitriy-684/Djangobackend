from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # main page
    path('', views.main_page),
    # admin page
    path('admin/', admin.site.urls),
    # registration user
    path('register/', views.create_person_post),
    # authorize user
    path("login/", views.user_authorization_post),
    # loading image to ipfs
    path("load-image/", views.load_image_post),
    # test for load image
    path("post-image/", views.test_post_image),
    # get image from ipfs
    path("get-image/", views.test_get_image),
    # test for registration
    path('reg-user', views.test_post_for_registration),
    # test for authorize
    path('auth-user', views.test_post_for_authorization),
    # get person by address
    path('get/<str:address>', views.get_person_by_address),
    # get all persons
    path('get/', views.get_person_all),
    # update person data
    path('update/<str:address>', views.update_person_data),

]
