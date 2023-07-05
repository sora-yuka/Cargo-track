from rest_framework.response import Response

from applications.feedback.models import Rating
from applications.feedback.serializers import RatingSerializer


class FeedbackMixin:
    
    def rating(self, request, pk=None, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            rating_obj, _ = Rating.objects.get_or_create(owner=request.user, worker_id=pk)
            rating_obj.rating = request.data['rating']
            rating_obj.save()
            msg = request.data['rating']
            return Response(f'You give {msg} points!')
        except:
            return Response('Something went wrong!')