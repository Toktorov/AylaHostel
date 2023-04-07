from modeltranslation.translator import translator, TranslationOptions
from apps.settings.models import Setting, Benefit

class SettingTranslationOptions(TranslationOptions):
    fields = ('description', )

class BenefitTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Setting, SettingTranslationOptions)
translator.register(Benefit, BenefitTranslationOptions)