from django.urls import path

from Profile.views import IndexView


urlpatterns = [
    path('', IndexView.as_view())
]