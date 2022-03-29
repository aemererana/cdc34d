from django.db import models

from . import utils
from .user import User
from .group import Group

class GroupMembers(utils.CustomModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    belongingGroup = models.ForeignKey(Group, on_delete=models.CASCADE)
    joinedOn = models.DateTimeField(auto_now_add=True)
