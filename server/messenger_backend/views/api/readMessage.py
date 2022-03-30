from urllib.request import Request
from django.contrib.auth.middleware import get_user
from django.http import HttpResponse, JsonResponse
from messenger_backend.models import Message, Conversation
from rest_framework.views import APIView

class ReadMessages(APIView):

    def get(self, request : Request):
        try:
            user = get_user(request)

            if user.is_anonymous:
                return HttpResponse(status=401)

            reading_person_id = user.id
            body = request.query_params
            conversation_id = body.get("conversationId")
            recipient_id = body.get("recipientId")


            # if convo id is supplied then use it
            # otherwise find it and if none found
            # send error
            if not conversation_id:
                conversation = Conversation.find_conversation(reading_person_id, recipient_id)
                if conversation:
                    conversation_id = conversation["id"]

            if conversation_id:
                messages = Message.objects.filter(conversation=conversation_id)
                for msg in messages:
                    if msg.senderId != reading_person_id and msg.isRead is not True:
                        msg.isRead = True
                        msg.save()
                
                return JsonResponse({"result": "ok"})


            # the data supplied did not return a valid conversation
            return HttpResponse(status=400)

        except Exception as e:
            return HttpResponse(status=500)
