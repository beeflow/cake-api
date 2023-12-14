"""copyright (c) 2014 - 2023 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.core.exceptions import ValidationError
from django.db.utils import DataError, IntegrityError
from django.test import TestCase
from faker import Faker

from cake.models import Cake


class TestModel(TestCase):
    def test_incorrect_name(self):
        with self.assertRaises(DataError):
            Cake.objects.create(
                name=Faker().pystr(min_chars=31, max_chars=201),
                comment=Faker().text(max_nb_chars=200),
                image_url=Faker().url(),
                yum_factor=Faker().pyint(min_value=1, max_value=5),
            )

    def test_incorrect_comment(self):
        with self.assertRaises(DataError):
            Cake.objects.create(
                name=Faker().word(),
                comment=Faker().pystr(min_chars=201, max_chars=201),
                image_url=Faker().url(),
                yum_factor=Faker().pyint(min_value=1, max_value=5),
            )

    def test_incorrect_image_url(self):
        invalid_image_cake = Cake.objects.create(
            name=Faker().word(),
            comment=Faker().text(max_nb_chars=200),
            image_url=Faker().word(),
            yum_factor=Faker().pyint(min_value=1, max_value=5),
        )

        with self.assertRaises(ValidationError):
            invalid_image_cake.full_clean()

    def test_incorrect_yum_factor(self):
        with self.assertRaises(IntegrityError):
            Cake.objects.create(
                name=Faker().word(),
                comment=Faker().text(max_nb_chars=200),
                image_url=Faker().url(),
                yum_factor=Faker().pyint(min_value=6),
            )

    def test_create_model_success(self):
        name = Faker().word()
        comment = Faker().text(max_nb_chars=200)
        image_url = Faker().url()
        yum_factor = Faker().pyint(min_value=1, max_value=5)

        cake = Cake.objects.create(name=name, comment=comment, image_url=image_url, yum_factor=yum_factor)

        cake.refresh_from_db()

        self.assertEqual(cake.name, name)
        self.assertEqual(cake.comment, comment)
        self.assertEqual(cake.image_url, image_url)
        self.assertEqual(cake.yum_factor, yum_factor)

    def test_to_str(self):
        name = Faker().word()

        cake = Cake.objects.create(
            name=name,
            comment=Faker().text(max_nb_chars=200),
            image_url=Faker().url(),
            yum_factor=Faker().pyint(min_value=1, max_value=5),
        )

        cake.refresh_from_db()

        self.assertEqual(str(cake), name)
