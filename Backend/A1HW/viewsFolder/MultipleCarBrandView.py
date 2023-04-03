from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from A1HW.models import Car, CarBrand


class MultipleCarBrandViewAPI(APIView):

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