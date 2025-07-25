from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("last-deals", views.last_deals, name="last_deals"),
    path("add-deal", views.add_deal, name="add_deal"),
]