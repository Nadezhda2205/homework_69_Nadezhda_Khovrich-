from django.urls import path
from webapp.views import calculate_view, index_view

urlpatterns = [
    path('', index_view),
    path('subtract/', calculate_view),
    path('multiply/', calculate_view),
    path('divide/', calculate_view),
    path('add/', calculate_view),
]
