from rest_framework import viewsets
from django.views.generic import ListView
from django.views import View
from django.http import JsonResponse

from cmdb.models import Asset,TreeNode
from .serializers import AssetSerializer, TreeNodeSerializer
from .page import StandardResultsSetPagination


class ServerTreeViewSet(viewsets.ModelViewSet):
    queryset = TreeNode.objects.filter(node_upstream=None)
    serializer_class = TreeNodeSerializer

class AssetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    pagination_class = StandardResultsSetPagination

class AssetApi(View):
    def get(self, request):
        users = Asset.objects.values()
        return JsonResponse(list(users), safe=False)

