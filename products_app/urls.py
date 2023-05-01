from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_xml.renderers import XMLRenderer

from .views import AssortmentListView, DivisionListView

urlpatterns = [
    path('assortment/', AssortmentListView.as_view()),
    path(
        'assortment.xml',
        AssortmentListView.as_view(renderer_classes=[XMLRenderer]),
        name='assortment-list-xml'
    ),
    path('division/', DivisionListView.as_view()),
    path(
        'division.xml',
        DivisionListView.as_view(renderer_classes=[XMLRenderer]),
        name='division-list-xml'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)