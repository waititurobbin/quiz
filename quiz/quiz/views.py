from rest_framework.decorators import api_view
from rest_framework.respose import Response
from rest_framework import status

def index(request):
    message = 'This is the test url'
    return Response(data=message, status=status.HTTP_200_OK)
