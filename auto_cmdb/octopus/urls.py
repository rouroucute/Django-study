from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

app_name="octopus"
urlpatterns = [
    path('connection/',views.ConnectionView.as_view(),name="connection"),
    path('runshell/',views.ExecCommandView.as_view(),name="runshell"),
    path('get_result/',views.ExecCommandGetTaskView.as_view(),name="getresult"),
    path('async/',views.AsyncDemoView.as_view(),name="asyncdemo"),
    path('get_task/',views.AsyncDemoGetTaskView.as_view(),name="gettask"),
    path('donamic_task/',views.DonamicGetTaskView.as_view(),name="dotask"),
    path('donamic_result/',views.DonamicGetResultView.as_view(),name="doresult"),
]