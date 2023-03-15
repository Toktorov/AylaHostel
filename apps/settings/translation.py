from modeltranslation.translator import translator, TranslationOptions
from apps.settings.models import Setting

class SettingTranslationOptions(TranslationOptions):
    fields = ('description', )

translator.register(Setting, SettingTranslationOptions)