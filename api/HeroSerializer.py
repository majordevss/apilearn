from rest_framework import serializers
from .models import Hero
  

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Hero
        fields = ('name', 'alias')
