from django.urls import re_path
from usuarios import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns=[
    re_path(r'^cliente/$',views.clienteApi),
    re_path(r'^cliente/([0-9]+)$',views.clienteApi),
    re_path(r'^cuenta/$',views.cuentaApi),
    re_path(r'^cuenta/([0-9]+)$',views.cuentaApi),
    re_path(r'^dir/$',views.direccionApi),
    re_path(r'^dir/([0-9]+)$',views.direccionApi),
    re_path(r'^registro/$', views.logeo)
]