from rest_framework import serializers
from .models import *


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongFiles
        fields = ('id', 'name', 'duration', 'upload_time')


class PodCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodCastFiles
        fields = ('id', 'name', 'duration', 'upload_time', 'host', 'participants')


class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBookFiles
        fields = ('id', 'title', 'author', 'narrator' , 'duration', 'upload_time')