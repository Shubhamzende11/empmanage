from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index,name='index'),
    path('registration',views.registration,name='registration'),
    path('emp_login', views.emp_login, name='emp_login'),
    path('emp_home', views.emp_home, name='emp_home'),
    path('profile', views.profile, name='profile'),
    path('Logout', views.Logout, name='logout'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('my_experience', views.my_experience, name='my_experience'),
    path('edit_myexperience<int:pid>', views.edit_myexperience, name='edit_myexperience'),
    path('my_education', views.my_education, name='my_education'),
    path('edit_myeducation<int:pid>', views.edit_myeducation, name='edit_myeducation'),
    path('change_password', views.change_password, name='change_password'),
    path('change_adminpassword', views.change_adminpassword, name='change_adminpassword'),
    path('all_employee', views.all_employee, name='all_employee'),
    path('delete_employee/<int:pid>', views.delete_employee, name='delete_employee'),
    path('edit_profile<int:pid>', views.edit_profile, name='edit_profile'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



