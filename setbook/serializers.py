from rest_framework import serializers
from .models import HeroInfo

class HeroSerializer(serializers.ModelSerializer):
    hbook_id = serializers.IntegerField(help_text='图书编号')

    class Meta:
        model = HeroInfo
        fields = '__all__'
