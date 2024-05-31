from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.ServiceList.as_view()),
    path('project/', views.ProjectList.as_view()),
    path('partner/', views.PartnerList.as_view()),
    path('review/', views.ReviewList.as_view()),
    path('get-in-touch/', views.GetInTouchCreate.as_view()),
    path('our-story/', views.OurStoryList.as_view())
]
