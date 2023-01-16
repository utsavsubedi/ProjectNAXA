from rest_framework import serializers
from api.models import Address, Budget, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
