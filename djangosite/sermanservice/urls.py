from django.urls import path
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', home_view, name='home_page'),
    path('form/', form_view, name='form_page'),
    # path('form2/', get_report.as_view(), name='form_page2'),
    # path('register/', RegisterUser.as_view(), name='register'),
    # path('login/', login_view, name='login2'),
    # path('top_menu/<int:item_menu_id>', top_menu_view, name='top_menu'),
    # path('sub_menu/<int:sub_item_menu_id>/', sub_menu_view, name='sub_menu'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),


]
