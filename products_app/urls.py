from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AssortmentListView, DivisionListView

urlpatterns = [
    path('assortment/', AssortmentListView.as_view()),
    path('division/', DivisionListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)