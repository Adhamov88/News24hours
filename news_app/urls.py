from django.urls import path
from .views import ListViews, detail_views, HomePageView, ContactView,PoliticalView,SportView,LocalView

urlpatterns = [
    path('news/', ListViews, name='news_list'),
    path('/<slug:news>/',detail_views, name='detail_list'),
    path('', HomePageView.as_view(), name='home_page_view'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('political/',PoliticalView.as_view(),name='political_news'),
    path('sport/',SportView.as_view(),name='sport_news'),
    path('local/',LocalView.as_view(),name='local_news')
]