from django.db import models
from django.db.models import Q

from . import utils
from .user import User
from .group import Group


class Conversation(utils.CustomModel):

    user1 = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column="user1Id", related_name="+", null=True
    )
    user2 = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column="user2Id", related_name="+", null=True
    )
    groupId = models.OneToOneField(Group, on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, db_index=True)
    updatedAt = models.DateTimeField(auto_now=True)

    # find conversation given two user Ids
    def find_conversation(user1Id, user2Id):
        # return conversation or None if it doesn't exist
        try:
            return Conversation.objects.get(
                (Q(user1__id=user1Id) | Q(user1__id=user2Id)),
                (Q(user2__id=user1Id) | Q(user2__id=user2Id)),
            )
        except Conversation.DoesNotExist:
            return None

    def find_conversation_by_group(groupId):
            try:
                return Conversation.objects.get(groupId=groupId)
            except Conversation.DoesNotExist:
                return None   