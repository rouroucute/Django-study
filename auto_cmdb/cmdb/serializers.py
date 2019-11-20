from rest_framework import serializers
from .models import Asset,Server,Memory,Disk,TreeNode
class AssetSerializer(serializers.ModelSerializer):  
      device_type = serializers.SerializerMethodField()
      device_status = serializers.SerializerMethodField()
      class Meta:
            model = Asset
            fields = "__all__"
      def get_device_type(self,obj):
            return obj.get_device_type_id_display()

      def get_device_status(self,obj):
            return obj.get_device_status_id_display()

class ServerSerializer(serializers.ModelSerializer):
      class Meta:
            model = Server
            fields = "__all__"
class MemorySerializer(serializers.ModelSerializer):
      class Meta:
            model = Memory
            fields = "__all__"
class DiskSerializer(serializers.ModelSerializer):
      class Meta:
            model = Disk
            fields = "__all__"

##组件序列化

