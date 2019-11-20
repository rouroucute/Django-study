from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

# router = DefaultRouter()
# router.register(r'assets',views.AssetViewSet),
# router.register(r'server',views.ServerViewSet),
# router.register(r'memory',views.MemoryViewSet),
# router.register(r'disk',views.DiskViewSet)


# app_name="cmdb"
# urlpatterns = [
#     path('', include(router.urls)),
#     path('assets-list/',TemplateView.as_view(template_name="cmdb/assets-list.html"),name="assets_list"),
#     path('server-list/',TemplateView.as_view(template_name="cmdb/server-list.html"),name="server_list"),
#     path('mem-list/',TemplateView.as_view(template_name="cmdb/mem-list.html"),name="mem_list"),
#     path('disk-list/',TemplateView.as_view(template_name="cmdb/disk-list.html"),name="disk_list"),
#     path('assets-detail/<slug:pk>/', views.AssetsDetailView.as_view(),name='assetsDetail'),   
# ]


###cbv
app_name="cmdb"
urlpatterns = [
    path('assets_list/',views.AssetListView.as_view(),name="assetsList"),
    path('server-list/', views.ServerListView.as_view(), name="serverList"),
    path('mem-list/', views.MemoryListView.as_view(), name="memList"),
    path('disk-list/', views.DiskListView.as_view(), name="diskList"),
    path('server_detail/<slug:pk>/',views.ServerDetailView.as_view(),name="server_detail"),
    path('asset_detail/<slug:pk>/',views.AssetsDetailView.as_view(),name="assets_detail"),
    path('servers/',views.ServerListView.as_view(),name="servers"),
]