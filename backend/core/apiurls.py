# filepath: [urls.py](http://_vscodecontentref_/5)
from django.urls import path
from .views import (
    DisasterEventListCreateView, DisasterEventDetailView,
    SatelliteImageUploadView, TextSummarizeView, DisasterEventSearchView
)

urlpatterns = [
    path('events/', DisasterEventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', DisasterEventDetailView.as_view(), name='event-detail'),
    path('upload-image/', SatelliteImageUploadView.as_view(), name='upload-image'),
    path('summarize/', TextSummarizeView.as_view(), name='summarize-text'),
    path('search/', DisasterEventSearchView.as_view(), name='event-search'),
]