from django.contrib import admin

from about_committee.models import *


admin.site.register(Overview)
admin.site.register(Administration)
admin.site.register(CentralOffice)
admin.site.register(Structure)
admin.site.register(FightAgainstCorruption)
admin.site.register(TerritorialDivisions)
admin.site.register(Ifsatasr)
admin.site.register(Board)
admin.site.register(InternationalPartnership)
admin.site.register(StatisticalCouncil)
admin.site.register(PublicCouncil)
admin.site.register(YoungPolicy)
admin.site.register(Vacancies)






































#
# @admin.register(Overview)
# class Overview(TranslationAdmin):
#     list_display = ['title', 'fullname', 'abbreviated_name']
#     list_filter = ['title']
#     search_fields = ['title']
#
#
# @admin.register(Structure)
# class Structure(TranslationAdmin):
#     list_display = ['title']
#     list_filter = ['title']
#     search_fields = ['title']
#
#
# @admin.register(Administration)
# class Administration(TranslationAdmin):
#     list_display = ['positions', 'fullname', 'email', 'phone']
#     list_filter = ['fullname', 'email']
#     search_fields = ['fullname']
#
#
# @admin.register(CentralOffice)
# class CentralOffice(TranslationAdmin):
#     list_display = ['positions', 'fullname', 'email', 'phone', 'departament']
#     list_filter = ['fullname', 'email']
#     search_fields = ['fullname']
#
#
# @admin.register(FightAgainstCorruption)
# class FightAgainstCorruption(TranslationAdmin):
#     list_display = ['title']
#     list_filter = ['title']
#     search_fields = ['title']
#
#
# @admin.register(TerritorialDivisions)
# class TerritorialDivisions(TranslationAdmin):
#     list_display = ['region', 'phone_head', 'address', 'email']
#     list_filter = ['region']
#     search_fields = ['region']
#
#
# @admin.register(Ifsatasr)
# class Ifsatasr(TranslationAdmin):
#     list_display = ['title', 'phone', 'fax', 'email']
#     list_filter = ['title']
#     search_fields = ['title']
#
#
# @admin.register(Board)
# class Board(TranslationAdmin):
#     list_display = ['title']
#     list_filter = ['title']
#     search_fields = ['title']
#
#
# @admin.register(InternationalPartnership)
# class InternationalPartnership(TranslationAdmin):
#     list_display = ['news']
#     list_filter = ['news']
#     search_fields = ['news']
