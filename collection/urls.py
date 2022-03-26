from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CollectionList, CollectionDetail

urlpatterns = [
    path('/', CollectionList.as_view()),
    path('/<int:pk>/', CollectionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
