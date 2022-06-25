from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
from api.models import Series
from api.serializers import SeriesSerializer
from rest_framework.pagination import LimitOffsetPagination


class SeriesViewSet(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name',)
    pagination_class = LimitOffsetPagination

