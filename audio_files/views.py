from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import SongSerializer, PodCastSerializer, AudioBookSerializer
from .models import *
# Create your views here.
import pdb

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class FilesListApiView(APIView):
    def get_object(self, file_type):
        
        if (file_type == 'song') or (file_type == 'Song'):
            try:
                return SongFiles.objects.all()
            except SongFiles.DoesNotExist:
                return None

        elif (file_type == 'podcast') or (file_type == 'Podcast'):
            try:
                return PodCastFiles.objects.all()
            except PodCastFiles.DoesNotExist:
                return None
        
        elif (file_type == 'audiobook') or (file_type == 'Audiobook'):
            try:
                return AudioBookFiles.objects.all()
            except AudioBookFiles.DoesNotExist:
                return None

    
    def get(self, request, file_type, *args, **kwargs):

        file_instance = self.get_object(file_type)
        if not file_instance:
            return Response(
                {"res": "Object with file id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if (file_type == 'song') or (file_type == 'Song'):
            serializer = SongSerializer(file_instance, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif (file_type == 'podcast') or (file_type == 'Podcast'):
            serializer = PodCastSerializer(file_instance, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif (file_type == 'audiobook') or (file_type == 'Audiobook'):
            serializer = AudioBookSerializer(file_instance, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, *args, **kwargs):
        
        if request.data.get('audioFileType') == 'song':
            data = {
                'name':request.data.get('name'),
                'duration':request.data.get('duration')   
            }
            serializer = SongSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.data.get('audioFileType') == 'podcast':
            data = {
                'name':request.data.get('name'),
                'duration':request.data.get('duration'),
                'host':request.data.get('host'),
                'participants':request.data.get('participants')
            }
            serializer = PodCastSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.data.get('audioFileType') == 'audiobook':
            data = {
                'title':request.data.get('title'),
                'author':request.data.get('author'),
                'narrator':request.data.get('narrator'),
                'duration':request.data.get('duration')
            }
            serializer = AudioBookSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class FileDetailApiView(APIView):
    # http_method_names = ['get', 'head', 'delete', 'put']

    def get_object(self, file_type, file_id):

        if (file_type == 'song') or (file_type == 'Song'):
            try:
                return SongFiles.objects.get(id=file_id)
            except SongFiles.DoesNotExist:
                return None

        elif (file_type == 'podcast') or (file_type == 'Podcast'):
            try:
                return PodCastFiles.objects.get(id=file_id)
            except PodCastFiles.DoesNotExist:
                return None
        
        elif (file_type == 'audiobook') or (file_type == 'Audiobook'):
            try:
                return AudioBookFiles.objects.get(id=file_id)
            except AudioBookFiles.DoesNotExist:
                return None

    
    def get(self, request, file_type, file_id, *args, **kwargs):

        file_instance = self.get_object(file_type, file_id)
        if not file_instance:
            return Response(
                {"res": "Object with file id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if (file_type == 'song') or (file_type == 'Song'):
            serializer = SongSerializer(file_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif (file_type == 'podcast') or (file_type == 'Podcast'):
            serializer = PodCastSerializer(file_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif (file_type == 'audiobook') or (file_type == 'Audiobook'):
            serializer = AudioBookSerializer(file_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)



    def delete(self, request, file_type, file_id, *args, **kwargs):

        
        file_instance = self.get_object(file_type, file_id)

        if not file_instance:
            return Response(
                {"res": "Object with file id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        file_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


    def put(self, request, file_type, file_id, *args, **kwargs):

        file_instance = self.get_object(file_type, file_id)

        if request.data.get('audioFileType') == 'song':
            
            serializer = SongSerializer(instance=file_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.data.get('audioFileType') == 'podcast':
            
            serializer = PodCastSerializer(instance=file_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.data.get('audioFileType') == 'audiobook':
           
            serializer = AudioBookSerializer(instance=file_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
