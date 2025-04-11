from django.urls import path
from .views import RegisterView, LoginWithPhraseView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginWithPhraseView.as_view(), name='login'),
]
