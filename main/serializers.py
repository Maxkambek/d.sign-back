from .models import Service, Project, Partner, Reviews, GetInTouch, OurStory
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'name',
            'description'
        ]


class ProjectSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=False)

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'image',
            'file',
            'service'
        ]


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            'id',
            'name',
            'logo'
        ]


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = [
            'id',
            'name',
            'description'
        ]


class GetInTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetInTouch
        fields = [
            'id',
            'name',
            'description',
            'email',
            'phone'
        ]


class OurStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurStory
        fields = [
            'id',
            'name',
            'image'
        ]
