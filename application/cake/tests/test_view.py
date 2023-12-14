from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from cake.models import Cake
from cake.serializers import CakeSerializer


class CakeViewSetV1Test(APITestCase):
    def setUp(self):
        self.cake_data = {
            "name": "Test Cake",
            "comment": "Test comment",
            "image_url": "https://example.com/cake.jpg",
            "yum_factor": 4,
        }
        self.cake = Cake.objects.create(**self.cake_data)

    def test_list_cakes(self):
        url = reverse("cake_v1:cakes")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_cake(self):
        url = reverse("cake_v1:cake", kwargs={"pk": self.cake.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_cake(self):
        url = reverse("cake_v1:cakes")
        response = self.client.post(url, self.cake_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_cake(self):
        url = reverse("cake_v1:cake", kwargs={"pk": self.cake.pk})
        updated_data = {
            "name": "Updated Cake",
            "comment": "Updated comment",
            "image_url": "https://example.com/updated-cake.jpg",
            "yum_factor": 5,
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_cake(self):
        url = reverse("cake_v1:cake", kwargs={"pk": self.cake.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_cakes_failure(self):
        # Test listing cakes when there are none in the database
        url = reverse("cake_v1:cakes")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Adjust the expected status code as needed

    def test_retrieve_cake_failure(self):
        # Test retrieving a cake with an invalid ID
        invalid_id = 9999  # An ID that doesn't exist
        url = reverse("cake_v1:cake", kwargs={"pk": invalid_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_cake_failure(self):
        # Test updating a cake with invalid data
        invalid_id = 9999  # An ID that doesn't exist
        url = reverse("cake_v1:cake", kwargs={"pk": invalid_id})
        invalid_data = {"name": "Invalid Cake"}  # Invalid data to update
        response = self.client.put(url, invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_destroy_cake_failure(self):
        # Test deleting a cake with an invalid ID
        invalid_id = 9999  # An ID that doesn't exist
        url = reverse("cake_v1:cake", kwargs={"pk": invalid_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_cakes_data(self):
        # Creating test cakes for listing
        Cake.objects.create(
            name="Test Cake 1",
            comment="Test comment 1",
            image_url="https://example.com/cake1.jpg",
            yum_factor=3,
        )
        Cake.objects.create(
            name="Test Cake 2",
            comment="Test comment 2",
            image_url="https://example.com/cake2.jpg",
            yum_factor=4,
        )

        url = reverse("cake_v1:cakes")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the content of the response data
        cakes = Cake.objects.all()
        serializer = CakeSerializer(cakes, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_cake_data(self):
        # Creating a test cake for retrieval
        test_cake = Cake.objects.create(
            name="Test Cake",
            comment="Test comment",
            image_url="https://example.com/cake.jpg",
            yum_factor=4,
        )

        url = reverse("cake_v1:cake", kwargs={"pk": test_cake.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the content of the response data
        serializer = CakeSerializer(test_cake)
        self.assertEqual(response.data, serializer.data)

    def test_create_cake_data(self):
        url = reverse("cake_v1:cakes")
        new_cake_data = {
            "name": "New Test Cake",
            "comment": "New Test comment",
            "image_url": "https://example.com/new-cake.jpg",
            "yum_factor": 5,
        }
        response = self.client.post(url, new_cake_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the content of the created cake
        created_cake = Cake.objects.get(name="New Test Cake")
        serializer = CakeSerializer(created_cake)
        self.assertEqual(response.data, serializer.data)
