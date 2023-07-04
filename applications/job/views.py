from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from applications.job.models import Job
from applications.job.permissions import IsShipper, IsCompanyOrCarrier
from applications.job.serializers import JobOfferSerializer, JobSerializer
from applications.profiles.models import BaseProfile


def index(request):
    return render(request, "applications/job/template/index.html")



class PaginationApiView(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_size_query_param = 'jobs'


class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = [IsShipper]
    
    pagination_class = PaginationApiView
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['title']
    search_fields = ['title']
    
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    
    def get_queryset(self):
        try:
            if BaseProfile.objects.get(user=self.request.user.id).shipper:
                queryset = super().get_queryset()
                queryset = queryset.filter(owner=self.request.user)
                return queryset
        except:
            return super().get_queryset()
    
    
    @action(detail=True, methods=['GET'])
    def recommend(self, request, pk=None):
        destination_location = self.get_object().destination_location
        delivery_date = self.get_object().delivery_date
        queryset = Job.objects.filter(pickup_location=destination_location, pickup_date=delivery_date)
        serializers = JobSerializer(queryset, many=True)
        return Response(serializers.data)
    
    
class JobOfferApiView(UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobOfferSerializer
    permission_classes = [IsCompanyOrCarrier]
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    
    
class JobConfirmApiView(APIView):
    def get(self, request, code, pk):
        job = get_object_or_404(Job, pk=pk, activation_code=code)
        job = Job.objects.get(pk=pk, activation_code=code)
        print(job.pk)
        if not job.is_confirm:
            job.status = 'Delivering'
            job.is_confirm = True
            job.started_at = timezone.now()
            job.save(update_fields=['is_confirm', 'status', 'started_at'])
            return Response({'message': 'You have confirmed the order'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have already confirmed the order'}, status=status.HTTP_400_BAD_REQUEST)
    
    
class JobCompleteApiView(APIView):
    def get(self, request, code, pk):
        job = get_object_or_404(Job, pk=pk, complete_code=code)
        job = Job.objects.get(pk=pk, complete_code=code)
        if job.status != 'Completed':
            job.status = 'Completed'
            job.save(update_fields=['status'])
            return Response({'message': 'You have successfully completed this job'}, status=status.HTTP_200_OK)
        return Response({'message': 'You already completed this job'}, status=status.HTTP_404_NOT_FOUND)
    
    
class JobCanselApiView(APIView):
    def get(self, request, code, pk):
        job = get_object_or_404(Job, pk=pk, cancel_code=code)
        job = Job.objects.get(pk=pk, cancel_code=code)
        
        time_since_request = timezone.now() - job.started_at
        if time_since_request.total_seconds() > 10:
            return Response({'message': 'Time to cancel this job has expired'}, status=status.HTTP_404_NOT_FOUND)
             
        if job.is_confirm:
            job.is_confirm = False
            job.status = 'Looking for shipper' 
            job.driver_id = ''
            job.save(update_fields=['status', 'is_confirm', 'driver_id'])
            return Response({'message': 'This job was canceled'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have already canceled this job'}, status=status.HTTP_404_NOT_FOUND)
    
    
class JobHistoryViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = []
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(driver_id = self.request.user.id)
        return queryset
        
        
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(is_confirm=True)
    #     return queryset
    
    
    
    
    
