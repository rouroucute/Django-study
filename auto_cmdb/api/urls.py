from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView


router = DefaultRouter()
router.register('server-tree',views.ServerTreeViewSet),


app_name="api"
urlpatterns = [
    path('', include(router.urls)),
]


