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
from django.utils import timezone

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
            job.status = 'Delivering'
            job.is_confirm = True
            job.started_at = timezone.now()
            job.save(update_fields=['is_confirm', 'status', 'started_at'])
            return Response({'message': 'You have confirmed order'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have already confirmed order'}, status=status.HTTP_400_BAD_REQUEST)
    
    
class JobCompleteApiView(APIView):
    def get(self, request, code):
        job = get_object_or_404(Job, complete_code=code)
        job = Job.objects.get(complete_code=code)
        if job.status != 'Completed':
            job.status = 'Completed'
            job.save(update_fields=['status'])
            return Response({'message': 'You have successfully completed this job'}, status=status.HTTP_200_OK)
        return Response({'message': 'You already completed this job'}, status=status.HTTP_404_NOT_FOUND)
    
    
class JobCanselApiView(APIView):
    def get(self, request, code):
        job = get_object_or_404(Job, cancel_code=code)
        job = Job.objects.get(cancel_code=code)
        
        time_since_request = timezone.now() - job.started_at
        if time_since_request.total_seconds() > 10:
            return Response({'message': 'Time to cancel this job has expired'}, status=status.HTTP_404_NOT_FOUND)
             
        if job.is_confirm:
            job.is_confirm = False
            job.status = 'Looking for shipper' 
            job.save(update_fields=['status', 'is_confirm'])
            return Response({'message': 'This job was canceled'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have already canceled this job'}, status=status.HTTP_404_NOT_FOUND)
    
    
    
    
    
