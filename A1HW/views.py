from django.views.decorators.csrf import csrf_exempt

from .models import Car,CarBrand,Owner,CarWorkshop,CarTunedBy
from django.http import JsonResponse
from rest_framework.response import Response

from rest_framework import status
from .serializers import StatisticSerializerOwnerCarBrandEmploy,StatisticSerializer,CarSerializer,CarBrandSerializer,OwnerSerializer,CarDetailSerializer,CarBrandDetailSerializer,OwnerDetailSerializer,CarWorkshopDetailSerializer,CarWorkshopSerializer,CarTunedBySerializer
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.db.models import Count, Q, Avg,Sum
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import  GenericAPIView,ListAPIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.views import APIView


class CarAPIView(APIView):

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





class CarBrandAPIView(APIView):

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


class OwnerAPIView(APIView):
    @api_view(['GET','POST'])
    def owner_list(request):
        if request.method == 'GET':
            owner = Owner.objects.all()
            serializer = OwnerSerializer(owner,many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            serializer = OwnerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


    @api_view(['GET','PUT','DELETE'])
    def owner_detail(request, id):
        try:
            owner = Owner.objects.get(pk=id)
        except Owner.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            # GET CERTAIN ID
            serializer = OwnerDetailSerializer(owner)
            return Response(serializer.data)
        elif request.method == 'PUT':
            # UPDATE CERTAIN ID
            serializer = OwnerSerializer(owner, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            owner.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class CarWorkshopAPIView(APIView):
    @api_view(['GET','POST'])
    def workshop_list(request):
        if request.method == 'GET':
            cw = CarWorkshop.objects.all()
            serializer = CarWorkshopSerializer(cw,many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            serializer = CarWorkshopSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


    @api_view(['GET','PUT','DELETE'])
    def workshop_detail(request, id):
        try:
            cw = CarWorkshop.objects.get(pk=id)
        except CarWorkshop.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            # GET CERTAIN ID
            serializer = CarWorkshopDetailSerializer(cw)
            return Response(serializer.data)
        elif request.method == 'PUT':
            # UPDATE CERTAIN ID
            serializer = CarWorkshopSerializer(cw, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            cw.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class CarTunedByAPIView(APIView):
    @api_view(['GET','POST'])
    def carstuned_list(request):
        if request.method == 'GET':
            ct = CarTunedBy.objects.all()
            serializer = CarTunedBySerializer(ct,many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            serializer = CarTunedBySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    @api_view(['GET', 'PUT', 'DELETE'])
    def carstuned_detail(request, id):
        try:
            cw = CarTunedBy.objects.get(pk=id)
        except CarTunedBy.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            # GET CERTAIN ID
            serializer = CarTunedBySerializer(cw)
            return Response(serializer.data)
        elif request.method == 'PUT':
            # UPDATE CERTAIN ID
            serializer = CarTunedBySerializer(cw, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            cw.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




class Statistics(APIView):
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

class StatisticOwnerCarBrandEmploy(APIView):
    @api_view(['GET'])
    def statistic(request):
        statistics = Owner.objects.annotate(
            avg_employees=Avg('cars__CarBrand__NumberOfEmployees'),
            no_cars=Count('cars')
        ).order_by('-avg_employees')

        serializer = StatisticSerializerOwnerCarBrandEmploy(statistics, many=True)
        return Response(serializer.data)



class MultipleCarBrandView(APIView):
    @csrf_exempt
    @api_view(['POST'])
    def bulkAdd(request):
        car_id_new_brand_list = request.data.get('car_id_new_brand_list')

        # Loop through the list of car ids and new car brands to update
        for item in car_id_new_brand_list:
            car = Car.objects.get(id=item['car_id'])
            car.CarBrand = CarBrand.objects.get(CarBrand=item['newcarbrand'])
            car.save()

        return Response({'message': 'Car brands updated successfully.'})

    # {
    #     "car_id_new_brand_list": [
    #         {"car_id": 1, "newcarbrand": "Toyota"},
    #         {"car_id": 2, "newcarbrand": "Audi"}
    #     ]
    # }