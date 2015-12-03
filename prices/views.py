from prices.models import Price
from prices.serializers import PriceSerializer
from rest_framework.permissions import AllowAny

from rest_framework import generics

class PricesList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class PriceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
