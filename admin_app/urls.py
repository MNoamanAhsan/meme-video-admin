from django.urls import path
from .views import CategoryListView, MemeSearchApi

urlpatterns=[
    path('api/home/',CategoryListView.as_view(),name='home_list'),
    path('api/search/', MemeSearchApi.as_view(),name='meme_search')
]