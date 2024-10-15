from rest_framework import generics
from .models import Addmoney_info
from .serializers import AddmoneyInfoSerializer

class AddmoneyInfoList(generics.ListCreateAPIView):
    queryset = Addmoney_info.objects.all()
    serializer_class = AddmoneyInfoSerializer

