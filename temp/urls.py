
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from chart.views import  HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chart/', include('chart.urls')),

    path('', HomeView.as_view(), name='home'),

]
