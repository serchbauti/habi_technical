from django.urls import reverse
from rest_framework.test import APITestCase
from restframework import status


class TestProperties(APITestCase):

    fixtures = (
        "test_data/properties.json",
        "test_data/status.json",
        "test_data/status_history.json",
    )

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("api:property_list")

    def test_list_properties(self):
        request = self.client_test.get(self.url)
        self.assertEqual(7, request.data.count())
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_property_detail(self):
        request = self.client_test.get(
            reverse(
                "enterprises:enterprise_detail",
                kwargs={"pk": self.property.id},
            )
        )
        self.assertEqual(request.status_code, status.HTTP_200_OK)
