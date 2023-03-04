from rest_framework import serializers
from .models import *

class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"

class MainSerializers(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = "__all__"
    
class Give_order(serializers.ModelSerializer):
    class Meta:
        model = Give_order
        fields = "__all__"

class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class Product_infoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_info
        fields = "__all__"


class AdviceSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = "__all__"

class About_companySrializers(serializers.ModelSerializers):
    class Meta:
        model = About_company
        fields = "__all__"

class Korean_factSerializers(serializers.ModelSerializer):
    class Meta:
        model = Korean_fact
        fields = "__all__"

class About_teaSerializers(serializers.ModelSerializer):
    class Meta:
        model = About_tea
        fields = "__all__"
    
class Fact_numbersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fact_numbers
        fields = "__all__"

class Fill_formulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fill_formul
        fields = "__all__"