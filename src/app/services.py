from collections import defaultdict
from app.models import Application


def get_manufactures(contract_pk: int) -> dict:
    manufacture = defaultdict(list)
    applications = Application.objects.prefetch_related('product').filter(contract_id=contract_pk)
    for app in applications:
        manufacture['manufacture_id'] = app.product.all().values_list('manufacture_id', flat=True).distinct()
    return manufacture
