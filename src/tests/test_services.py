import pytest
from app.services import get_manufactures
from app.models import Manufacture, Product
from tests.factories import ApplicationFactory, ProductFactory, ManufactureFactory


@pytest.mark.django_db
def test__get_manufactures_by_app_id():
    application = ApplicationFactory()
    manufacture_1 = ManufactureFactory()
    manufacture_2 = ManufactureFactory()
    for i in range(2):
        ProductFactory(manufacture=manufacture_2, application=application)
        ProductFactory(manufacture=manufacture_1, application=application)
    manufactures = get_manufactures(application.contract_id)
    assert Manufacture.objects.all().count() == 2
    assert Product.objects.all().count() == 4
    assert manufactures['manufacture_id'].count() == 2


@pytest.mark.django_db
def test__get_manufactures_by_app_id__empty():
    application = ApplicationFactory()
    manufacture_1 = ManufactureFactory()
    manufacture_2 = ManufactureFactory()
    for i in range(2):
        ProductFactory(manufacture=manufacture_2, application=application)
        ProductFactory(manufacture=manufacture_1, application=application)
    manufactures = get_manufactures(123)
    assert Manufacture.objects.all().count() == 2
    assert Product.objects.all().count() == 4
    assert manufactures['manufacture_id'] == []
