from collections import OrderedDict

from django.contrib.auth import get_user_model
from rest_framework import views, generics, response, permissions, filters, pagination, status

from . import serializers
from .models import Word, Category, Rotatsiya

User = get_user_model()


class CategoryListAPIViews(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()


class WordPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return response.Response(OrderedDict([
            ('object_count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('items', data)
        ]))


class WordAPIViews(views.APIView):
    def get(self, request):
        quantity = Word.objects.count()
        return response.Response({'number': quantity})


class WordListAPIViews(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.WordSerializer
    queryset = Word.objects.all()
    pagination_class = WordPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class WordDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]
    serializer_class = serializers.WordSerializer
    queryset = Word.objects.all()
    lookup_field = 'id'


class RotationApiView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Rotatsiya.objects.all()
    serializer_class = serializers.RotatsiyaSerializer


class UserListAPIViews(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserNUMAPIViews(views.APIView):
    def get(self, request):
        quantity = User.objects.count()
        return response.Response({'user_number': quantity})


class UserRegisterView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = serializers.UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


class UserLoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


class LogoutView(views.APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return response.Response(status=status.HTTP_200_OK)
