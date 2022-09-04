from django.urls import re_path
from usuarios import views
urlpatterns=[
    re_path(r'^cliente/$',views.clienteApi),
    re_path(r'^cliente/([0-9]+)$',views.clienteApi),
    re_path(r'^cuenta/$',views.cuentaApi),
    re_path(r'^cuenta/([0-9]+)$',views.cuentaApi)
]