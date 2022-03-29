from django.db import models


from .groupMembers import GroupMembers
from .user import User
from . import utils

class Group(utils.CustomModel):
    name = models.TextField()
    membership = models.ManyToManyField(User, through=GroupMembers)
    startedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, db_index=True)
    updatedAt = models.DateTimeField(auto_now=True)