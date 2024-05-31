from rest_framework import generics

from .models import Service, Project, Partner, Reviews, GetInTouch, OurStory
from .serializers import ServiceSerializer, ProjectSerializer, PartnerSerializer, ReviewsSerializer, \
    GetInTouchSerializer, OurStorySerializer


class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        service = self.request.query_params.get('service', None)
        if service:
            queryset = queryset.filter(service_id=service)
        return queryset


class PartnerList(generics.ListAPIView):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class ReviewList(generics.ListAPIView):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()


class GetInTouchCreate(generics.CreateAPIView):
    serializer_class = GetInTouchSerializer
    queryset = GetInTouch.objects.all()


class OurStoryList(generics.ListAPIView):
    serializer_class = OurStorySerializer
    queryset = OurStory.objects.all()
