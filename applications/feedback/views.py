from rest_framework.response import Response

from applications.feedback.models import CRating, DRating
from applications.feedback.serializers import CRatingSerializer, DRatingSerializer


class FeedbackMixin:
    
    def rating(self, request, pk=None, *args, **kwargs):
        try:
            serializer = CRatingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            rating_obj, _ = CRating.objects.get_or_create(owner=request.user, worker_id=pk)
            rating_obj.rating = request.data['rating']
            rating_obj.save()
            msg = request.data['rating']
            return Response(f'You give {msg} points!')
        except:
            serializer = DRatingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            rating_obj, _ = DRating.objects.get_or_create(owner=request.user, worker_id=pk)
            rating_obj.rating = request.data['rating']
            rating_obj.save()
            msg = request.data['rating']
            return Response(f'You give {msg} points!')
        