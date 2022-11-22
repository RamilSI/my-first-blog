from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index_report, name='home'),
    path('cats/<int:cat_id>/', report_cat),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive),
]