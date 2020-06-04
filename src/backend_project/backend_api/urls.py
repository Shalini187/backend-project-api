from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('user-viewset', views.HelloViewSet, base_name='user-viewset')

urlpatterns = [
    url(r'^user/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)),
]
