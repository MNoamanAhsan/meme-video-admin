from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Category, Memes
from .serializers import CategorySerializer, MemeSerializer
from django.db.models import Q


class CategoryListView(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class MemeSearchApi(generics.ListAPIView):
    serializer_class=MemeSerializer

    def get_queryset(self):
        query=self.request.GET.get('q',None)
        if query:
            return Memes.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query))
        return Memes.objects.none()



