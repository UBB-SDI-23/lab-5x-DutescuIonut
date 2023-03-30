"""A1HW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from A1HW import views
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
    path("cars/", views.CarAPIView.car_list),
    path("cars/<int:id>", views.CarAPIView.car_detail),
    path("carbrands/", views.CarBrandAPIView.carBrand_list),
    #path("carbrands/<int:id>", views.CarBrandAPIView.carBrand_detail),
    path('carbrands/<str:name>', views.CarBrandAPIView.carBrand_detail),
    path("owners/", views.OwnerAPIView.owner_list),
    path("owners/<int:id>", views.OwnerAPIView.owner_detail),
    path("carworkshops/", views.CarWorkshopAPIView.workshop_list),
    path("carworkshops/<int:id>", views.CarWorkshopAPIView.workshop_detail),
    path("carstuned/",views.CarTunedByAPIView.carstuned_list),
    path("carstuned/<int:id>",views.CarTunedByAPIView.carstuned_detail),
    path("averageprodyear/", views.Statistics.statistic, name="statisticAvgProdyear"),
    path("averagebrandemployees/",views.StatisticOwnerCarBrandEmploy.statistic, name="statisticAvgBrandEmployees"),
    path("multiplecarbrand/", views.MultipleCarBrandView.bulkAdd),


]
