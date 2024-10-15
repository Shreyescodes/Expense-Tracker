from rest_framework import serializers
from .models import Addmoney_info

class AddmoneyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addmoney_info
        fields = ['id', 'user', 'add_money', 'quantity', 'Date', 'Category']

