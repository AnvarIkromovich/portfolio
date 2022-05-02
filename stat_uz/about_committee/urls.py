from django.urls import path
from about_committee.views import *

app_name = 'about_committee'

urlpatterns = [

    path('overview/', OverviewListView.as_view(), name='overview'),
    path('structure/', StructureListView.as_view(), name='structure'),
    path('administration/', AdministrationListView.as_view(), name='administration'),
    path('centraloffice/', CentralofficeListView.as_view(), name='centraloffice'),
    path('fightagainstcorruption/', FightagainstcorruptionListView.as_view(), name='fightagainstcorruption'),
    path('territorialdivisions/', TerritorialDivisionsListView.as_view(), name='territorialdivisions'),
    path('board/', BoardListView.as_view(), name='board'),
    path('ifsatasr/', IfsatasrListView.as_view(), name='ifsatasr'),
    path('internationalpartnership/', InternationalPartnershipListView.as_view(), name='internationalpartnership'),
    path('administration/<int:pk>', FunctionalDuties.as_view(), name='functional_duties'),
    path('administration/<int:pk>', Biography.as_view(), name='biography'),
    path('statisticalcouncil/', StatisticalCouncilListView.as_view(), name='statisticalcouncil'),
    path('publiccouncil/', PublicCouncilListView.as_view(), name='publiccouncil'),
    path('youngpolicy/', YoungPolicyListView.as_view(), name='youngpolicy'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies'),
    path('', HomeTemplateViews.as_view(), name='home')
]