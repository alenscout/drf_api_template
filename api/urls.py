from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .views import MFTFList, MOFTList

@api_view(['GET'])
def getRoutes(request):
    routes = [
    'api/moft',
    'api/mtft',
    ]
    return Response(routes)

urlpatterns = [
    path('', getRoutes),
    path('moft/', MOFTList.as_view()),
    path('mtft/', MFTFList.as_view()),
]