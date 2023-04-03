"""A1HW URL Configuration

The `urlpatterns` list routes URLs to viewsFolder. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function viewsFolder
    1. Add an import:  from my_app import viewsFolder
    2. Add a URL to urlpatterns:  path('', viewsFolder.home, name='home')
Class-based viewsFolder
    1. Add an import:  from other_app.viewsFolder import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from A1HW import views
from A1HW.viewsFolder import AverageProdYearStatView,CarBrandView,CarTunedByView,CarView,CarWorkshopView
from A1HW.viewsFolder import  OwnerView ,OwnerCarBrandEmployStatView,MultipleCarBrandView

from rest_framework import routers
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from rest_framework import  permissions

# schema_view = get_schema_view(openapi.Info
#                               (title="REST API",
#                                default_version="1.0.0",
#                                description="Documentation for API"),
#                               public=True,
#                               permission_classes= [permissions.AllowAny], )
#



urlpatterns = [
    #path("doc/", schema_view.with_ui("swagger", cache_timeout=0), name="swaggerUI"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("admin/", admin.site.urls),
    path("cars/", CarView.CarAPIView.car_list),
    path("cars/<int:id>",CarView.CarAPIView.car_detail),
    path("carbrands/", CarBrandView.CarBrandAPIView.carBrand_list),
    #path("carbrands/<int:id>", viewsFolder.CarBrandAPIView.carBrand_detail),
    path('carbrands/<str:name>', CarBrandView.CarBrandAPIView.carBrand_detail),
    path("owners/", OwnerView.OwnerAPIView.owner_list),
    path("owners/<int:id>", OwnerView.OwnerAPIView.owner_detail),
    path("carworkshops/",CarWorkshopView.CarWorkshopAPIView.workshop_list),
    path("carworkshops/<int:id>", CarWorkshopView.CarWorkshopAPIView.workshop_detail),
    path("carstuned/", CarTunedByView.CarTunedByAPIView.carstuned_list),
    path("carstuned/<int:id>", CarTunedByView.CarTunedByAPIView.carstuned_detail),
    path("averageprodyear/", AverageProdYearStatView.Statistics.statistic, name="statisticAvgProdyear"),
    path("averagebrandemployees/", OwnerCarBrandEmployStatView.StatisticOwnerCarBrandEmploy.statistic, name="statisticAvgBrandEmployees"),
    path("multiplecarbrand/", MultipleCarBrandView.MultipleCarBrandViewAPI.bulkAdd),


]
