import factory

from app.models import Contract, Manufacture, Application, Product


class ContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contract


class ApplicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Application
    contract = factory.SubFactory(ContractFactory)


class ManufactureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Manufacture
    name = factory.Faker('company')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    name = factory.Faker('bs')
    manufacture = factory.SubFactory(ManufactureFactory)
    application = factory.SubFactory(ApplicationFactory)

