from urllib.request import Request
from django.contrib.auth.middleware import get_user
from django.http import HttpResponse
from messenger_backend.models import Message, Conversation
from rest_framework.views import APIView

class ReadMessages(APIView):

    def put(self, request : Request):
        user = get_user(request)

        if user.is_anonymous:
            return HttpResponse(status=401)

        reading_person_id = user.id
        body = request.data
        conversation_id = body.get("conversationId")


        # if convo id is not supplied
        # send 400
        if not conversation_id:
            return HttpResponse(status=400)

        try:
            conversation = Conversation.objects.get(pk=conversation_id)

            # check if user has authority on the conversation
            # error 403 if not
            if(conversation.user1_id != reading_person_id and conversation.user2_id != reading_person_id):
                return HttpResponse(status=403)

        except Conversation.DoesNotExist:
            # not found
            return HttpResponse(status=404)

        # get messages where the other party is
        # the sender and hasn't been read.
        Message.objects.filter(conversation=conversation_id).exclude(senderId=reading_person_id, isRead=True).update(isRead=True)

        return HttpResponse(status=204)
