#process of going from python object to JSON
from rest_framework import serializers
from .models import Car,CarBrand,Owner,CarWorkshop,CarTunedBy


class CarSerializer(serializers.ModelSerializer):
    CarBrand = serializers.SlugRelatedField(queryset=CarBrand.objects.all(), slug_field='CarBrand')
    CarModel = serializers.CharField(max_length=200)
    ProductionYear = serializers.IntegerField(default=0)
    SeatsNumber = serializers.IntegerField(default=0)
    Color = serializers.CharField(max_length=50)
    OwnerCNP = serializers.SlugRelatedField(queryset=Owner.objects.all(), slug_field='CNP')


    class Meta:
        model = Car
        fields = ['id', 'CarBrand', 'CarModel', 'ProductionYear',
                  'SeatsNumber', 'Color', 'OwnerCNP']

    def validate_ProductionYear(self, value):

        if value < 1900:
            raise serializers.ValidationError("ProductionYear cannot be less than 1900")
        return value

    def validate_SeatsNumber(self,value):
        if value<2:
            raise serializers.ValidationError("SeatsNumber cannot be less than 2")
        return value



class CarTunedBySerializer(serializers.ModelSerializer):
   CarID = serializers.SlugRelatedField(queryset=Car.objects.all(), slug_field='id')
   CarWorkshopID = serializers.SlugRelatedField(queryset=CarWorkshop.objects.all(), slug_field='id')

   class Meta:
        model = CarTunedBy
        fields =['id', 'CarID', 'CarWorkshopID','DateTuned','TuningPrice']


class CarDetailSerializer(serializers.ModelSerializer):
    workshops = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Car
        fields = ['id', 'CarBrand', 'CarModel', 'ProductionYear',
                  'SeatsNumber', 'Color', 'OwnerCNP', 'workshops']
        depth = 1

    def get_workshops(self,obj):
        workshops = CarTunedBy.objects.filter(CarID=obj)
        return CarTunedBySerializer(workshops, many=True).data

    def validate_ProductionYear(self, value):

        if value < 1900:
            raise serializers.ValidationError("ProductionYear cannot be less than 1900")
        return value

    def validate_SeatsNumber(self,value):
        if value<2:
            raise serializers.ValidationError("SeatsNumber cannot be less than 2")
        return value


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ['id', 'CarBrand', 'Founded', 'CEO', 'NumberOfEmployees', 'NetIncome']

    def validate_NumberOfEmployees(self,value):
        if value<1:
            raise serializers.ValidationError("There must be atleast one employee.")
        return value


class CarBrandDetailSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = CarBrand
        fields = ['id', 'CarBrand', 'Founded', 'CEO', 'NumberOfEmployees', 'NetIncome', 'cars']

    def validate_NumberOfEmployees(self,value):
        if value<1:
            raise serializers.ValidationError("There must be atleast one employee.")
        return value


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'LastName', 'FirstName', 'CNP', 'Email', 'Address']

    def validate_CNP(self,value):
        if len(value)!=13:
            raise serializers.ValidationError("CNP invalid")
        return value


class OwnerDetailSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ['id', 'LastName', 'FirstName', 'CNP', 'Email', 'Address', 'cars']

    def validate_CNP(self, value):
        if len(value) != 13:
            raise serializers.ValidationError("CNP invalid")
        return value

class CarWorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWorkshop
        fields = ['id', 'Name', 'Owner', 'Founded', 'Location', 'NumberOfEmployees']

    def validate_NumberOfEmployees(self,value):
        if value<1:
            raise serializers.ValidationError("There must be atleast one employee.")
        return value


class CarWorkshopDetailSerializer(serializers.ModelSerializer):
    carsTuned = serializers.SerializerMethodField()

    class Meta:
        model = CarWorkshop
        fields = ['id', 'Name', 'Owner', 'Founded', 'Location', 'NumberOfEmployees','carsTuned']

    def get_carsTuned(self,obj):
        carsTuned = CarTunedBy.objects.filter(CarWorkshopID=obj)
        return CarTunedBySerializer(carsTuned, many=True).data

    def validate_NumberOfEmployees(self,value):
        if value<1:
            raise serializers.ValidationError("There must be atleast one employee.")
        return value


class StatisticSerializer(serializers.ModelSerializer):
    avg_production_year = serializers.IntegerField(read_only=True)
    car_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = CarBrand
        fields = ['id', 'CarBrand', 'avg_production_year', 'car_count']
    # CarBrand = serializers.CharField(source='CarBrand.CarBrand')
    #
    # class Meta:
    #     model = Car
    #     fields = [ 'id', 'Color', 'ProductionYear', 'CarBrand']


class StatisticSerializerOwnerCarBrandEmploy(serializers.ModelSerializer):
    avg_employees = serializers.IntegerField(read_only=True)
    no_cars = serializers.IntegerField(read_only=True)

    class Meta:
        model = Owner
        fields = ['id', 'LastName', 'FirstName', 'CNP', 'avg_employees', 'no_cars']

