from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from A1HW.models import Owner
from A1HW.serializers import OwnerSerializer, OwnerDetailSerializer


class OwnerAPIView(APIView):
    @extend_schema(responses={201: OwnerSerializer}, )
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

    @extend_schema(responses={201: OwnerDetailSerializer}, )
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
