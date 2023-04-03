from django.db.models import Avg, Count
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from A1HW.models import Owner
from A1HW.serializers import StatisticSerializerOwnerCarBrandEmploy


class StatisticOwnerCarBrandEmploy(APIView):
    @extend_schema( responses={201: StatisticSerializerOwnerCarBrandEmploy},)
    @api_view(['GET'])
    def statistic(request):
        statistics = Owner.objects.annotate(
            avg_employees=Avg('cars__CarBrand__NumberOfEmployees'),
            no_cars=Count('cars')
        ).order_by('-avg_employees')

        serializer = StatisticSerializerOwnerCarBrandEmploy(statistics, many=True)
        return Response(serializer.data)

