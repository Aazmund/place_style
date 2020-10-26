from django.urls import path

from . import views
from .views import BlogListView

urlpatterns = [
    path('', views.index_view, name='index'),
    path('blog', BlogListView.as_view(), name='blog'),
    path('repair', views.repair_view, name='repair'),
    path('levkas', views.levkas_view, name='levkas'),
    path('farmer', views.farmer_view, name='farmer'),
    path('home', views.home_view, name='home'),
    path('blacksmith', views.blacksmith_view, name='blacksmith'),
    path('foreman', views.foreman_view, name='foreman'),
    path('antiques', views.antiques_view, name='antiques'),
    path('stove', views.stove_view, name='stove'),
    path('electrician', views.electrician_view, name='electrician'),

]
