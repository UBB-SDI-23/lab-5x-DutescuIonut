from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from A1HW.models import CarBrand
from A1HW.serializers import CarBrandSerializer, CarBrandDetailSerializer


class CarBrandAPIView(APIView):
    @extend_schema( responses={201: CarBrandSerializer},)
    @api_view(['GET', 'POST'])
    def carBrand_list(request):

        if request.method == 'GET':
            carBrands = CarBrand.objects.all()
            serializer = CarBrandSerializer(carBrands,many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            serializer = CarBrandSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(responses={201: CarBrandDetailSerializer}, )
    @api_view(['GET','PUT','DELETE'])
    def carBrand_detail(request, name):
        try:
            carBrand = CarBrand.objects.get(CarBrand=name)
        except CarBrand.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            # GET CERTAIN ID
            serializer = CarBrandDetailSerializer(carBrand)
            return Response(serializer.data)
        if request.method == 'PUT':
            # UPDATE CERTAIN ID
            serializer = CarBrandSerializer(carBrand, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            carBrand.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)