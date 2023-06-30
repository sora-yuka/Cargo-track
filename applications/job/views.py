from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import mixins
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from applications.job.models import Job
from applications.job.permissions import ShipperOnly
from applications.job.serializers import JobOfferSerializer, JobSerializer


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
    
    
class JobOfferApiView(UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobOfferSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    
    
class JobConfirmApiView(APIView):
    def get(self, request, code):
        job = get_object_or_404(Job, activation_code=code)
        job = Job.objects.get(activation_code=code)
        if not job.is_confirm:
            job.is_confirm = True
            job.save(update_fields=['is_confirm', 'activation_code'])
            return Response({'message': 'You have confirmed order'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have already confirmed order'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
