from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Contract(BaseModel):
    pass


class Application(BaseModel):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='application')


class Manufacture(BaseModel):
    name = models.CharField(max_length=256)


class Product(BaseModel):
    name = models.CharField(max_length=256)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, related_name='product')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='product')
