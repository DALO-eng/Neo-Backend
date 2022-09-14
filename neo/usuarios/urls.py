from django.urls import re_path
from usuarios import views
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns=[
    re_path(r'^cliente/$',views.clienteApi),
    re_path(r'^cliente/([0-9]+)$',views.clienteApi),
    re_path(r'^cuenta/$',views.cuentaApi),
    re_path(r'^cuenta/([0-9]+)$',views.cuentaApi),
    re_path(r'^registro/$', views.logeo),
    re_path(r'^login/$',views.login),
    re_path(r'^enviar/$',views.enviar),
    re_path(r'^auth/$',ObtainAuthToken.as_view())
]