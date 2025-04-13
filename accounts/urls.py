from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginWithPhraseView.as_view(), name='login'),
    path('messages/', MessageView.as_view(), name='messages'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
