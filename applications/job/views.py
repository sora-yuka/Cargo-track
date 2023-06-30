from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from applications.job.models import Job
from applications.job.permissions import ShipperOnly
from applications.job.serializers import JobSerializer


class PaginationApiView(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_size_query_param = 'jobs'

class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = [ShipperOnly]
    
    pagination_class = PaginationApiView
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['title']
    search_fields = ['title']
    
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    
