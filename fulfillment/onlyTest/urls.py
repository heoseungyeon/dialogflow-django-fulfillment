from django.urls import path
from . import views

urlpatterns = [
    path('', views.webhook, name="webhook"),
    path('dfp/',views.webhook_d_f_p, name="webhook_d_f_p")
]