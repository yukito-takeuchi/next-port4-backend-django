# coding: utf-8
from django.urls import path

from . import views

urlpatterns = [
  path('device/', views.TaskCreateListAPIView.as_view()),
  path('device/<int:pk>/', views.TaskRetrieveUpdataDestroyAPIView.as_view()),
  path('jobs/', views.JobsPage),
  # path('jobs-create/', views.CreateJobsPage),

]