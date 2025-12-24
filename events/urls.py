from django.urls import path , include
from .views import (
    eventListView,
    eventDetailView,
    RegistrationCreateView,
    RegistrationListView,
    )
urlpatterns = [
    path('events/',eventListView.as_view()),
    path('events/<int:pk>/',eventDetailView.as_view()),
    path('register/',RegistrationCreateView.as_view()),
    path('registrations/',RegistrationListView.as_view()),
    ]