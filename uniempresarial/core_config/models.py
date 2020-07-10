from django.db import models

# Create your models here.
from django.db import models
from common.models import BaseModel, User


# Create your models here.
class Faculty(BaseModel):
    external_id = models.CharField(max_length=15, unique=True, null=True)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}{}'.format(self.id, self.name)


class Program(BaseModel):
    external_id = models.CharField(max_length=15, unique=True, null=True)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}{}'.format(self.id, self.name)


class ScheduleModel(BaseModel):
    external_id = models.CharField(max_length=15, unique=True, null=True)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}{}'.format(self.id, self.name)


class PromotionModel(BaseModel):
    external_id = models.CharField(max_length=15, unique=True, null=True)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}{}'.format(self.id, self.name)


class AccountModel(BaseModel):
    code_id = models.CharField(max_length=15, unique=True)
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    schedule = models.ForeignKey(ScheduleModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}{}'.format(self.code_id, self.auth_user)


class StateModel(BaseModel):
    external_id = models.CharField(max_length=15, unique=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}{}'.format(self.id, self.name)


class ModuleConfig(BaseModel):
    external_id = models.CharField(max_length=15, unique=True, null=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    status = models.ForeignKey(StateModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}{}'.format(self.id, self.name)


class RolConfig(BaseModel):
    external_id = models.CharField(max_length=15, unique=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    status = models.ForeignKey(StateModel, related_name='status', on_delete=models.CASCADE)
    modules = models.ManyToManyField(ModuleConfig, related_name='modules')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}{}'.format(self.id, self.name)


class RolUser(BaseModel):
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    config = models.ForeignKey(RolConfig, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}{}'.format(self.id, self.name)
