from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from A1HW.models import CarWorkshop
from A1HW.serializers import CarWorkshopSerializer, CarWorkshopDetailSerializer


class CarWorkshopAPIView(APIView):
    @extend_schema( responses={201: CarWorkshopSerializer},)
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

    @extend_schema(responses={201: CarWorkshopDetailSerializer}, )
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