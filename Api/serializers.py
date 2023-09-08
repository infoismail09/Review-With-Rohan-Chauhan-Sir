from rest_framework import serializers

class CustomizedDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    msg = serializers.CharField()