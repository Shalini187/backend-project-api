from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/', views.HelloApiView.as_view())
]
