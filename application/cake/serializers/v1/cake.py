"""copyright (c) 2014 - 2023 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from rest_framework.serializers import ModelSerializer

from cake.models import Cake


class CakeSerializer(ModelSerializer):
    class Meta:
        model = Cake
        fields = "__all__"
