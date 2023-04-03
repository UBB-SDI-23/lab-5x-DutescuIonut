from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from A1HW.models import Car
from A1HW.serializers import CarSerializer, CarDetailSerializer


class CarAPIView(APIView):
    @extend_schema( responses={201: CarSerializer},)
    @api_view(['GET', 'POST'])
    def car_list(request):
        id = request.query_params.get('id')
        productionyear = request.query_params.get('productionyear')
        if request.method== 'GET':
            #GET REQUEST
            if id:
                # Filter by ID
                # .../cars/?id=X
                cars = Car.objects.filter(id=id)
            elif productionyear:
                #.../cars/?productionyear=X
                #WILL RETRIEVE CARS WITH PRODUCTION YEAR > given production year in url
                cars = Car.objects.filter(ProductionYear__gt=productionyear)

            else:
                # No filters applied, return all cars
                cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)
        if request.method=='POST':

            serializer = CarSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(status=status.HTTP_404_NOT_FOUND)

    @extend_schema(responses={201: CarDetailSerializer}, )
    @api_view(['GET','PUT','DELETE'])
    def car_detail(request, id):
        try:
            car=Car.objects.get(pk=id)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            #GET CERTAIN ID
            serializer = CarDetailSerializer(car)
            return Response(serializer.data)
        elif request.method == 'PUT':
            #UPDATE CERTAIN ID
            serializer= CarDetailSerializer(car,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        elif request.method=='DELETE':
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

