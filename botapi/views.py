from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from django.http import JsonResponse
import json
from django.views.generic import View
# Create your views here.

class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """


    chatterbot = ChatBot(**settings.CHATTERBOT)



    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """

        input_data = json.loads(request.body)['user']
        print(input_data)
        input_data = input_data.replace('-', '')
        input_data = input_data.replace(',', '')
        input_data = input_data.replace('?', '')
        input_data = input_data.replace('.', '')
        input_data = input_data.replace('/', '')
        input_data = input_data.replace('%', '')
        input_data = input_data.replace('"', '')
        input_data = input_data.replace('#', '')
        input_data = input_data.replace('*', '')
        input_data = input_data.replace('^', '')
        input_data = input_data.lower()


        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()
        

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
