from unittest import TestCase

from django.db.models import Count, Avg
from django.db.models import Avg, Q
from django_mock_queries.query import MockSet, MockModel
from django.urls import resolve,reverse
from django.test import SimpleTestCase,TestCase,Client
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from unittest.mock import patch, MagicMock
from rest_framework.test import APITestCase
from rest_framework import status
from A1HW.models import CarBrand, Owner, Car
from A1HW.serializers import CarBrandSerializer, StatisticSerializer, StatisticSerializerOwnerCarBrandEmploy
from A1HW.viewsFolder import CarBrandAPIView
from unittest.mock import Mock

from django.test import TestCase
from rest_framework.test import APIClient


class APIUrlsTests(APITestCase):

    statistic_url=reverse('statisticAvgProdyear')
    statistic2_url=reverse('statisticAvgBrandEmployees')

    def test_statistics_url(self):
        url = reverse("statisticAvgProdyear")
        self.assertEqual(resolve(url).route, "averageprodyear/")

    def test_statistics2_url(self):
        url = reverse("statisticAvgBrandEmployees")
        self.assertEqual(resolve(url).route, "averagebrandemployees/")

    def test_get_statistic1(self):
        response = self.client.get(self.statistic_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_statistic2(self):
        response2 = self.client.get(self.statistic2_url)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)


class StatisticSerializerTest(TestCase):
    def setUp(self):
        self.car_brand = CarBrand.objects.create(
            CarBrand='Tesla',
            Founded='2003',
            CEO='Elon Musk',
            NumberOfEmployees=50000,
            NetIncome='$21.5 billion',
        )
        self.owner1=Owner.objects.create(CNP="1234567890123")
        self.owner2 = Owner.objects.create(CNP="1234567890124")
        self.car1 = self.car_brand.cars.create(OwnerCNP=self.owner1,ProductionYear=2018)
        self.car2 = self.car_brand.cars.create(OwnerCNP=self.owner2,ProductionYear=2020)

    def test_serializer(self):
        mock_statistics = Mock(
            avg_production_year=2019,
            car_count=2,
            id=self.car_brand.id,
            CarBrand=self.car_brand.CarBrand,
        )
        serializer = StatisticSerializer(instance=mock_statistics)
        expected_data = {
            'id': self.car_brand.id,
            'CarBrand': self.car_brand.CarBrand,
            'avg_production_year': 2019,
            'car_count': 2,
        }
        self.assertEqual(serializer.data, expected_data)


class StatisticOwnerCarBrandEmployTests(TestCase):
    def setUp(self):
        brand1 = CarBrand.objects.create(
            CarBrand='Brand1',
            Founded='1900',
            CEO='CEO1',
            NumberOfEmployees=1000,
            NetIncome='100M'
        )
        brand2 = CarBrand.objects.create(
            CarBrand='Brand2',
            Founded='1950',
            CEO='CEO2',
            NumberOfEmployees=2000,
            NetIncome='200M'
        )
        owner1 = Owner.objects.create(
            LastName='Doe',
            FirstName='John',
            CNP='1234567890123',
            Email='john.doe@example.com',
            Address='123 Main St'
        )
        owner2 = Owner.objects.create(
            LastName='Smith',
            FirstName='Jane',
            CNP='1234567890124',
            Email='jane.smith@example.com',
            Address='456 Elm St'
        )
        Car.objects.create(
            CarBrand=brand1,
            CarModel='Model1',
            ProductionYear=2020,
            SeatsNumber=4,
            Color='Red',
            OwnerCNP=owner1
        )
        Car.objects.create(
            CarBrand=brand2,
            CarModel='Model2',
            ProductionYear=2021,
            SeatsNumber=5,
            Color='Blue',
            OwnerCNP=owner2
        )
        Car.objects.create(
            CarBrand=brand2,
            CarModel='Model3',
            ProductionYear=2022,
            SeatsNumber=5,
            Color='Green',
            OwnerCNP=owner2
        )

    def test_statistic(self):
        client = APIClient()
        url = reverse('statisticAvgBrandEmployees')
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [
            {
                 'id':2,
                'LastName': 'Smith',
                'FirstName': 'Jane',
                'CNP':'1234567890124',
                'avg_employees': 2000.0,
                'no_cars': 2,
            },
            {
                'id':1,
                'LastName': 'Doe',
                'FirstName': 'John',
                'CNP':'1234567890123',
                'avg_employees': 1000.0,
                'no_cars': 1,
            },
        ]
        serializer = StatisticSerializerOwnerCarBrandEmploy(expected_data, many=True)
        self.assertEqual(response.data, serializer.data)