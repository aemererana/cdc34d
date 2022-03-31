from django.db import models


from .user import User
from . import utils

class Group(utils.CustomModel):
    name = models.TextField(null=True)
    membership = models.ManyToManyField(User, through="GroupMembers", related_name='+')
    startedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    createdAt = models.DateTimeField(auto_now_add=True, db_index=True)
    updatedAt = models.DateTimeField(auto_now=True)