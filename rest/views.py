from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
#noinspection PyUnresolvedReferences
from rest_framework import mixins
from .models import Article
from .serializers import ArticleSerializer
#noinspection PyUnresolvedReferences
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
#noinspection PyUnresolvedReferences
from rest_framework.permissions import IsAuthenticated
#noinspection PyUnresolvedReferences
from rest_framework import viewsets
#noinspection PyUnresolvedReferences
from django.shortcuts import get_object_or_404
#noinspection PyUnresolvedReferences
from django_filters import rest_framework as filters
#noinspection PyUnresolvedReferences
from rest_framework.filters import SearchFilter, OrderingFilter

class ArticleList(APIView):
    def get(self,request):
        queryset=Article.objects.all()
        serializer=ArticleSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=204)


#Gneeric views and mixins
class Articlegenericview(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    queryset = Article.objects.all()
    serializer_class=ArticleSerializer
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)

class ArticleViewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Article.objects.all()
        serializer=ArticleSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,id=None):
        queryset = Article.objects.all()
        article=get_object_or_404(queryset,id=id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.DjangoFilterBackend,OrderingFilter,SearchFilter)   #Go to this URl for browsabale API ---> http://127.0.0.1:8000/api/article/?name=Ashu
    filter_fields =('name',)
    ordering_fields=('city',)
    search_fields=('department',)


