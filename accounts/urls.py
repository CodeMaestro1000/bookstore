# No longer used. Has been replaced with Django all-auth package
from django.urls import path
from .views import SignupPageView, CustomLoginView


urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('custom_login/', CustomLoginView.as_view(), name='login'),
]