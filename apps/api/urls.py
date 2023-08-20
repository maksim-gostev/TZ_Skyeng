from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from .v1 import urlpatterns as v1_urls
from .login.views import UserLogin

app_name = 'api'
urlpatterns = [
    path('v1/', include(v1_urls)),
    path('login/', UserLogin.as_view()),
]
