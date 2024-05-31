from django.contrib import admin
from .models import Service, Project, Partner, Reviews, GetInTouch, OurStory
from modeltranslation.admin import TranslationAdmin


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass


@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    pass


@admin.register(OurStory)
class OurStoryAdmin(admin.ModelAdmin):
    pass
