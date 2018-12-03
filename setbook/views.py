from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import HeroInfo
from setbook.serializers import HeroSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class HerosView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # 封装查询集
    queryset = HeroInfo.objects.filter(id__gt=17)
    # 序列化器
    serializer_class = HeroSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class HeroView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView):
    # 　封装查询集
    queryset = HeroInfo.objects.all()
    # 序列化器
    serializer_class = HeroSerializer

    # 根据主键查询单个对象
    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class Heros2View(generics.ListCreateAPIView):
    queryset = HeroInfo.objects.all()
    serializer_class = HeroSerializer

class Hero2View(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeroInfo.objects.all()
    serializer_class = HeroSerializer

class HeromodelView(ModelViewSet):
    # 定义查询集
    queryset = HeroInfo.objects.all()
    # 定义序列化器对象
    serializer_class = HeroSerializer
    @action(methods=['get'],detail=False)
    def latest(self,request):
        query = HeroInfo.objects.filter(pk__gt=10).all()
        serializer = HeroSerializer(query,many=True)
        return  Response(serializer.data)




