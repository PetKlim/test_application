from collections import defaultdict
from app.models import Application


def get_manufactures(contract_pk: int) -> dict:
    manufacture = defaultdict(list)
    applications = (Application.objects.
                    filter(contract_id=contract_pk).
                    values_list('product__manufacture_id', flat=True).
                    distinct())
    manufacture['manufacture_id'] = applications
    return manufacture
