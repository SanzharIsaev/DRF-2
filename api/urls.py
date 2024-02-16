from django.urls import path
from .views import BookAPiView

urlpatterns = [
    path('', BookAPiView.as_view(),)
]
