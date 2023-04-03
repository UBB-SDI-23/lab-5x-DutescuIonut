from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from A1HW.models import CarTunedBy
from A1HW.serializers import CarTunedBySerializer


class CarTunedByAPIView(APIView):
    @extend_schema( responses={201: CarTunedBySerializer},)
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

