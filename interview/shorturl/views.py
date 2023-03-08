from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import urlShortModel
from django.shortcuts import redirect


# Create your views here.


@api_view(['POST'])
def shortURL(request):
    data = request.data
    url = urlShortModel.objects.create(
        long_url=data['url']
    )
    print(url.uuid)
    print(str(url.uuid))
    shorturl = "http://localhost:8000/shorten/" + str(url.uuid)
    return Response({'longurl': url.long_url, 'shorturl': shorturl})


@api_view(['GET'])
def redirectToLong(request, pk):
    url = urlShortModel.objects.get(pk=pk)

    return redirect(url.long_url)