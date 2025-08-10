from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path("update/<int:id>",views.home,name='update_student')  
    # edit ma click garepaxi path ma update/5 esari janxa , into home function of view.py  
]
