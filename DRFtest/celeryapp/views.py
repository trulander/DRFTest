from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .tasks import create_new_object

@api_view(['GET'])
def asycn_job(request):
    result = create_new_object.apply_async(ignore_result=True)
    return Response('result')

# Create your views here.
