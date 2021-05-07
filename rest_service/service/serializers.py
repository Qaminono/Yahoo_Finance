from rest_framework import serializers
from .models import Data


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('id', 'company', 'date', 'open', 'high', 'low', 'close', 'adj_close', 'volume',)
