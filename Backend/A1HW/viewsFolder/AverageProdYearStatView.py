from django.db.models import Avg, Count
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from A1HW.models import CarBrand
from A1HW.serializers import StatisticSerializer


class Statistics(APIView):
     @extend_schema( responses={201: StatisticSerializer},)
     @api_view(['GET'])
     def statistic(request):
        statistics = CarBrand.objects.annotate(
            avg_production_year=Avg('cars__ProductionYear'),
            car_count=Count('cars')
        ).order_by('-avg_production_year')

        serializer = StatisticSerializer(statistics, many=True)
        return Response(serializer.data)

# Get all cars green-colored whose CarBrand company is founded after 1950, ordered by car production year.
#         # cars = Car.objects.filter(
#         #     Q(Color='Green'),
#         #     Q(CarBrand__Founded__gte='1950')
#         # ).order_by('ProductionYear')
#         #
#         # serializer = StatisticSerializer(cars, many=True)
#         #
#         # return Response(serializer.data)