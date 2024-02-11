from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema

from app.models import Contract, Manufacture, Application, Product
from app.serializers import ContractSerializer, ApplicationCreationSerializer, ManufactureResponseSerializer
from app.services import get_manufactures


class ContractView(ModelViewSet):
    queryset = Contract.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ApplicationCreationSerializer
        return ContractSerializer

    @extend_schema(
        responses=ManufactureResponseSerializer,
    )
    def retrieve(self, request, pk=None, *args, **kwargs):
        manufactures = get_manufactures(pk)
        serializer = ManufactureResponseSerializer(manufactures)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=ApplicationCreationSerializer,
        responses={201: ContractSerializer},
        auth=None,
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            contract = Contract.objects.create()
            application = Application.objects.create(contract=contract)
            for product in serializer.data['products']:
                manufacture, _ = Manufacture.objects.get_or_create(name=product['manufacture'])
                Product.objects.create(
                    name=product['name'],
                    manufacture=manufacture,
                    application=application
                )
        return Response(status=status.HTTP_200_OK)
