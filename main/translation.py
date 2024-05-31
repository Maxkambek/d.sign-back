from modeltranslation.translator import TranslationOptions, register

from .models import Service


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
