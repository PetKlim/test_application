from rest_framework import serializers

from app.models import Contract


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'


class ManufactureResponseSerializer(serializers.Serializer):

    manufacture_id = serializers.ListField(allow_empty=True)


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(label='Name', allow_blank=False, max_length=256)
    manufacture = serializers.CharField(label='Manufacture', allow_blank=False, max_length=256)


class ApplicationCreationSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)


class ContractCreationSerializer(serializers.Serializer):
    application = ApplicationCreationSerializer()
