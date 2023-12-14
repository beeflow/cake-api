from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from cake.models import Cake
from cake.serializers import CakeSerializer

response_update_retrieve_schema_dict = {
    "404": openapi.Response(
        description="Cake not found",
    ),
}
response_create_schema_dict = {
    "201": openapi.Response(
        description="The request has succeeded and has led to the creation of a resource",
    ),
}
response_destroy_schema_dict = {
    "204": openapi.Response(
        description="The request has succeeded, but that the client doesn't need to navigate away from its current "
        "page",
    ),
    "404": openapi.Response(
        description="Cake not found",
    ),
}


@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(responses=response_update_retrieve_schema_dict),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(responses=response_update_retrieve_schema_dict),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(responses=response_destroy_schema_dict),
)
@method_decorator(name="create", decorator=swagger_auto_schema(responses=response_create_schema_dict))
class CakeViewSet(viewsets.ModelViewSet):
    """
    ViewSet to handle Cake RestAPI methods

    list: Get list of Cakes
    create: Create new Cake
    retrieve: Get specific Cake by ID
    update: Update selected Cake
    destroy: Remove Cake
    """

    serializer_class = CakeSerializer
    queryset = Cake.objects.all()
