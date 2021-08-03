from django.urls import path
from api.views.property import PropertyView

app_name = "properties"

property_list = PropertyView.as_view({"get": "list"})
property_detail = PropertyView.as_view({"get": "retrieve"})

urlpatterns = [
    path("properties", property_list, name="property_list"),
    path("properties/<int:pk>", property_detail, name="property_detail"),
]
