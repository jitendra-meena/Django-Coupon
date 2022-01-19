from dataclasses import fields
from rest_framework.serializers import Serializer
from rest_framework import serializers
from coupon.models import Coupon


class Coupon_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class Coupon_UseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon 
        fields = '__all__'