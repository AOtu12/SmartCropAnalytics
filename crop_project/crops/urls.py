from django.urls import path
from . import views

# URL patterns connect web addresses (URLs)
# to the correct view functions in views.py

urlpatterns = [
    # Home page route
    # This opens the main data table page
    path('', views.data_page, name='data_page'),

    # Charts dashboard route
    # This opens the analytics charts page
    path('charts/', views.chart_page, name='chart_page'),
]