from modeltranslation.translator import register, TranslationOptions
from schoolsite220.models import *


@register(AboutSchool)
class AboutSchoolTranslationOptions(TranslationOptions):
    fields = ('title', 'describtions',)


@register(Managements)
class ManagementsTranslationOptions(TranslationOptions):
    fields = ('fullname', 'pozitions','biografy',)


@register(Staff)
class StaffTranslationOptions(TranslationOptions):
    fields = ('fullname','pozitions','biografy',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title','short_descriptions','descriptions',)


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Features)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Courses)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('course_name','short_description','description',)


@register(Students)
class StudentsTranslationOptions(TranslationOptions):
    fields = ('content','fullname','title',)

