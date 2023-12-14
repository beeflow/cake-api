"""copyright (c) 2014 - 2023 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.urls import path

from cake import views

app_name = "cake_v1"

urlpatterns = [
    path(
        "cake",
        views.CakeViewSetV1.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="cakes",
    ),
    path(
        "cake/<int:pk>",
        views.CakeViewSetV1.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="cake",
    ),
]
